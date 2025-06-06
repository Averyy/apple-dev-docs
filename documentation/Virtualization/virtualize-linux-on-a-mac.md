# Virtualize Linux on a Mac

**Framework**: Virtualization

Configure and run Linux guests on Apple silicon and Intel-based Mac computers.

#### Overview

Use [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) to create a configuration that represents a specific Linux platform with the devices you want to use with your virtual machine (VM) — like [`VZVirtioSoundDeviceConfiguration`](vzvirtiosounddeviceconfiguration.md) or [`VZUSBKeyboardConfiguration`](vzusbkeyboardconfiguration.md).

You use this configuration to load a Linux kernel image from disk that — using [`VZLinuxBootLoader`](vzlinuxbootloader.md) — runs in a [`VZVirtualMachine`](vzvirtualmachine.md) that you control.

For more information about running a Linux guest, including how to download kernel and RAM disk images, see [`Creating and Running a Linux Virtual Machine`](creating-and-running-a-linux-virtual-machine.md). For more information about running GUI Linux virtual machines, see [`Running GUI Linux in a virtual machine on a Mac`](running-gui-linux-in-a-virtual-machine-on-a-mac.md).

## Topics

### Configurations
- [class VZVirtualMachineConfiguration](vzvirtualmachineconfiguration.md)
  The environment attributes and list of devices to use during the configuration of macOS or Linux VMs.
- [class VZVirtualMachineStartOptions](vzvirtualmachinestartoptions.md)
  The abstract class for VM start options.
- [class VZGenericPlatformConfiguration](vzgenericplatformconfiguration.md)
  The platform configuration for a generic Intel or ARM virtual machine.
- [class VZPlatformConfiguration](vzplatformconfiguration.md)
  The base class for a platform configuration.
### Boot loaders
- [class VZBootLoader](vzbootloader.md)
  The base class that defines the management of the initial process of the guest system.
- [class VZLinuxBootLoader](vzlinuxbootloader.md)
  An object that loads and configures a Linux kernel as the guest system of your VM.
- [class VZEFIBootLoader](vzefibootloader.md)
  The boot loader configuration the system uses to boot guest-operating systems that expect an Extensible Firmware Interface (EFI) ROM.
- [class VZEFIVariableStore](vzefivariablestore.md)
  An object that represents the Extensible Firmware Interface (EFI) variable store that contains NVRAM variables the EFI exposes.

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
- [Virtualize macOS on a Mac](virtualize-macos-on-a-mac.md)
  Configure and run macOS guests on Apple silicon.
- [Running Intel Binaries in Linux VMs with Rosetta](running-intel-binaries-in-linux-vms-with-rosetta.md)
  Run x86_64 Linux binaries under ARM Linux on Apple silicon.
- [Accelerating the performance of Rosetta](accelerating-the-performance-of-rosetta.md)
  Improve Rosetta performance by adding support for the total store ordering (TSO) memory model to your Linux kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/virtualize-linux-on-a-mac)*