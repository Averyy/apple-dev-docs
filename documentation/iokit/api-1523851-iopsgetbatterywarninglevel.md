# IOPSGetBatteryWarningLevel

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Indicates whether the system is at a low battery warning level.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
IOPSLowBatteryWarningLevel IOPSGetBatteryWarningLevel(void);
```

## Discussion

If your app runs in full screen mode and occludes macOS's battery monitor's low battery warnings, you should alert the user at least when the system is in kIOPSLowBatteryWarnFinal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1523851-iopsgetbatterywarninglevel)*