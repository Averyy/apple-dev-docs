# Installing macOS on a Virtual Machine

**Framework**: Virtualization

Download a macOS restore image and install it in a new VM.

#### Overview

Each new VM begins in an empty state. To boot and run macOS in a VM, you must first install a macOS image onto the new VM. Installing macOS in a new machine requires the following steps:

1. Obtain a restore image.
2. Set up a compatible VM configuration.
3. Create a VM, install the restore image, and start the VM.

##### Obtaining the Restore Image

A macOS restore image is an installation media file for a specific version of macOS. Use [`VZMacOSRestoreImage`](vzmacosrestoreimage.md) to find restore images over the network and obtain information about their requirements. To obtain a new restore image use the [`latestSupported`](vzmacosrestoreimage/latestsupported.md) class function to download the latest supported macOS image over from Apple the network using the URL in the restore image’s [`url`](vzmacosrestoreimage/url.md) property.

If you already have a restore image on disk, you can reload the [`VZMacOSRestoreImage`](vzmacosrestoreimage.md) from a local URL instead.

##### Setting Up the Vm Configuration

Running a macOS, VM requires a valid [`VZMacPlatformConfiguration`](vzmacplatformconfiguration.md), a [`VZMacOSBootLoader`](vzmacosbootloader.md), and a configuration compatible with the [`VZMacOSRestoreImage`](vzmacosrestoreimage.md).

A [`VZMacOSRestoreImage`](vzmacosrestoreimage.md) can contain installation media for multiple Mac hardware models ([`VZMacHardwareModel`](vzmachardwaremodel.md)) and the current host may not support some of these hardware models. Use the [`mostFeaturefulSupportedConfiguration`](vzmacosrestoreimage/mostfeaturefulsupportedconfiguration.md) property to determine the hardware model and configuration requirements that provides the most complete feature set compatible with the current host. If the current hosts supports none of the hardware models, this property is `nil`.

The [`VZMacPlatformConfiguration`](vzmacplatformconfiguration.md) configuration encapsulates all the necessary unique components for booting and running macOS on Apple silicon, these are:

- The hardware model — A Mac platform configuration must describe the specific virtual Mac hardware model it targets. During installation this should match the `hardwareModel` of the [`VZMacOSRestoreImage`](vzmacosrestoreimage.md).
- Auxiliary storage — Auxiliary storage contains data used by the macOS boot loader and operating system and is necessary to boot a macOS guest OS. During installation this can be a newly created auxiliary image that uses the `hardwareModel` of the [`VZMacOSRestoreImage`](vzmacosrestoreimage.md).
- A machine identifier — A machine identifier that macOS guests use to uniquely identify the virtual hardware.

To configure the [`VZMacPlatformConfiguration`](vzmacplatformconfiguration.md) for installation:

1. Create a [`VZMacPlatformConfiguration`](vzmacplatformconfiguration.md).
2. Set its `VZMacPlatformConfiguration`.[`hardwareModel`](vzmacplatformconfiguration/hardwaremodel.md) to the `VZMacOSConfigurationRequirements`.[`hardwareModel`](vzmacosconfigurationrequirements/hardwaremodel.md).
3. Create a new [`VZMacAuxiliaryStorage`](vzmacauxiliarystorage.md) with [`init(creatingStorageAt:hardwareModel:options:)`](vzmacauxiliarystorage/init(creatingstorageat:hardwaremodel:options:).md) using the `VZMacOSConfigurationRequirements`.[`hardwareModel`](vzmacplatformconfiguration/hardwaremodel.md).
4. Set the new [`VZMacAuxiliaryStorage`](vzmacauxiliarystorage.md) on `VZMacPlatformConfiguration`.[`auxiliaryStorage`](vzmacplatformconfiguration/auxiliarystorage.md).

##### Installing and Running the Vm

Install a macOS using a [`VZMacOSInstaller`](vzmacosinstaller.md) with a VM instance and an image on the local filesystem using the following steps:

1. Create a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) with a [`VZMacPlatformConfiguration`](vzmacplatformconfiguration.md) configured as described above.
2. Create a new [`VZVirtualMachine`](vzvirtualmachine.md) from the [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md).
3. Create a [`VZMacOSInstaller`](vzmacosinstaller.md) with the [`VZVirtualMachine`](vzvirtualmachine.md) and the image that you downloaded, either as a new image from Apple servers or using a previously saved image. The URL must the refer to a local file on disk.
4. Call the installer’s [`install()`](vzmacosinstaller/install().md) to start the installation.

A VM must be in a [`VZVirtualMachine.State.stopped`](vzvirtualmachine/state-swift.enum/stopped.md) state to start installation. Pausing, or stopping the virtual machine during the installation process results in undefined behavior. You can monitor or cancel the installation progress by observing [`progress`](vzmacosinstaller/progress.md) property of the [`VZMacOSInstaller`](vzmacosinstaller.md).

The example below shows the complete process for installing and running a macOS VM:

## See Also

- [Running macOS in a virtual machine on Apple silicon](running-macos-in-a-virtual-machine-on-apple-silicon.md)
  Install and run macOS in a virtual machine using the Virtualization framework.
- [Running Linux in a Virtual Machine](running-linux-in-a-virtual-machine.md)
  Run a Linux operating system on your Mac using the Virtualization framework.
- [Running GUI Linux in a virtual machine on a Mac](running-gui-linux-in-a-virtual-machine-on-a-mac.md)
  Install and run GUI Linux in a virtual machine using the Virtualization framework.
- [Creating and Running a Linux Virtual Machine](creating-and-running-a-linux-virtual-machine.md)
  Design and run custom Linux guests on Apple silicon or Intel-based Mac Computers.
- [Virtualize macOS on a Mac](virtualize-macos-on-a-mac.md)
  Configure and run macOS guests on Apple silicon.
- [Virtualize Linux on a Mac](virtualize-linux-on-a-mac.md)
  Configure and run Linux guests on Apple silicon and Intel-based Mac computers.
- [Running Intel Binaries in Linux VMs with Rosetta](running-intel-binaries-in-linux-vms-with-rosetta.md)
  Run x86_64 Linux binaries under ARM Linux on Apple silicon.
- [Accelerating the performance of Rosetta](accelerating-the-performance-of-rosetta.md)
  Improve Rosetta performance by adding support for the total store ordering (TSO) memory model to your Linux kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/installing-macos-on-a-virtual-machine)*