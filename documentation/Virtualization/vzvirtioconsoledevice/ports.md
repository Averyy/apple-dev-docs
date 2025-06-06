# ports

**Framework**: Virtualization  
**Kind**: property

The array of console ports that a specific device uses.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var ports: VZVirtioConsolePortArray { get }
```

## See Also

- [var delegate: (any VZVirtioConsoleDeviceDelegate)?](vzvirtioconsoledevice/delegate.md)
  The delegate object for the console device.
- [protocol VZVirtioConsoleDeviceDelegate](vzvirtioconsoledevicedelegate.md)
  Optional methods that you use to respond when a console port opens or closes in the virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoledevice/ports)*