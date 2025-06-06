# Virtualize macOS on a Mac

**Framework**: Virtualization

Configure and run macOS guests on Apple silicon.

#### Overview

Use the [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) to create a [`VZMacPlatformConfiguration`](vzmacplatformconfiguration.md) that represents a specific macOS platform configuration ([`VZMacHardwareModel`](vzmachardwaremodel.md), number of virtual CPUs, RAM, devices, and so on) that you want to run on your Apple silicon Mac.

The Virtualization framework provides everything you need to macOS on a VM using macOS installation images you download from Apple. Use the [`latestSupported`](vzmacosrestoreimage/latestsupported.md) method of [`VZMacOSRestoreImage`](vzmacosrestoreimage.md) to obtain the URL for the installation media used to install the latest version of macOS. Alternatively, if you’ve already downloaded a macOS release, you can construct a `VZMacOSRestoreImage` object using that file. The `mostFeaturefulSupportedConfiguration` property of a `VZMacOSRestoreImage` object specifies the requirements and recommendations that you use to configure a [`VZVirtualMachineDelegate`](vzvirtualmachinedelegate.md) to complete this installation. After creating a `VZVirtualMachine`, use [`VZMacOSInstaller`](vzmacosinstaller.md) to install macOS on that virtual machine. You then use this configuration to create a bootable image that, along with a [`VZMacOSBootLoader`](vzmacosbootloader.md), runs in a [`VZVirtualMachine`](vzvirtualmachine.md) that you can control.

For more information on running macOS as a guest, see `Creating and Running a macOS Virtual Machine`.

## Topics

### Platform components
- [class VZVirtualMachineConfiguration](vzvirtualmachineconfiguration.md)
  The environment attributes and list of devices to use during the configuration of macOS or Linux VMs.
- [class VZMacOSVirtualMachineStartOptions](vzmacosvirtualmachinestartoptions.md)
  A class that describes start options for macOS VMs.
- [class VZMacPlatformConfiguration](vzmacplatformconfiguration.md)
  The platform configuration for booting macOS on Apple silicon.
- [class VZPlatformConfiguration](vzplatformconfiguration.md)
  The base class for a platform configuration.
- [class VZMacHardwareModel](vzmachardwaremodel.md)
  A specification for the hardware elements and configurations present in a particular Mac hardware model.
- [class VZMacMachineIdentifier](vzmacmachineidentifier.md)
  A unique identifier for a VM.
- [class VZMacAuxiliaryStorage](vzmacauxiliarystorage.md)
  An object that contains information the boot loader needs for booting macOS as a guest operating system.
### Boot images
- [class VZMacOSBootLoader](vzmacosbootloader.md)
  An object that loads and configures a boot loader for running macOS on Apple silicon as a guest system of your VM.
- [class VZBootLoader](vzbootloader.md)
  The base class that defines the management of the initial process of the guest system.
### Installers
- [class VZMacOSInstaller](vzmacosinstaller.md)
  An object you use to install macOS on the specified virtual machine.
- [class VZMacOSRestoreImage](vzmacosrestoreimage.md)
  An object that describes a version of macOS to install on to a virtual machine.
- [class VZMacOSConfigurationRequirements](vzmacosconfigurationrequirements.md)
  An object that describes the parameter constraints required by a specific configuration of macOS.

## See Also

- [Running macOS in a virtual machine on Apple silicon](running-macos-in-a-virtual-machine-on-apple-silicon.md)
  Install and run macOS in a virtual machine using the Virtualization framework.
- [Running Linux in a Virtual Machine](running-linux-in-a-virtual-machine.md)
  Run a Linux operating system on your Mac using the Virtualization framework.
- [Running GUI Linux in a virtual machine on a Mac](running-gui-linux-in-a-virtual-machine-on-a-mac.md)
  Install and run GUI Linux in a virtual machine using the Virtualization framework.
- [Installing macOS on a Virtual Machine](installing-macos-on-a-virtual-machine.md)
  Download a macOS restore image and install it in a new VM.
- [Creating and Running a Linux Virtual Machine](creating-and-running-a-linux-virtual-machine.md)
  Design and run custom Linux guests on Apple silicon or Intel-based Mac Computers.
- [Virtualize Linux on a Mac](virtualize-linux-on-a-mac.md)
  Configure and run Linux guests on Apple silicon and Intel-based Mac computers.
- [Running Intel Binaries in Linux VMs with Rosetta](running-intel-binaries-in-linux-vms-with-rosetta.md)
  Run x86_64 Linux binaries under ARM Linux on Apple silicon.
- [Accelerating the performance of Rosetta](accelerating-the-performance-of-rosetta.md)
  Improve Rosetta performance by adding support for the total store ordering (TSO) memory model to your Linux kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/virtualize-macos-on-a-mac)*