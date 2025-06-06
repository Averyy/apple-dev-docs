# VZPointingDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

The base class for a pointing device configuration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZPointingDeviceConfiguration
```

#### Overview

Don’t instantiate a `VZPointingDeviceConfiguration` directly, use one of its subclasses like [`VZUSBScreenCoordinatePointingDeviceConfiguration`](vzusbscreencoordinatepointingdeviceconfiguration.md) instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZMacTrackpadConfiguration](vzmactrackpadconfiguration.md)
- [VZUSBScreenCoordinatePointingDeviceConfiguration](vzusbscreencoordinatepointingdeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZMacTrackpadConfiguration](vzmactrackpadconfiguration.md)
  The class that represents the configuration for a Mac trackpad.
- [class VZUSBScreenCoordinatePointingDeviceConfiguration](vzusbscreencoordinatepointingdeviceconfiguration.md)
  An object that defines the configuration for a USB pointing device that reports absolute coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzpointingdeviceconfiguration)*