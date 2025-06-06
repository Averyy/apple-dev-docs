# consoleDevice(_:didClose:)

**Framework**: Virtualization  
**Kind**: method

Tells the delegate that the framework closed a console port.

**Availability**:
- macOS 13.0+

## Declaration

```swift
optional func consoleDevice(_ consoleDevice: VZVirtioConsoleDevice, didClose consolePort: VZVirtioConsolePort)
```

#### Discussion

Be sure to finish processing or flushing any remaining data from the [`VZVirtioConsolePort`](vzvirtioconsoleport.md) attachment after closing a port, or the additional data might remain on the serial port.

## Parameters

- `consoleDevice`: The console port’s console device.
- `consolePort`: The   port that the framework closed.

## See Also

- [func consoleDevice(VZVirtioConsoleDevice, didOpen: VZVirtioConsolePort)](vzvirtioconsoledevicedelegate/consoledevice(_:didopen:).md)
  Tells the delegate that the framework opened a console port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoledevicedelegate/consoledevice(_:didclose:))*