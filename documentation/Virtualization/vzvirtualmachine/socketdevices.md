# socketDevices

**Framework**: Virtualization  
**Kind**: property

The array of socket devices that the VM configures for use ports in the guest VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var socketDevices: [VZSocketDevice] { get }
```

#### Discussion

If you included a [`VZVirtioSocketDeviceConfiguration`](vzvirtiosocketdeviceconfiguration.md) object in the configuration of your VM, this property contains a corresponding [`VZVirtioSocketDevice`](vzvirtiosocketdevice.md) object. Use that object to configure the ports your VM makes available to the guest operating system.

If you didn’t include a socket device in your configuration, this property contains an empty array.

## See Also

- [var consoleDevices: [VZConsoleDevice]](vzvirtualmachine/consoledevices.md)
  The list of configured console devices on the VM.
- [var memoryBalloonDevices: [VZMemoryBalloonDevice]](vzvirtualmachine/memoryballoondevices.md)
  The array of devices that you use to adjust the amount of memory available to the guest system.
- [var networkDevices: [VZNetworkDevice]](vzvirtualmachine/networkdevices.md)
  The list of configured network devices on the VM.
- [var directorySharingDevices: [VZDirectorySharingDevice]](vzvirtualmachine/directorysharingdevices.md)
  The list of configured directory-sharing devices on the VM.
- [var usbControllers: [VZUSBController]](vzvirtualmachine/usbcontrollers.md)
  The list of runtime USB controller objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/socketdevices)*