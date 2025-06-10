# VZUSBDeviceConfiguration

**Framework**: Virtualization  
**Kind**: protocol

The protocol for configuring USB devices.

**Availability**:
- macOS 15.0+

## Declaration

```swift
protocol VZUSBDeviceConfiguration : NSObjectProtocol
```

#### Overview

Classes that conform to this protocol represent hot-pluggable USB device configurations.

> ❗ **Important**:  Don’t use the `VZUSBDeviceConfiguration` protocol with objects outside the Virtualization framework. This protocol only describes capabilities of Virtualization framework objects.

## Topics

### Properties
- [var uuid: UUID](vzusbdeviceconfiguration/uuid.md)
  The device’s unique identifier.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [VZUSBMassStorageDeviceConfiguration](vzusbmassstoragedeviceconfiguration.md)

## See Also

- [protocol VZUSBDevice](vzusbdevice.md)
  A protocol that represents a USB device in a VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbdeviceconfiguration)*