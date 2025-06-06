# VZGraphicsDisplay

**Framework**: Virtualization  
**Kind**: class

A class that represents a graphics display in a VM.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class VZGraphicsDisplay
```

#### Overview

Don’t instantiate a `VZGraphicsDisplay` directly. Graphics displays are first configured on a [`VZGraphicsDeviceConfiguration`](vzgraphicsdeviceconfiguration.md) subclass. When you create a [`VZVirtualMachine`](vzvirtualmachine.md) from the configuration, the displays are available through the [`displays`](vzgraphicsdevice/displays.md) property of the configuration’s [`VZGraphicsDevice`](vzgraphicsdevice.md).

## Topics

### Getting the display size
- [var sizeInPixels: CGSize](vzgraphicsdisplay/sizeinpixels.md)
  Returns the size of the display, in pixels.
### Observing changes to the display configuration
- [func addObserver(any VZGraphicsDisplayObserver)](vzgraphicsdisplay/addobserver(_:).md)
  Adds an observer to notify about display configuration changes.
- [func removeObserver(any VZGraphicsDisplayObserver)](vzgraphicsdisplay/removeobserver(_:).md)
  Removes a display configuration change observer.
- [protocol VZGraphicsDisplayObserver](vzgraphicsdisplayobserver.md)
  A protocol you implement to observe state changes in graphic displays.
### Changing the display configuration
- [func reconfigure(sizeInPixels: CGSize) throws](vzgraphicsdisplay/reconfigure(sizeinpixels:).md)
  Resize this display with the new dimensions you provide.
- [func reconfigure(configuration: VZGraphicsDisplayConfiguration) throws](vzgraphicsdisplay/reconfigure(configuration:).md)
  Reconfigure this display with the new display configuration you provide.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZMacGraphicsDisplay](vzmacgraphicsdisplay.md)
- [VZVirtioGraphicsScanout](vzvirtiographicsscanout.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZMacGraphicsDisplayConfiguration](vzmacgraphicsdisplayconfiguration.md)
  The configuration for a Mac graphics device.
- [class VZVirtioGraphicsScanoutConfiguration](vzvirtiographicsscanoutconfiguration.md)
  The configuration for a Virtio graphics device that configures the dimensions of the graphics device for a Linux VM.
- [class VZGraphicsDevice](vzgraphicsdevice.md)
  A class that represents a graphics device in a VM.
- [class VZMacGraphicsDevice](vzmacgraphicsdevice.md)
  An object that represents a Mac graphics device.
- [class VZVirtioGraphicsScanout](vzvirtiographicsscanout.md)
  A Virtio graphics scanout that corresponds to a Virtio graphics scanout configuration.
- [class VZMacGraphicsDisplay](vzmacgraphicsdisplay.md)
  An object that represents the graphics display on a Mac.
- [class VZVirtioGraphicsDevice](vzvirtiographicsdevice.md)
  A Virtio graphics device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdisplay)*