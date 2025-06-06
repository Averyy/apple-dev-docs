# usbControllers

**Framework**: Virtualization  
**Kind**: property

The list of runtime USB controller objects.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var usbControllers: [VZUSBController] { get }
```

#### Discussion

Return an empty array if there isn’t a configured controller USB.

## See Also

- [var consoleDevices: [VZConsoleDevice]](vzvirtualmachine/consoledevices.md)
  The list of configured console devices on the VM.
- [var memoryBalloonDevices: [VZMemoryBalloonDevice]](vzvirtualmachine/memoryballoondevices.md)
  The array of devices that you use to adjust the amount of memory available to the guest system.
- [var networkDevices: [VZNetworkDevice]](vzvirtualmachine/networkdevices.md)
  The list of configured network devices on the VM.
- [var socketDevices: [VZSocketDevice]](vzvirtualmachine/socketdevices.md)
  The array of socket devices that the VM configures for use ports in the guest VM.
- [var directorySharingDevices: [VZDirectorySharingDevice]](vzvirtualmachine/directorysharingdevices.md)
  The list of configured directory-sharing devices on the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/usbcontrollers)*