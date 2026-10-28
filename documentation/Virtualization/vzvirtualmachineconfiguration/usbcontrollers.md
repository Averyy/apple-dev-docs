# usbControllers

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The list of configured USB controllers for the VM.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var usbControllers: [VZUSBControllerConfiguration] { get set }
```

```objc
@property (copy, readwrite) NSArray<VZUSBControllerConfiguration *> * usbControllers;
```

## Discussion

Use this property to attach USB controllers to the VM configuration, as in the following example:

```swift
// Configure and start the virtual machine.
let usbControllerConfiguration = VZXHCIControllerConfiguration()

let vmConfiguration = VZVirtualMachineConfiguration()
vmConfiguration.usbControllers = [usbControllerConfiguration]

let virtualMachine = VZVirtualMachine(configuration: vmConfiguration)
try await virtualMachine.start()
```

This property contains an empty array if the `VZVirtualMachineConfiguration` doesn’t have any configured USB controllers.

## See Also

### Related Documentation
- [class VZUSBControllerConfiguration](../vzusbcontrollerconfiguration.md)
  The base class for a USB controller configuration.
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
- [var customVirtioDevices: [VZCustomVirtioDeviceConfiguration]](./customvirtiodevices.md)
  The array of custom virtio devices that you expose to the guest operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/usbcontrollers)*