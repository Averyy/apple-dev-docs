# consoleDevice(_:didOpen:)

**Framework**: Virtualization  
**Kind**: method

Tells the delegate that the framework opened a console port.

**Availability**:
- macOS 13.0+

## Declaration

```swift
optional func consoleDevice(_ consoleDevice: VZVirtioConsoleDevice, didOpen consolePort: VZVirtioConsolePort)
```

#### Discussion

Be sure to process or flush any pending data from the [`VZVirtioConsolePort`](vzvirtioconsoleport.md) attachment before communicating with a new virtual machine process, or additional data might remain on the serial port from the previous session.

## Parameters

- `consoleDevice`: The console port’s console device.
- `consolePort`: The   port that the framework opened.

## See Also

- [func consoleDevice(VZVirtioConsoleDevice, didClose: VZVirtioConsolePort)](vzvirtioconsoledevicedelegate/consoledevice(_:didclose:).md)
  Tells the delegate that the framework closed a console port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoledevicedelegate/consoledevice(_:didopen:))*