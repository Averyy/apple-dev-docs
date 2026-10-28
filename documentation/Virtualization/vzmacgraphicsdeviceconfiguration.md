# VZMacGraphicsDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

Configuration for a display attached to a Mac graphics device.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZMacGraphicsDeviceConfiguration
```

```objc
@interface VZMacGraphicsDeviceConfiguration : VZGraphicsDeviceConfiguration
```

## Overview

Use this device to attach a display that’s shown in a [`VZVirtualMachineView`](./vzvirtualmachineview.md).

## Topics

### Creating the graphics device configuration
- [init()](./vzmacgraphicsdeviceconfiguration/init%28%29.md)
  Creates a new Mac graphics device configuration.
### Configuring displays
- [var displays: [VZMacGraphicsDisplayConfiguration]](./vzmacgraphicsdeviceconfiguration/displays.md)
  The displays associated with this graphics device.

## Relationships

### Inherits From
- [VZGraphicsDeviceConfiguration](./vzgraphicsdeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configurations
- [class VZGraphicsDisplayConfiguration](./vzgraphicsdisplayconfiguration.md)
  The base class for a graphics display configuration.
- [class VZMacGraphicsDisplayConfiguration](./vzmacgraphicsdisplayconfiguration.md)
  The configuration for a Mac graphics device.
- [class VZGraphicsDeviceConfiguration](./vzgraphicsdeviceconfiguration.md)
  The base class for a graphics device configuration.
- [class VZVirtioGraphicsDeviceConfiguration](./vzvirtiographicsdeviceconfiguration.md)
  Configuration that represents the configuration of a Virtio graphics device for a Linux VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacgraphicsdeviceconfiguration)*