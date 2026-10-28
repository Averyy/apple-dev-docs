# platform

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The hardware platform to use.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var platform: VZPlatformConfiguration { get set }
```

```objc
@property (strong) VZPlatformConfiguration * platform;
```

## Discussion

This can be an instance of either [`VZGenericPlatformConfiguration`](../vzgenericplatformconfiguration.md) or [`VZMacPlatformConfiguration`](../vzmacplatformconfiguration.md). The default is `VZGenericPlatformConfiguration`.

## See Also

### Adding devices to the VM
- [var audioDevices: [VZAudioDeviceConfiguration]](./audiodevices.md)
  The list of audio devices.
- [var consoleDevices: [VZConsoleDeviceConfiguration]](./consoledevices.md)
  The array of console devices that you expose to the guest operating system.
- [var customVirtioDevices: [VZCustomVirtioDeviceConfiguration]](./customvirtiodevices.md)
  The array of custom virtio devices that you expose to the guest operating system.
- [var directorySharingDevices: [VZDirectorySharingDeviceConfiguration]](./directorysharingdevices.md)
  The list of directory sharing devices.
- [var entropyDevices: [VZEntropyDeviceConfiguration]](./entropydevices.md)
  The array of randomization devices that you expose to the guest operating system.
- [var graphicsDevices: [VZGraphicsDeviceConfiguration]](./graphicsdevices.md)
  The list of graphics devices.
- [var keyboards: [VZKeyboardConfiguration]](./keyboards.md)
  The list of keyboards.
- [var networkDevices: [VZNetworkDeviceConfiguration]](./networkdevices.md)
  The array of network devices that you expose to the guest operating system.
- [var pointingDevices: [VZPointingDeviceConfiguration]](./pointingdevices.md)
  The list of pointing devices.
- [var serialPorts: [VZSerialPortConfiguration]](./serialports.md)
  The array of serial ports that you expose to the guest operating system.
- [var socketDevices: [VZSocketDeviceConfiguration]](./socketdevices.md)
  The socket device that you use to implement port-based communication with the guest operating system.
- [var storageDevices: [VZStorageDeviceConfiguration]](./storagedevices.md)
  The array of storage devices that you expose to the guest operating system.
- [var usbControllers: [VZUSBControllerConfiguration]](./usbcontrollers.md)
  The list of configured USB controllers for the VM.
- [var customVirtioDevices: [VZCustomVirtioDeviceConfiguration]](./customvirtiodevices.md)
  The array of custom virtio devices that you expose to the guest operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/platform)*