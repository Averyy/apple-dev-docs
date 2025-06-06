# VZVirtioConsolePortConfiguration

**Framework**: Virtualization  
**Kind**: class

A class that represents the configuration options you can set on a Virtio console port.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZVirtioConsolePortConfiguration
```

#### Overview

A console port is a two-way communication channel between a host [`VZSerialPortAttachment`](vzserialportattachment.md) and a VM console port. A Virtio device can have one or more attached console devices. Optionally, you can set a name for a console port and also configure a console port that the guest can use as the system console.

## Topics

### Creating a port configuration
- [init()](vzvirtioconsoleportconfiguration/init.md)
  Creates a new Virtio console port configuration.
### Configuring the port
- [var isConsole: Bool](vzvirtioconsoleportconfiguration/isconsole.md)
  A Boolean value that indicates whether this port is a console.
- [var name: String?](vzvirtioconsoleportconfiguration/name.md)
  The name of the port.

## Relationships

### Inherits From
- [VZConsolePortConfiguration](vzconsoleportconfiguration.md)
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
- [class VZVirtioConsoleDeviceConfiguration](vzvirtioconsoledeviceconfiguration.md)
  A console device that enables communication between the host and the guest using console ports through a Virtio interface.
- [class VZVirtioConsolePortConfigurationArray](vzvirtioconsoleportconfigurationarray.md)
  A class that represents a collection of Virtio console port configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoleportconfiguration)*