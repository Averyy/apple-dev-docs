# kIOMessageCanSystemSleep

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```c
#define kIOMessageCanSystemSleep
```

## Discussion

Announces/Requests permission to proceed to system sleep. Delivered to in-kernel IOKit drivers via `kIOGeneralInterest` and `kIOPriorityPowerStateInterest`. Delivered to user clients of `IORegisterForSystemPower`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiomessagecansystemsleep)*