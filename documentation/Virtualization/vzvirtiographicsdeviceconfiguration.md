# VZVirtioGraphicsDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

Configuration that represents the configuration of a Virtio graphics device for a Linux VM.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZVirtioGraphicsDeviceConfiguration
```

## Topics

### Creating the configuration object
- [init()](vzvirtiographicsdeviceconfiguration/init.md)
  Creates a new Virtio graphics device.
### Instance properties
- [var scanouts: [VZVirtioGraphicsScanoutConfiguration]](vzvirtiographicsdeviceconfiguration/scanouts.md)
  The array of output devices.
- [class VZVirtioGraphicsScanoutConfiguration](vzvirtiographicsscanoutconfiguration.md)
  The configuration for a Virtio graphics device that configures the dimensions of the graphics device for a Linux VM.

## Relationships

### Inherits From
- [VZGraphicsDeviceConfiguration](vzgraphicsdeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZGraphicsDisplayConfiguration](vzgraphicsdisplayconfiguration.md)
  The base class for a graphics display configuration.
- [class VZMacGraphicsDeviceConfiguration](vzmacgraphicsdeviceconfiguration.md)
  Configuration for a display attached to a Mac graphics device.
- [class VZMacGraphicsDisplayConfiguration](vzmacgraphicsdisplayconfiguration.md)
  The configuration for a Mac graphics device.
- [class VZGraphicsDeviceConfiguration](vzgraphicsdeviceconfiguration.md)
  The base class for a graphics device configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiographicsdeviceconfiguration)*