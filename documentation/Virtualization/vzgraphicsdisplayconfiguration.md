# VZGraphicsDisplayConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The base class for a graphics display configuration.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class VZGraphicsDisplayConfiguration
```

```objc
@interface VZGraphicsDisplayConfiguration : NSObject
```

#### Overview

Don’t instantiate `VZGraphicsDisplayConfiguration` directly. Use one of its subclasses instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZMacGraphicsDisplayConfiguration](./vzmacgraphicsdisplayconfiguration.md)
- [VZVirtioGraphicsScanoutConfiguration](./vzvirtiographicsscanoutconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZVirtioGraphicsScanoutConfiguration](./vzvirtiographicsscanoutconfiguration.md)
  The configuration for a Virtio graphics device that configures the dimensions of the graphics device for a Linux VM.
### Configurations
- [class VZMacGraphicsDeviceConfiguration](./vzmacgraphicsdeviceconfiguration.md)
  Configuration for a display attached to a Mac graphics device.
- [class VZMacGraphicsDisplayConfiguration](./vzmacgraphicsdisplayconfiguration.md)
  The configuration for a Mac graphics device.
- [class VZGraphicsDeviceConfiguration](./vzgraphicsdeviceconfiguration.md)
  The base class for a graphics device configuration.
- [class VZVirtioGraphicsDeviceConfiguration](./vzvirtiographicsdeviceconfiguration.md)
  Configuration that represents the configuration of a Virtio graphics device for a Linux VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdisplayconfiguration)*