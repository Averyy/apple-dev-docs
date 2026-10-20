# VZMacGraphicsDevice

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

An object that represents a Mac graphics device.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class VZMacGraphicsDevice
```

```objc
@interface VZMacGraphicsDevice : VZGraphicsDevice
```

#### Overview

You don’t instantiate a `VZMacGraphicsDevice` directly. Graphics devices are first configured on the [`VZVirtualMachineConfiguration`](./vzvirtualmachineconfiguration.md) through a subclass of [`VZMacGraphicsDeviceConfiguration`](./vzmacgraphicsdeviceconfiguration.md).  When the framework creates a VZVirtualMachine from the configuration, the graphics devices are available through the `graphicsDevices` property.

## Relationships

### Inherits From
- [VZGraphicsDevice](./vzgraphicsdevice.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZMacGraphicsDeviceConfiguration](./vzmacgraphicsdeviceconfiguration.md)
  Configuration for a display attached to a Mac graphics device.
### Devices
- [class VZGraphicsDevice](./vzgraphicsdevice.md)
  A class that represents a graphics device in a VM.
- [class VZGraphicsDisplay](./vzgraphicsdisplay.md)
  A class that represents a graphics display in a VM.
- [class VZVirtioGraphicsScanout](./vzvirtiographicsscanout.md)
  A Virtio graphics scanout that corresponds to a Virtio graphics scanout configuration.
- [class VZMacGraphicsDisplay](./vzmacgraphicsdisplay.md)
  An object that represents the graphics display on a Mac.
- [class VZVirtioGraphicsDevice](./vzvirtiographicsdevice.md)
  A Virtio graphics device.
- [struct VZVirtualMachineViewAdaptor](./vzvirtualmachineviewadaptor.md)
  A sendable wrapper that connects a virtual machine view to a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacgraphicsdevice)*