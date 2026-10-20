# VZVirtioConsoleDeviceDelegate

**Framework**: Virtualization  
**Kind**: protocol  
**Role**: Protocol

Optional methods that you use to respond when a console port opens or closes in the virtual machine.

**Availability**:
- macOS 13.0+

## Declaration

```swift
protocol VZVirtioConsoleDeviceDelegate : NSObjectProtocol
```

```objc
@protocol VZVirtioConsoleDeviceDelegate <NSObject>
```

## Topics

### Responding to console device changes
- [func consoleDevice(VZVirtioConsoleDevice, didOpen: VZVirtioConsolePort)](./vzvirtioconsoledevicedelegate/consoledevice%28_,didopen%29.md)
  Tells the delegate that the framework opened a console port.
- [func consoleDevice(VZVirtioConsoleDevice, didClose: VZVirtioConsolePort)](./vzvirtioconsoledevicedelegate/consoledevice%28_,didclose%29.md)
  Tells the delegate that the framework closed a console port.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZVirtioConsoleDevice](./vzvirtioconsoledevice.md)
  A class that represents a Virtio console device in a virtual machine.
- [class VZVirtioConsolePort](./vzvirtioconsoleport.md)
  A class that represents a Virtio console port in a VM.
### Configuring the console
- [var ports: VZVirtioConsolePortArray](./vzvirtioconsoledevice/ports.md)
  The array of console ports that a specific device uses.
- [var delegate: (any VZVirtioConsoleDeviceDelegate)?](./vzvirtioconsoledevice/delegate.md)
  The delegate object for the console device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoledevicedelegate)*