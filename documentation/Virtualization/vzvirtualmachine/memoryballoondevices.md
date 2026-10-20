# memoryBalloonDevices

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The array of devices that you use to adjust the amount of memory available to the guest system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var memoryBalloonDevices: [VZMemoryBalloonDevice] { get }
```

```objc
@property (copy, readonly) NSArray<VZMemoryBalloonDevice *> * memoryBalloonDevices;
```

#### Discussion

If you included a [`VZVirtioTraditionalMemoryBalloonDeviceConfiguration`](../vzvirtiotraditionalmemoryballoondeviceconfiguration.md) object in the configuration of your VM, this property contains a corresponding [`VZVirtioTraditionalMemoryBalloonDevice`](../vzvirtiotraditionalmemoryballoondevice.md) object. Use that object to adjust the amount of memory available to the guest operating system.

If you didn’t include a memory balloon object in your configuration, this property contains an empty array.

## See Also

### Configuring VM attributes at runtime
- [var consoleDevices: [VZConsoleDevice]](./consoledevices.md)
  The list of configured console devices on the VM.
- [var networkDevices: [VZNetworkDevice]](./networkdevices.md)
  The list of configured network devices on the VM.
- [var socketDevices: [VZSocketDevice]](./socketdevices.md)
  The array of socket devices that the VM configures for use ports in the guest VM.
- [var directorySharingDevices: [VZDirectorySharingDevice]](./directorysharingdevices.md)
  The list of configured directory-sharing devices on the VM.
- [var usbControllers: [VZUSBController]](./usbcontrollers.md)
  The list of runtime USB controller objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/memoryballoondevices)*