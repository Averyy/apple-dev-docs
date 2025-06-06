# VZVirtioConsoleDevice

**Framework**: Virtualization  
**Kind**: class

A class that represents a Virtio console device in a virtual machine.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZVirtioConsoleDevice
```

## Topics

### Configuring the console
- [var ports: VZVirtioConsolePortArray](vzvirtioconsoledevice/ports.md)
  The array of console ports that a specific device uses.
- [var delegate: (any VZVirtioConsoleDeviceDelegate)?](vzvirtioconsoledevice/delegate.md)
  The delegate object for the console device.
- [protocol VZVirtioConsoleDeviceDelegate](vzvirtioconsoledevicedelegate.md)
  Optional methods that you use to respond when a console port opens or closes in the virtual machine.

## Relationships

### Inherits From
- [VZConsoleDevice](vzconsoledevice.md)
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
- [class VZConsoleDevice](vzconsoledevice.md)
  A class that represents a console device in a VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoledevice)*