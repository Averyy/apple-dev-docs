# networkDevices

**Framework**: Virtualization  
**Kind**: property

The list of configured network devices on the VM.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var networkDevices: [VZNetworkDevice] { get }
```

#### Discussion

Returns an empty array if there are no configured network devices.

## See Also

- [var consoleDevices: [VZConsoleDevice]](vzvirtualmachine/consoledevices.md)
  The list of configured console devices on the VM.
- [var memoryBalloonDevices: [VZMemoryBalloonDevice]](vzvirtualmachine/memoryballoondevices.md)
  The array of devices that you use to adjust the amount of memory available to the guest system.
- [var socketDevices: [VZSocketDevice]](vzvirtualmachine/socketdevices.md)
  The array of socket devices that the VM configures for use ports in the guest VM.
- [var directorySharingDevices: [VZDirectorySharingDevice]](vzvirtualmachine/directorysharingdevices.md)
  The list of configured directory-sharing devices on the VM.
- [var usbControllers: [VZUSBController]](vzvirtualmachine/usbcontrollers.md)
  The list of runtime USB controller objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/networkdevices)*