# kIOMessageSystemWillPowerOn

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.3+
- visionOS 1.0+

## Declaration

```c
#define kIOMessageSystemWillPowerOn
```

#### Discussion

Announces that the system is beginning to power the device tree; most devices are unavailable at this point.. Delivered to in-kernel IOKit drivers via `kIOGeneralInterest` and `kIOPriorityPowerStateInterest`. Delivered to user clients of `IORegisterForSystemPower`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiomessagesystemwillpoweron)*