# VZVirtioGraphicsScanoutConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The configuration for a Virtio graphics device that configures the dimensions of the graphics device for a Linux VM.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZVirtioGraphicsScanoutConfiguration
```

```objc
@interface VZVirtioGraphicsScanoutConfiguration : VZGraphicsDisplayConfiguration
```

#### Overview

Use a `VZVirtioGraphicsScanoutConfiguration` to configure the width and height of a Virtio graphics device.

## Topics

### Creating the configuration object
- [init(widthInPixels: Int, heightInPixels: Int)](./vzvirtiographicsscanoutconfiguration/init%28widthinpixels,heightinpixels%29.md)
  Creates a Virtio graphics device with the specified dimensions.
### Instance properties
- [var heightInPixels: Int](./vzvirtiographicsscanoutconfiguration/heightinpixels.md)
  An integer value that describes the height of the graphics device in pixels.
- [var widthInPixels: Int](./vzvirtiographicsscanoutconfiguration/widthinpixels.md)
  An integer value that describes the width of the graphics device in pixels.

## Relationships

### Inherits From
- [VZGraphicsDisplayConfiguration](./vzgraphicsdisplayconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Instance properties
- [var scanouts: [VZVirtioGraphicsScanoutConfiguration]](./vzvirtiographicsdeviceconfiguration/scanouts.md)
  The array of output devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiographicsscanoutconfiguration)*