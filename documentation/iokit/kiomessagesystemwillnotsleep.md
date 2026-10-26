# kIOMessageSystemWillNotSleep

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
#define kIOMessageSystemWillNotSleep
```

#### Discussion

Announces that the system has retracted a previous attempt to sleep; it follows `kIOMessageCanSystemSleep`. Delivered to in-kernel IOKit drivers via `kIOGeneralInterest` and `kIOPriorityPowerStateInterest`. Delivered to user clients of `IORegisterForSystemPower`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiomessagesystemwillnotsleep)*