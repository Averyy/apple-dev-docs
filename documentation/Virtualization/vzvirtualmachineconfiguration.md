# VZVirtualMachineConfiguration

**Framework**: Virtualization  
**Kind**: class

The environment attributes and list of devices to use during the configuration of macOS or Linux VMs.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZVirtualMachineConfiguration
```

## Mentions

- [Creating and Running a Linux Virtual Machine](creating-and-running-a-linux-virtual-machine.md)
- [Installing macOS on a Virtual Machine](installing-macos-on-a-virtual-machine.md)

#### Overview

Use a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) object to configure the environment for a macOS or Linux VM. This configuration object contains information about the VM environment, including the devices that the VM exposes to the guest operating system. For example, use the configuration object to specify the network interfaces and storage devices that the operating system may access. For more information on the devices that macOS and Linux guests can support, see the Devices section on the [`Virtualization`](Virtualization.md) framework page.

You create and configure [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) objects directly. After validating the configuration object, use it to initialize the [`VZVirtualMachine`](vzvirtualmachine.md) object that manages the virtual environment. The smallest valid configuration includes a value for the [`bootLoader`](vzvirtualmachineconfiguration/bootloader.md) property; you can also include more devices in the configuration depending on the needs of your app, such as graphics devices, shared directories, and so on. When you finish configuring the object, call the [`validate()`](vzvirtualmachineconfiguration/validate().md) method to determine whether a VM can successfully support your configuration. A configuration object is invalid if your app doesn’t have the [`com.apple.security.virtualization`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.virtualization) entitlement.

For more information on using `VZVirtualMachineConfiguration`, see [`Installing macOS on a Virtual Machine`](installing-macos-on-a-virtual-machine.md) and [`Creating and Running a Linux Virtual Machine`](creating-and-running-a-linux-virtual-machine.md).

## Topics

### Configuring the guest system
- [var bootLoader: VZBootLoader?](vzvirtualmachineconfiguration/bootloader.md)
  The guest system to boot when the VM starts.
### Setting the number of CPUs
- [var cpuCount: Int](vzvirtualmachineconfiguration/cpucount.md)
  The number of CPUs you make available to the guest operating system.
- [class var minimumAllowedCPUCount: Int](vzvirtualmachineconfiguration/minimumallowedcpucount.md)
  The minimum number of CPUs you may configure for the VM.
- [class var maximumAllowedCPUCount: Int](vzvirtualmachineconfiguration/maximumallowedcpucount.md)
  The maximum number of CPUs you may configure for the VM.
### Sizing the memory partition
- [var memorySize: UInt64](vzvirtualmachineconfiguration/memorysize.md)
  The amount of physical memory the guest operating system recognizes.
- [class var minimumAllowedMemorySize: UInt64](vzvirtualmachineconfiguration/minimumallowedmemorysize.md)
  The minimum amount of memory that you may configure for the VM.
- [class var maximumAllowedMemorySize: UInt64](vzvirtualmachineconfiguration/maximumallowedmemorysize.md)
  The maximum amount of memory that you may configure for the VM.
- [var memoryBalloonDevices: [VZMemoryBalloonDeviceConfiguration]](vzvirtualmachineconfiguration/memoryballoondevices.md)
  An array that you configure with a memory balloon device, used to update the memory in the VM.
### Adding devices to the VM
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
- [var usbControllers: [VZUSBControllerConfiguration]](vzvirtualmachineconfiguration/usbcontrollers.md)
  The list of configured USB controllers for the VM.
### Validating the configuration
- [func validate() throws](vzvirtualmachineconfiguration/validate.md)
  Validates the current configuration settings and reports any issues that might prevent the successful initialization of the VM.
- [func validateSaveRestoreSupport() throws](vzvirtualmachineconfiguration/validatesaverestoresupport.md)
  Determines whether the framework can save or restore the VM’s current configuration.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtualMachineStartOptions](vzvirtualmachinestartoptions.md)
  The abstract class for VM start options.
- [class VZGenericPlatformConfiguration](vzgenericplatformconfiguration.md)
  The platform configuration for a generic Intel or ARM virtual machine.
- [class VZPlatformConfiguration](vzplatformconfiguration.md)
  The base class for a platform configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration)*