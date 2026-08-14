# VZMacGraphicsDisplayConfiguration

**Framework**: Virtualization  
**Kind**: class

The configuration for a Mac graphics device.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZMacGraphicsDisplayConfiguration
```

#### Overview

Use this device to attach a display that’s shown in a [`VZVirtualMachineView`](vzvirtualmachineview.md).

## Topics

### Creating the display configuration
- [convenience init(for: NSScreen, sizeInPoints: NSSize)](vzmacgraphicsdisplayconfiguration/init(for:sizeinpoints:).md)
  Create a display configuration suitable for showing on the specified screen.
- [init(widthInPixels: Int, heightInPixels: Int, pixelsPerInch: Int)](vzmacgraphicsdisplayconfiguration/init(widthinpixels:heightinpixels:pixelsperinch:).md)
  Create a display configuration with the specified pixel dimensions and pixel density.
### Configuring the display properties
- [var heightInPixels: Int](vzmacgraphicsdisplayconfiguration/heightinpixels.md)
  The height of the display, in pixels.
- [var widthInPixels: Int](vzmacgraphicsdisplayconfiguration/widthinpixels.md)
  The width of the display, in pixels.
- [var pixelsPerInch: Int](vzmacgraphicsdisplayconfiguration/pixelsperinch.md)
  The pixel density in pixels per inch.
### Initializers
- [convenience init(forScreen: NSScreen, sizeInPoints: NSSize)](vzmacgraphicsdisplayconfiguration/init(forscreen:sizeinpoints:).md)

## Relationships

### Inherits From
- [VZGraphicsDisplayConfiguration](vzgraphicsdisplayconfiguration.md)
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
- [class VZMacGraphicsDeviceConfiguration](vzmacgraphicsdeviceconfiguration.md)
  Configuration for a display attached to a Mac graphics device.
- [class VZGraphicsDeviceConfiguration](vzgraphicsdeviceconfiguration.md)
  The base class for a graphics device configuration.
- [class VZVirtioGraphicsDeviceConfiguration](vzvirtiographicsdeviceconfiguration.md)
  Configuration that represents the configuration of a Virtio graphics device for a Linux VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacgraphicsdisplayconfiguration)*