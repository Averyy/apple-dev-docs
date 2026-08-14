# VZGraphicsDevice

**Framework**: Virtualization  
**Kind**: class

A class that represents a graphics device in a VM.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class VZGraphicsDevice
```

#### Overview

You don’t instantiate a `VZGraphicsDevice` directly. Graphics devices are first configured on the [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) through a subclass of [`VZGraphicsDeviceConfiguration`](vzgraphicsdeviceconfiguration.md).

When the framework creates a [`VZVirtualMachine`](vzvirtualmachine.md) from the configuration, the graphics devices are available through the [`graphicsDevices`](vzvirtualmachine/graphicsdevices.md) property.

The real type of [`VZGraphicsDevice`](vzgraphicsdevice.md) corresponds to the type used by the configuration.

For example, a [`VZVirtioGraphicsDeviceConfiguration`](vzvirtiographicsdeviceconfiguration.md) leads to a device of type [`VZVirtioGraphicsDevice`](vzvirtiographicsdevice.md) and a [`VZMacGraphicsDeviceConfiguration`](vzmacgraphicsdeviceconfiguration.md) leads to a device of type [`VZMacGraphicsDevice`](vzmacgraphicsdevice.md).

## Topics

### Getting the device’s displays
- [var displays: [VZGraphicsDisplay]](vzgraphicsdevice/displays.md)
  The list of graphics displays configured for this graphics device.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [VZMacGraphicsDevice](vzmacgraphicsdevice.md)
- [VZVirtioGraphicsDevice](vzvirtiographicsdevice.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZGraphicsDeviceConfiguration](vzgraphicsdeviceconfiguration.md)
  The base class for a graphics device configuration.
- [class VZMacGraphicsDeviceConfiguration](vzmacgraphicsdeviceconfiguration.md)
  Configuration for a display attached to a Mac graphics device.
- [class VZGraphicsDisplay](vzgraphicsdisplay.md)
  A class that represents a graphics display in a VM.
- [class VZMacGraphicsDevice](vzmacgraphicsdevice.md)
  An object that represents a Mac graphics device.
- [class VZVirtioGraphicsScanout](vzvirtiographicsscanout.md)
  A Virtio graphics scanout that corresponds to a Virtio graphics scanout configuration.
- [class VZMacGraphicsDisplay](vzmacgraphicsdisplay.md)
  An object that represents the graphics display on a Mac.
- [class VZVirtioGraphicsDevice](vzvirtiographicsdevice.md)
  A Virtio graphics device.
- [struct VZVirtualMachineViewAdaptor](vzvirtualmachineviewadaptor.md)
  A sendable wrapper that connects a virtual machine view to a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdevice)*