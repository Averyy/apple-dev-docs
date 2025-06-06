# VZConsoleDevice

**Framework**: Virtualization  
**Kind**: class

A class that represents a console device in a VM.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZConsoleDevice
```

#### Overview

Don’t instantiate a `VZConsoleDevice` directly: You first configure console devices on the [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) through a subclass of [`VZConsoleDeviceConfiguration`](vzconsoledeviceconfiguration.md). After you create [`VZVirtualMachine`](vzvirtualmachine.md) from the configuration, the console devices are available through the [`consoleDevices`](vzvirtualmachine/consoledevices.md) property.

The actual type of `VZConsoleDevice` corresponds to the type that the configuration uses. For example, a [`VZVirtioConsoleDeviceConfiguration`](vzvirtioconsoledeviceconfiguration.md) is a device of type [`VZVirtioConsoleDevice`](vzvirtioconsoledevice.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZVirtioConsoleDevice](vzvirtioconsoledevice.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZConsoleDeviceConfiguration](vzconsoledeviceconfiguration.md)
  The base class for a console device configuration.
- [class VZVirtioConsoleDevice](vzvirtioconsoledevice.md)
  A class that represents a Virtio console device in a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzconsoledevice)*