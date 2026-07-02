#ifndef TPVECTOR_H
#define TPVECTOR_H

#include "dtoolbase.h"
#include "pvector.h"

#ifndef USE_STL_ALLOCATOR
// If we're not using custom allocators, just use the standard class
// definition.
#define tpvector pvector

#elif defined(CPPPARSER)
// Simplified definition to speed up Interrogate parsing.
template<class Type>
class tpvector : public pvector<Type> {
};

#else

// We want this for thread support for safe emplace_back and push_back.
#include "lightReMutex.h"
#include "lightReMutexHolder.h"

/**
 * This is our own Panda specialization on the default STL vector.  Its main
 * purpose is to call the hooks for MemoryUsage to properly track STL-
 * allocated memory.
 *
 *
 * In addition this version of of vector is made to be more thread safe on use.
 */
template<class Type>
class tpvector : public pvector<Type> {
    private:
        // We need the thread lock for some functions to work right in a thread.
        // We will use re-mutex so we don't run into multi-lock issues in any form.
        static LightReMutex _tpvector_thread_lock;

    public:
        typedef pvector<Type> base_class;
        typedef typename base_class::size_type size_type;

        tpvector<Type> &operator =(const tpvector<Type> &copy) {
            base_class::operator =(copy);
            return *this;
        }

        tpvector<Type> &operator =(tpvector<Type> &&from) noexcept {
            base_class::operator =(std::move(from));
            return *this;
        }

        INLINE void push_back(const Type &value) {
            // Lock our thread, We don't want to cause thread thrashing.
            LightReMutexHolder holder(_tpvector_thread_lock);
            
            base_class::push_back(value);
        }

        INLINE void push_back(Type &&value) {
            // Lock our thread, We don't want to cause thread thrashing.
            LightReMutexHolder holder(_tpvector_thread_lock);
            
            base_class::push_back(value);
        }

        template <class... Args>
        INLINE void emplace_back(Args&&... args) {
            // Lock our thread, We don't want to cause thread thrashing.
            LightReMutexHolder holder(_tpvector_thread_lock);
              
            base_class::emplace_back(std::forward<Args>(args)...);
        }
};

template <class Type> 
LightReMutex tpvector<Type>::_tpvector_thread_lock("tpvector-thread-lock");

#endif  // USE_STL_ALLOCATOR

#endif // TPVECTOR_H
