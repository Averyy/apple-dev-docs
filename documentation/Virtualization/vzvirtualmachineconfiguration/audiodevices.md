# audioDevices

**Framework**: Virtualization  
**Kind**: property

The list of audio devices.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var audioDevices: [VZAudioDeviceConfiguration] { get set }
```

#### Discussion

The default value of this property is an empty array. If your VM exposes one or more audio devices, assign an array of [`VZAudioDeviceConfiguration`](vzaudiodeviceconfiguration.md) objects to this property.

## See Also

- [var consoleDevices: [VZConsoleDeviceConfiguration]](vzvirtualmachineconfiguration/consoledevices.md)
  The array of console devices that you expose to the guest operating system.
- [var networkDevices: [VZNetworkDeviceConfiguration]](vzvirtualmachineconfiguration/networkdevices.md)
  The array of network devices that you expose to the guest operating system.
- [var socketDevices: [VZSocketDeviceConfiguration]](vzvirtualmachineconfiguration/socketdevices.md)
  The socket device that you use to implement port-based communication with the guest operating system.
- [var serialPorts: [VZSerialPortConfiguration]](vzvirtualmachineconfiguration/serialports.md)
  The array of serial ports that you expose to the guest operating system.
- [var storageDevices: [VZStorageDeviceConfiguration]](vzvirtualmachineconfiguration/storagedevices.md)
  The array of storage devices that you expose to the guest operating system.
- [var entropyDevices: [VZEntropyDeviceConfiguration]](vzvirtualmachineconfiguration/entropydevices.md)
  The array of randomization devices that you expose to the guest operating system.
- [var directorySharingDevices: [VZDirectorySharingDeviceConfiguration]](vzvirtualmachineconfiguration/directorysharingdevices.md)
  The list of directory sharing devices.
- [var graphicsDevices: [VZGraphicsDeviceConfiguration]](vzvirtualmachineconfiguration/graphicsdevices.md)
  The list of graphics devices.
- [var keyboards: [VZKeyboardConfiguration]](vzvirtualmachineconfiguration/keyboards.md)
  The list of keyboards.
- [var platform: VZPlatformConfiguration](vzvirtualmachineconfiguration/platform.md)
  The hardware platform to use.
- [var pointingDevices: [VZPointingDeviceConfiguration]](vzvirtualmachineconfiguration/pointingdevices.md)
  The list of pointing devices.
- [var usbControllers: [VZUSBControllerConfiguration]](vzvirtualmachineconfiguration/usbcontrollers.md)
  The list of configured USB controllers for the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/audiodevices)*