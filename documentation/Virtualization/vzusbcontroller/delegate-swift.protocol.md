# VZUSBController.Delegate

**Framework**: Virtualization  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- macOS 27.0+

## Declaration

```swift
protocol Delegate : NSObjectProtocol
```

```objc
@protocol VZUSBControllerDelegate <NSObject>
```

#### Overview

Delegate object for a VZUSBController.

A class conforming to the VZUSBControllerDelegate protocol can provide methods that get invoked when the USB controller’s state changes.

## Topics

### Instance Methods
- [func usbController(VZUSBController, usbPassthroughDeviceDidDisconnect: VZUSBPassthroughDevice)](./delegate-swift.protocol/usbcontroller%28_,usbpassthroughdevicediddisconnect%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbcontroller/delegate-swift.protocol)*