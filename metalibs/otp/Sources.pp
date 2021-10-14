// DIR_TYPE "metalib" indicates we are building a shared library that
// consists mostly of references to other shared libraries.  Under
// Windows, this directly produces a DLL (as opposed to the regular
// src libraries, which don't produce anything but a pile of OBJ files
// under Windows).

#define DIR_TYPE metalib

#if $[BUILD_COMPONENTS]
#define BUILDING_DLL BUILDING_OTP_STUB
#else
#define BUILDING_DLL BUILDING_OTP
#endif

#define COMPONENT_LIBS \
   otpbase settings nametag movement secure navigation

#define OTHER_LIBS direct:m panda:m pandaexpress:m dtool:m \
    express:c prc event:c pgraph:c pgraphnodes:c linmath:c gobj:c \
    anim:c putil:c mathutil:c downloader:c mathutil:c \
    pandabase:c recorder:c grutil:c collide:c device:c \
    dgraph:c display:c gsgbase:c parametrics:c text:c pnmimage:c \
    dtoolutil:c interrogatedb interval:c dtoolbase:c \
    pipeline:c pstatclient:c cull:c pnmimagetypes:c \
    tform:c audio:c pgui:c directbase:c dcparser:c showbase:c \
    deadrec:c distributed:c motiontrail:c movies:c \
    $[if $[HAVE_NET],net:c] $[if $[WANT_NATIVE_NET],nativenet:c]

#if $[HAVE_FREETYPE]
    #define OTHER_LIBS $[OTHER_LIBS] pnmtext:c
  #endif

#begin metalib_target
  #define TARGET otp

  #define SOURCES otp.cxx
#end metalib_target
