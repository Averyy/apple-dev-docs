# directorySharingDevices

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The list of configured directory-sharing devices on the VM.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var directorySharingDevices: [VZDirectorySharingDevice] { get }
```

```objc
@property (copy, readonly) NSArray<VZDirectorySharingDevice *> * directorySharingDevices;
```

#### Discussion

Returns an empty array if there are no directory sharing devices associated with this virtual machine.

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
- [var usbControllers: [VZUSBController]](./usbcontrollers.md)
  The list of runtime USB controller objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/directorysharingdevices)*