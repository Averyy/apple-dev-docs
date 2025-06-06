# VZUSBController

**Framework**: Virtualization  
**Kind**: class

A class that represents a USB controller in a VM.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class VZUSBController
```

#### Overview

Don’t create a `VZUSBController` directly. You need to first configure USB controllers on a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) through a subclass of [`VZUSBControllerConfiguration`](vzusbcontrollerconfiguration.md). When you create a [`VZVirtualMachine`](vzvirtualmachine.md) from the configuration, the USB controllers are available through the [`usbControllers`](vzvirtualmachine/usbcontrollers.md) property.

The concrete type of a `VZUSBController` corresponds to the type the configuration uses. For example, a [`VZXHCIControllerConfiguration`](vzxhcicontrollerconfiguration.md) leads to a device of type [`VZXHCIController`](vzxhcicontroller.md).

## Topics

### Instance properties
- [var usbDevices: [any VZUSBDevice]](vzusbcontroller/usbdevices.md)
  The list of attached USB devices for the controller.
### Attaching and detaching devices
- [func attach(device: any VZUSBDevice, completionHandler: ((any Error)?) -> Void)](vzusbcontroller/attach(device:completionhandler:).md)
  Attaches a USB device to the controller.
- [func detach(device: any VZUSBDevice, completionHandler: ((any Error)?) -> Void)](vzusbcontroller/detach(device:completionhandler:).md)
  Detaches a USB device from the controller.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZXHCIController](vzxhcicontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZXHCIController](vzxhcicontroller.md)
  A class that represents a USB Extensible Host Controller Interface (XHCI) controller in a VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbcontroller)*