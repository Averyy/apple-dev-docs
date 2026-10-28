# VZUSBScreenCoordinatePointingDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

An object that defines the configuration for a USB pointing device that reports absolute coordinates.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZUSBScreenCoordinatePointingDeviceConfiguration
```

```objc
@interface VZUSBScreenCoordinatePointingDeviceConfiguration : VZPointingDeviceConfiguration
```

## Overview

A `VZVirtualMachineView` can use this device to send pointer events to the VM.

## Topics

### Creating pointing devices
- [init()](./vzusbscreencoordinatepointingdeviceconfiguration/init%28%29.md)
  Creates a new pointing device.

## Relationships

### Inherits From
- [VZPointingDeviceConfiguration](./vzpointingdeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Pointing devices
- [class VZMacTrackpadConfiguration](./vzmactrackpadconfiguration.md)
  The class that represents the configuration for a Mac trackpad.
- [class VZPointingDeviceConfiguration](./vzpointingdeviceconfiguration.md)
  The base class for a pointing device configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbscreencoordinatepointingdeviceconfiguration)*