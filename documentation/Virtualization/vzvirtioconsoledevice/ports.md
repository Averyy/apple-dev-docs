# ports

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The array of console ports that a specific device uses.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var ports: VZVirtioConsolePortArray { get }
```

```objc
@property (strong, readonly) VZVirtioConsolePortArray * ports;
```

## See Also

### Configuring the console
- [var delegate: (any VZVirtioConsoleDeviceDelegate)?](./delegate.md)
  The delegate object for the console device.
- [protocol VZVirtioConsoleDeviceDelegate](../vzvirtioconsoledevicedelegate.md)
  Optional methods that you use to respond when a console port opens or closes in the virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoledevice/ports)*