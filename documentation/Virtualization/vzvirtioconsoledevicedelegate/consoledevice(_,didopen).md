# consoleDevice(_:didOpen:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the framework opened a console port.

**Availability**:
- macOS 13.0+

## Declaration

```swift
optional func consoleDevice(_ consoleDevice: VZVirtioConsoleDevice, didOpen consolePort: VZVirtioConsolePort)
```

```objc
- (void) consoleDevice:(VZVirtioConsoleDevice *) consoleDevice didOpenPort:(VZVirtioConsolePort *) consolePort;
```

#### Discussion

Be sure to process or flush any pending data from the [`VZVirtioConsolePort`](../vzvirtioconsoleport.md) attachment before communicating with a new virtual machine process, or additional data might remain on the serial port from the previous session.

## Parameters

- `consoleDevice`: The console port’s console device.
- `consolePort`: The [`VZVirtioConsolePort`](../vzvirtioconsoleport.md) port that the framework opened.

## See Also

### Responding to console device changes
- [func consoleDevice(VZVirtioConsoleDevice, didClose: VZVirtioConsolePort)](./consoledevice%28_,didclose%29.md)
  Tells the delegate that the framework closed a console port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoledevicedelegate/consoledevice(_:didopen:))*