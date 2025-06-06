# VZVirtioGraphicsScanoutConfiguration

**Framework**: Virtualization  
**Kind**: class

The configuration for a Virtio graphics device that configures the dimensions of the graphics device for a Linux VM.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZVirtioGraphicsScanoutConfiguration
```

#### Overview

Use a `VZVirtioGraphicsScanoutConfiguration` to configure the width and height of a Virtio graphics device.

## Topics

### Creating the configuration object
- [init(widthInPixels: Int, heightInPixels: Int)](vzvirtiographicsscanoutconfiguration/init(widthinpixels:heightinpixels:).md)
  Creates a Virtio graphics device with the specified dimensions.
### Instance properties
- [var heightInPixels: Int](vzvirtiographicsscanoutconfiguration/heightinpixels.md)
  An integer value that describes the height of the graphics device in pixels.
- [var widthInPixels: Int](vzvirtiographicsscanoutconfiguration/widthinpixels.md)
  An integer value that describes the width of the graphics device in pixels.

## Relationships

### Inherits From
- [VZGraphicsDisplayConfiguration](vzgraphicsdisplayconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var scanouts: [VZVirtioGraphicsScanoutConfiguration]](vzvirtiographicsdeviceconfiguration/scanouts.md)
  The array of output devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiographicsscanoutconfiguration)*