# usbControllers

**Framework**: Virtualization  
**Kind**: property

The list of configured USB controllers for the VM.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var usbControllers: [VZUSBControllerConfiguration] { get set }
```

#### Discussion

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

- [class VZUSBControllerConfiguration](vzusbcontrollerconfiguration.md)
  The base class for a USB controller configuration.
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
- [var audioDevices: [VZAudioDeviceConfiguration]](vzvirtualmachineconfiguration/audiodevices.md)
  The list of audio devices.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/usbcontrollers)*