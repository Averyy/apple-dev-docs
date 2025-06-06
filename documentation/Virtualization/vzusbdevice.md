# VZUSBDevice

**Framework**: Virtualization  
**Kind**: protocol

A protocol that represents a USB device in a VM.

**Availability**:
- macOS 15.0+

## Declaration

```swift
protocol VZUSBDevice : NSObjectProtocol
```

#### Overview

Classes that conform to this protocol represent hot-pluggable USB devices.

> ❗ **Important**:  Don’t use the `VZUSBDevice` protocol with objects outside the Virtualization framework. This protocol only describes capabilities of Virtualization framework objects.

 Don’t use the `VZUSBDevice` protocol with objects outside the Virtualization framework. This protocol only describes capabilities of Virtualization framework objects.

## Topics

### Properties
- [var usbController: VZUSBController?](vzusbdevice/usbcontroller.md)
  The USB controller that has an attachment to the device.
- [var uuid: UUID](vzusbdevice/uuid.md)
  The device’s unique identifier.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [VZUSBMassStorageDevice](vzusbmassstoragedevice.md)

## See Also

- [class VZUSBMassStorageDevice](vzusbmassstoragedevice.md)
  A class that represents a hot-pluggable USB mass storage device.
- [protocol VZUSBDeviceConfiguration](vzusbdeviceconfiguration.md)
  The protocol for configuring USB devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbdevice)*