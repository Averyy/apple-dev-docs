# VZVirtioConsoleDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

A console device that enables communication between the host and the guest using console ports through a Virtio interface.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZVirtioConsoleDeviceConfiguration
```

#### Overview

A [`VZVirtioConsoleDeviceConfiguration`](vzvirtioconsoledeviceconfiguration.md) object enables serial communication between the guest-operating system and host computer through the Virtio interface. The device sets up one or more ports through [`VZVirtioConsolePortConfiguration`](vzvirtioconsoleportconfiguration.md) on the Virtio console device.

## Topics

### Creating the configuration object
- [init()](vzvirtioconsoledeviceconfiguration/init.md)
  Creates a console port configuration object.
### Configuring the console ports
- [var ports: VZVirtioConsolePortConfigurationArray](vzvirtioconsoledeviceconfiguration/ports.md)
  The list of Virtio port configurations.

## Relationships

### Inherits From
- [VZConsoleDeviceConfiguration](vzconsoledeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var consoleDevices: [VZConsoleDeviceConfiguration]](vzvirtualmachineconfiguration/consoledevices.md)
  The array of console devices that you expose to the guest operating system.
- [class VZConsoleDeviceConfiguration](vzconsoledeviceconfiguration.md)
  The base class for a console device configuration.
- [class VZConsolePortConfiguration](vzconsoleportconfiguration.md)
  The base class for a console port configuration.
- [class VZVirtioConsolePortConfiguration](vzvirtioconsoleportconfiguration.md)
  A class that represents the configuration options you can set on a Virtio console port.
- [class VZVirtioConsolePortConfigurationArray](vzvirtioconsoleportconfigurationarray.md)
  A class that represents a collection of Virtio console port configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoledeviceconfiguration)*