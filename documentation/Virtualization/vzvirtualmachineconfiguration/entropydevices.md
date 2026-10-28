# entropyDevices

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The array of randomization devices that you expose to the guest operating system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var entropyDevices: [VZEntropyDeviceConfiguration] { get set }
```

```objc
@property (copy, readwrite) NSArray<VZEntropyDeviceConfiguration *> * entropyDevices;
```

## Discussion

The default value of this property is an empty array. Add one or more entropy configuration objects if you want to provide the guest operating system with a source of entropy for its random number generator.

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
- [var graphicsDevices: [VZGraphicsDeviceConfiguration]](./graphicsdevices.md)
  The list of graphics devices.
- [var keyboards: [VZKeyboardConfiguration]](./keyboards.md)
  The list of keyboards.
- [var networkDevices: [VZNetworkDeviceConfiguration]](./networkdevices.md)
  The array of network devices that you expose to the guest operating system.
- [var platform: VZPlatformConfiguration](./platform.md)
  The hardware platform to use.
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

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/entropydevices)*