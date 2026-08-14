# VZMacGraphicsDevice

**Framework**: Virtualization  
**Kind**: class

An object that represents a Mac graphics device.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class VZMacGraphicsDevice
```

#### Overview

You don’t instantiate a `VZMacGraphicsDevice` directly. Graphics devices are first configured on the [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) through a subclass of [`VZMacGraphicsDeviceConfiguration`](vzmacgraphicsdeviceconfiguration.md).  When the framework creates a VZVirtualMachine from the configuration, the graphics devices are available through the `graphicsDevices` property.

## Relationships

### Inherits From
- [VZGraphicsDevice](vzgraphicsdevice.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZMacGraphicsDeviceConfiguration](vzmacgraphicsdeviceconfiguration.md)
  Configuration for a display attached to a Mac graphics device.
- [class VZGraphicsDevice](vzgraphicsdevice.md)
  A class that represents a graphics device in a VM.
- [class VZGraphicsDisplay](vzgraphicsdisplay.md)
  A class that represents a graphics display in a VM.
- [class VZVirtioGraphicsScanout](vzvirtiographicsscanout.md)
  A Virtio graphics scanout that corresponds to a Virtio graphics scanout configuration.
- [class VZMacGraphicsDisplay](vzmacgraphicsdisplay.md)
  An object that represents the graphics display on a Mac.
- [class VZVirtioGraphicsDevice](vzvirtiographicsdevice.md)
  A Virtio graphics device.
- [struct VZVirtualMachineViewAdaptor](vzvirtualmachineviewadaptor.md)
  A sendable wrapper that connects a virtual machine view to a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacgraphicsdevice)*