# Virtualization

**Framework**: Virtualization  
**Kind**: module

Create virtual machines and run macOS and Linux-based operating systems.

**Availability**:
- macOS 11.0+

## Mentions

- [Creating and Running a Linux Virtual Machine](creating-and-running-a-linux-virtual-machine.md)

#### Overview

The Virtualization framework provides high-level APIs for creating and managing virtual machines (VM) on Apple silicon and Intel-based Mac computers. Use this framework to boot and run macOS or Linux-based operating systems in custom environments that you define. The framework supports the [`Virtual I/O Device (VIRTIO)`](https://developer.apple.comhttps://docs.oasis-open.org/virtio/virtio/v1.1/csprd01/virtio-v1.1-csprd01.html) specification, which defines standard interfaces for many device types, including network, socket, serial port, storage, entropy, and memory-balloon devices.

To set up a VM, configure a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md). If you’re creating a macOS guest also configure a [`VZMacPlatformConfiguration`](vzmacplatformconfiguration.md), and then add the devices you want to expose to the guest operating system. Then, create a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) object with your configuration data, and use that VM object to start, pause, and resume the VM environment. To interact with the guest, you create a [`VZVirtualMachineView`](vzvirtualmachineview.md) with the [`VZVirtualMachine`](vzvirtualmachine.md) object to display and interact with the graphical content in a window.

## Topics

### Essentials
- [Adding the Virtualization Entitlement to Your Project](adding-the-virtualization-entitlement-to-your-project.md)
  Configure your project to use the Virtualization framework.
- [com.apple.security.virtualization](../BundleResources/Entitlements/com.apple.security.virtualization.md)
  A Boolean value that indicates whether your app can use the Virtualization framework.
- [Using iCloud with macOS virtual machines](using-icloud-with-macos-virtual-machines.md)
  Access iCloud from macOS guest virtual machines.
### Virtual machine setup
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
- [Virtualize Linux on a Mac](virtualize-linux-on-a-mac.md)
  Configure and run Linux guests on Apple silicon and Intel-based Mac computers.
- [Running Intel Binaries in Linux VMs with Rosetta](running-intel-binaries-in-linux-vms-with-rosetta.md)
  Run x86_64 Linux binaries under ARM Linux on Apple silicon.
- [Accelerating the performance of Rosetta](accelerating-the-performance-of-rosetta.md)
  Improve Rosetta performance by adding support for the total store ordering (TSO) memory model to your Linux kernel.
### Runtime
- [class VZVirtualMachine](vzvirtualmachine.md)
  An object that manages the overall state and configuration of your VM.
- [class VZVirtualMachineView](vzvirtualmachineview.md)
  A view that allows user interaction with a VM.
- [class VZLinuxRosettaDirectoryShare](vzlinuxrosettadirectoryshare.md)
  The Linux directory share for Rosetta.
### Devices
- [Audio](audio.md)
  Configure audio devices that enable the guest operating system to perform audio playback and capture through the host’s audio devices.
- [Graphics](graphics.md)
  Configure a device for a guest to display its UI.
- [Keyboards and pointing devices](keyboards-and-pointing-devices.md)
  Configure devices that connect a mouse and keyboard to the guest system.
- [Memory](memory.md)
  Configure a memory balloon device to change the allocated memory for the guest system.
- [Network](network.md)
  Configure the devices that connect the guest system to the network.
- [Randomization](randomization.md)
  Configure a device for the guest system to use to generate random numbers.
- [Serial ports](serial-ports.md)
  Configure the serial devices that you use to communicate with the guest system.
- [Shared directories](shared-directories.md)
  Configure devices that share directories from the host into the guest system.
- [Sockets](sockets.md)
  Configure a device that manages port-based communication with the guest system.
- [Storage](storage.md)
  Configure the block-storage devices that represent the disks of the guest system.
- [Consoles](consoles.md)
  Configure a device that manages multiport console communication with the guest system.
- [Clipboard sharing](clipboard-sharing.md)
  Share the pasteboard between the host and guest system.
- [USB Devices](usb-devices.md)
### Enumerations
- [Virtualization enumerations](virtualization-enumerations.md)
  Control the caching modes, disk synchronization, and macOS auxiliary storage options of VMs.
### Errors
- [let VZErrorDomain: String](vzerrordomain.md)
  The error domain for the Virtualization framework.
- [struct VZError](vzerror.md)
  Errors that you might encounter when configuring or using a VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Virtualization)*