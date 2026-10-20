# delegate

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The delegate object for the console device.

**Availability**:
- macOS 13.0+

## Declaration

```swift
weak var delegate: (any VZVirtioConsoleDeviceDelegate)? { get set }
```

```objc
@property (weak, nullable) id<VZVirtioConsoleDeviceDelegate> delegate;
```

## See Also

### Configuring the console
- [var ports: VZVirtioConsolePortArray](./ports.md)
  The array of console ports that a specific device uses.
- [protocol VZVirtioConsoleDeviceDelegate](../vzvirtioconsoledevicedelegate.md)
  Optional methods that you use to respond when a console port opens or closes in the virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoledevice/delegate)*