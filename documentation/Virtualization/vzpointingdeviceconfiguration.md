# VZPointingDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The base class for a pointing device configuration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZPointingDeviceConfiguration
```

```objc
@interface VZPointingDeviceConfiguration : NSObject
```

#### Overview

Don’t instantiate a `VZPointingDeviceConfiguration` directly, use one of its subclasses like [`VZUSBScreenCoordinatePointingDeviceConfiguration`](./vzusbscreencoordinatepointingdeviceconfiguration.md) instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZMacTrackpadConfiguration](./vzmactrackpadconfiguration.md)
- [VZUSBScreenCoordinatePointingDeviceConfiguration](./vzusbscreencoordinatepointingdeviceconfiguration.md)
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
- [class VZUSBScreenCoordinatePointingDeviceConfiguration](./vzusbscreencoordinatepointingdeviceconfiguration.md)
  An object that defines the configuration for a USB pointing device that reports absolute coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzpointingdeviceconfiguration)*