%module wallaby
%{
  #include "wallaby.h"


  #ifdef SWIGPYTHON
  #define _open open
  #endif

  #define CameraDevice Device
%}

#define EXPORT_SYM

#ifdef SWIGPYTHON
#define open _open
#endif

%include "vtable.h"
%include "motors.h"
%include "graphics.h"
%include "geom.h"
%include "servo.h"
%include "util.h"
%include "create.h"
%include "battery.h"
%include "analog.h"
%include "general.h"
%include "accel.h"
%include "camera.h"
%include "button.h"
%include "botball.h"
%include "console.h"
%include "audio.h"
%include "thread.h"
%include "digital.h"
