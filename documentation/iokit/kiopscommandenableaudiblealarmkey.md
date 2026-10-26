# kIOPSCommandEnableAudibleAlarmKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Command to give a UPS when it should either enable or disable the audible alarm.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
#define kIOPSCommandEnableAudibleAlarmKey
```

#### Discussion

- The matching argument should be a CFBooleanRef where kCFBooleanTrue enables the alarm and
- kCFBooleanFalse diables the alarm


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopscommandenableaudiblealarmkey)*