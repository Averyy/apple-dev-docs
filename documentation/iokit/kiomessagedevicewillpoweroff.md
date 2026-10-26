# kIOMessageDeviceWillPowerOff

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
#define kIOMessageDeviceWillPowerOff
```

#### Discussion

Indicates the device is about to move to a lower power state. Sent to IOKit interest notification clients of type `kIOAppPowerStateInterest` and `kIOGeneralInterest`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiomessagedevicewillpoweroff)*