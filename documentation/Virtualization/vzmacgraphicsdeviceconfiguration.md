# VZMacGraphicsDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

Configuration for a display attached to a Mac graphics device.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZMacGraphicsDeviceConfiguration
```

#### Overview

Use this device to attach a display that’s shown in a [`VZVirtualMachineView`](vzvirtualmachineview.md).

## Topics

### Creating the graphics device configuration
- [init()](vzmacgraphicsdeviceconfiguration/init.md)
  Creates a new Mac graphics device configuration.
### Configuring displays
- [var displays: [VZMacGraphicsDisplayConfiguration]](vzmacgraphicsdeviceconfiguration/displays.md)
  The displays associated with this graphics device.

## Relationships

### Inherits From
- [VZGraphicsDeviceConfiguration](vzgraphicsdeviceconfiguration.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZGraphicsDisplayConfiguration](vzgraphicsdisplayconfiguration.md)
  The base class for a graphics display configuration.
- [class VZMacGraphicsDisplayConfiguration](vzmacgraphicsdisplayconfiguration.md)
  The configuration for a Mac graphics device.
- [class VZGraphicsDeviceConfiguration](vzgraphicsdeviceconfiguration.md)
  The base class for a graphics device configuration.
- [class VZVirtioGraphicsDeviceConfiguration](vzvirtiographicsdeviceconfiguration.md)
  Configuration that represents the configuration of a Virtio graphics device for a Linux VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacgraphicsdeviceconfiguration)*