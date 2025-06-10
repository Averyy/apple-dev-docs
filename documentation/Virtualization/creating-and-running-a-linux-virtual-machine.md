# Creating and Running a Linux Virtual Machine

**Framework**: Virtualization

Design and run custom Linux guests on Apple silicon or Intel-based Mac Computers.

#### Overview

Running a Linux virtual machine (VM) is an additive process that starts with selecting a Linux distribution and obtaining Linux kernel and RAM disk images, and ends with instantiating and running the Linux VM on the user’s computer.

There many Linux distributions to choose from, select one that both meets your app’s needs in terms of device and application support, and supports ARM64 or 64-bit Intel-based CPUs. You’ll also need to decide how much of the host computer’s CPU resources and memory to dedicate to the VM in order to configure a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md). Unless your VM is solving self-contained computing problems, it’s likely your VM needs to interact with the user, access the network, and so on, so you’ll want to add devices to the VM to make this possible.

Finally, after creating a suitable [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md), you’ll use a [`VZLinuxBootLoader`](vzlinuxbootloader.md) to launch your VM and a [`VZVirtualMachine`](vzvirtualmachine.md) instance to control it.

##### Obtain the Kernel and Ram Disk Images

You can obtain images for many Linux distributions, including [`Ubuntu Linux`](https://developer.apple.comhttps://cloud-images.ubuntu.com/releases/hirsute/release/unpacked/). Most Linux distributions provide downloadable kernel and RAM disk images that can run on Mac computers; however, you’ll need to download images for your specific CPU:

- For Apple silicon Mac computers, download ARM 64-bit images.
- For Intel-based Mac computers, download AMD64 images.

If your app is universal, you’ll need to obtain images for both Apple silicon and Intel-based Mac computers in order to be able to run the appropriate Linux VM on the respective Apple silicon or Intel-based Mac computer.

> **Note**:  If the distribution you choose doesn’t provide images for the kernel and RAM disk, you’ll need to assemble and package those images yourself.

Some Linux distributions store kernel images in a compressed format, sometimes indicated by a `.gz` filename extension. If the image doesn’t have a file extension, you can determine the file’s compression status using the `file` command. After determining the file format for the image, add the appropriate filename extension. For example, if the output shows the file format as “gzip compressed data,” add the `.gz` extension to the image, and then use the `gzip` or `gunzip` command to unpack the image. Running `file` against the unpacked image reveals details about the kernel image you’re verifying.

You can include the Linux kernel and RAM disk as resources in your Xcode project for use in your app, or implement a custom solution that allows the user to download and save images over the network.

##### Set Up the Linux Vm Configuration

Configure a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) with the number of CPUs and amount of memory you want to use with your VM:

##### Add Devices to Your Vm

Next, you’ll need to decide what devices your Linux VM needs. Because you can’t change or add devices to a running VM, consider what devices you’ll need to support your app’s use cases and add them to the VM’s configuration. For example, if you need:

- To connect to network services from your VM, add a [`VZVirtioNetworkDeviceConfiguration`](vzvirtionetworkdeviceconfiguration.md).
- A source of entropy, add a [`VZVirtioEntropyDeviceConfiguration`](vzvirtioentropydeviceconfiguration.md).
- Audio devices, add [`VZVirtioSoundDeviceOutputStreamConfiguration`](vzvirtiosounddeviceoutputstreamconfiguration.md), [`VZVirtioSoundDeviceOutputStreamConfiguration`](vzvirtiosounddeviceoutputstreamconfiguration.md), and their associated stream sources and device configurations.

The example below adds a serial console, and sound input and output devices to the VM’s configuration:

For more information on devices that Linux guests can support, see the Devices section on the [`Virtualization`](Virtualization.md) framework.

##### Create a Boot Loader

Create an instance of a [`VZLinuxBootLoader`](vzlinuxbootloader.md) on the `VZVirtualMachineConfiguration` with a Linux kernel and a RAM disk that you load from locations on disk:

##### Instantiate and Run the Linux Vm

Instantiate a [`VZVirtualMachine`](vzvirtualmachine.md) from the `VZVirtualMachineConfiguration` that you use to start, stop, and control your Linux guest:

## See Also

- [Running macOS in a virtual machine on Apple silicon](running-macos-in-a-virtual-machine-on-apple-silicon.md)
  Install and run macOS in a virtual machine using the Virtualization framework.
- [Running Linux in a Virtual Machine](running-linux-in-a-virtual-machine.md)
  Run a Linux operating system on your Mac using the Virtualization framework.
- [Running GUI Linux in a virtual machine on a Mac](running-gui-linux-in-a-virtual-machine-on-a-mac.md)
  Install and run GUI Linux in a virtual machine using the Virtualization framework.
- [Installing macOS on a Virtual Machine](installing-macos-on-a-virtual-machine.md)
  Download a macOS restore image and install it in a new VM.
- [Virtualize macOS on a Mac](virtualize-macos-on-a-mac.md)
  Configure and run macOS guests on Apple silicon.
- [Virtualize Linux on a Mac](virtualize-linux-on-a-mac.md)
  Configure and run Linux guests on Apple silicon and Intel-based Mac computers.
- [Running Intel Binaries in Linux VMs with Rosetta](running-intel-binaries-in-linux-vms-with-rosetta.md)
  Run x86_64 Linux binaries under ARM Linux on Apple silicon.
- [Accelerating the performance of Rosetta](accelerating-the-performance-of-rosetta.md)
  Improve Rosetta performance by adding support for the total store ordering (TSO) memory model to your Linux kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/creating-and-running-a-linux-virtual-machine)*