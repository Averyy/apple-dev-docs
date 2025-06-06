# VZVirtioConsoleDeviceDelegate

**Framework**: Virtualization  
**Kind**: protocol

Optional methods that you use to respond when a console port opens or closes in the virtual machine.

**Availability**:
- macOS 13.0+

## Declaration

```swift
protocol VZVirtioConsoleDeviceDelegate : NSObjectProtocol
```

## Topics

### Responding to console device changes
- [func consoleDevice(VZVirtioConsoleDevice, didOpen: VZVirtioConsolePort)](vzvirtioconsoledevicedelegate/consoledevice(_:didopen:).md)
  Tells the delegate that the framework opened a console port.
- [func consoleDevice(VZVirtioConsoleDevice, didClose: VZVirtioConsolePort)](vzvirtioconsoledevicedelegate/consoledevice(_:didclose:).md)
  Tells the delegate that the framework closed a console port.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtioConsoleDevice](vzvirtioconsoledevice.md)
  A class that represents a Virtio console device in a virtual machine.
- [class VZVirtioConsolePort](vzvirtioconsoleport.md)
  A class that represents a Virtio console port in a VM.
- [var ports: VZVirtioConsolePortArray](vzvirtioconsoledevice/ports.md)
  The array of console ports that a specific device uses.
- [var delegate: (any VZVirtioConsoleDeviceDelegate)?](vzvirtioconsoledevice/delegate.md)
  The delegate object for the console device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoledevicedelegate)*