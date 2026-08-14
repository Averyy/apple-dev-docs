# VZUSBController.Delegate

**Framework**: Virtualization  
**Kind**: protocol

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol Delegate : NSObjectProtocol
```

#### Overview

Delegate object for a VZUSBController.

A class conforming to the VZUSBControllerDelegate protocol can provide methods that get invoked when the USB controller’s state changes.

## Topics

### Instance Methods
- [func usbController(VZUSBController, usbPassthroughDeviceDidDisconnect: VZUSBPassthroughDevice)](vzusbcontroller/delegate-swift.protocol/usbcontroller(_:usbpassthroughdevicediddisconnect:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbcontroller/delegate-swift.protocol)*