# kIOMessageCanDevicePowerOff

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
#define kIOMessageCanDevicePowerOff
```

#### Discussion

Delivered to `kIOAppPowerStateInterest` clients of devices that implement their own idle timeouts. This message type is almost never used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiomessagecandevicepoweroff)*