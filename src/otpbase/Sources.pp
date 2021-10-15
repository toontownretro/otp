#begin interface_target
  #define TARGET otpbase

  #define BUILDING_DLL BUILDING_OTP_OTPBASE

  #define OTHER_LIBS dtoolbase:c dtool:m

  #define USE_PACKAGES eigen

  #define SOURCES \
    otpbase.h otpsymbols.h \

  #define INSTALL_HEADERS \
    otpbase.h otpsymbols.h

#end interface_target
