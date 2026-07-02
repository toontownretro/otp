/**
 * PANDA 3D SOFTWARE
 * Copyright (c) Carnegie Mellon University.  All rights reserved.
 *
 * All use of this software is subject to the terms of the revised BSD
 * license.  You should have received a copy of this license along
 * with this source code in a file named "LICENSE."
 *
 * @file config_navigation.h
 * @author brian
 * @date 2021-10-12
 */

#ifndef CONFIG_NAVIGATION_H
#define CONFIG_NAVIGATION_H

#include "otpbase.h"
#include "dconfig.h"

ConfigureDecl(config_navigation, EXPCL_OTP_NAVIGATION, EXPTP_OTP_NAVIGATION);

extern EXPCL_OTP_NAVIGATION void init_libnavigation();

#endif // CONFIG_NAVIGATION_H
