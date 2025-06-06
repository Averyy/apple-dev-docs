# VZMacTrackpadConfiguration

**Framework**: Virtualization  
**Kind**: class

The class that represents the configuration for a Mac trackpad.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZMacTrackpadConfiguration
```

#### Overview

> **Note**:  The framework recognizes this device in virtual machines running macOS 13 and later. To support both macOS 13.0 and earlier guests, set [`pointingDevices`](vzvirtualmachineconfiguration/pointingdevices.md) to an array that contains both a [`VZMacTrackpadConfiguration`](vzmactrackpadconfiguration.md) and a [`VZUSBScreenCoordinatePointingDeviceConfiguration`](vzusbscreencoordinatepointingdeviceconfiguration.md) object.

 The framework recognizes this device in virtual machines running macOS 13 and later. To support both macOS 13.0 and earlier guests, set [`pointingDevices`](vzvirtualmachineconfiguration/pointingdevices.md) to an array that contains both a [`VZMacTrackpadConfiguration`](vzmactrackpadconfiguration.md) and a [`VZUSBScreenCoordinatePointingDeviceConfiguration`](vzusbscreencoordinatepointingdeviceconfiguration.md) object.

The [`VZVirtualMachineView`](vzvirtualmachineview.md) uses this device to send pointer events and multi-touch trackpad gestures to the virtual machine. In macOS 13 and later, guests use the multi-touch trackpad device, while earlier versions of macOS uses the USB pointing device.

## Topics

### Initializers
- [init()](vzmactrackpadconfiguration/init.md)
  Creates a new Mac trackpad configuration.

## Relationships

### Inherits From
- [VZPointingDeviceConfiguration](vzpointingdeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZUSBScreenCoordinatePointingDeviceConfiguration](vzusbscreencoordinatepointingdeviceconfiguration.md)
  An object that defines the configuration for a USB pointing device that reports absolute coordinates.
- [class VZPointingDeviceConfiguration](vzpointingdeviceconfiguration.md)
  The base class for a pointing device configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmactrackpadconfiguration)*