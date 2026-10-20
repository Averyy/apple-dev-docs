# usbControllers

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The list of runtime USB controller objects.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var usbControllers: [VZUSBController] { get }
```

```objc
@property (copy, readonly) NSArray<VZUSBController *> * usbControllers;
```

#### Discussion

Return an empty array if there isn’t a configured controller USB.

## See Also

### Configuring VM attributes at runtime
- [var consoleDevices: [VZConsoleDevice]](./consoledevices.md)
  The list of configured console devices on the VM.
- [var memoryBalloonDevices: [VZMemoryBalloonDevice]](./memoryballoondevices.md)
  The array of devices that you use to adjust the amount of memory available to the guest system.
- [var networkDevices: [VZNetworkDevice]](./networkdevices.md)
  The list of configured network devices on the VM.
- [var socketDevices: [VZSocketDevice]](./socketdevices.md)
  The array of socket devices that the VM configures for use ports in the guest VM.
- [var directorySharingDevices: [VZDirectorySharingDevice]](./directorysharingdevices.md)
  The list of configured directory-sharing devices on the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/usbcontrollers)*