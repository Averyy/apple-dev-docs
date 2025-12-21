# Running macOS in a virtual machine on Apple silicon

**Framework**: Virtualization

Install and run macOS in a virtual machine using the Virtualization framework.

**Availability**:
- macOS 14.0+
- Xcode 26.0+

#### Overview

This sample code project demonstrates how to install and run macOS virtual machines (VMs) on Apple silicon. The Xcode project includes two separate apps:

- `InstallationTool`, a command line utility that installs macOS from a restore image, which is a file with a `.ipsw` file extension, onto a VM. You can use this tool to download the restore image of the most current macOS release from the network, or with your own restore image. The utility creates a VM bundle and stores the resulting VM images in your Home directory.
- `macOSVirtualMachineSampleApp` is a Mac app that runs the macOS VM that `InstallationTool` installs. You use `macOSVirtualMachineSampleApp` to launch and control the macOS VM that loads and runs macOS from the VM bundle. This app includes entitlements to enable it to use Virtualization and access the VM’s’ audio input, such as the microphone.

There are four build targets in this project that represent the `InstallationTool` and the `macOSVirtualMachineSampleApp`, one set of targets each for Swift and Objective-C versions of the apps. You can use either version, they’re functionally identical.

> **Note**: The default deployment target is macOS 14. If you need to build for an earlier version of macOS, you need to change the deployment target as appropriate.

##### Configure the Sample Code Project

You need to install the virtual machine, and `VM.bundle` needs exist before launching the sample app.

1. Set up code signing for each of the project’s targets by navigating to the Signing & Capabilities settings and selecting your team from the drop-down menu.
2. Run `InstallationTool` from within Xcode or in Terminal to download the latest available macOS restore image from the network and create a macOS VM image on disk. `InstallationTool` creates a `VM.bundle` package in your Home directory, containing: - `Disk.img` — The main disk image of the installed OS.
- `AuxiliaryStorage` — The auxiliary storage for macOS.
- `MachineIdentifier` — The data representation of the `VZMacMachineIdentifier` object.
- `HardwareModel` — The data representation of the `VZMacHardwareModel` object.
- `RestoreImage.ipsw` — The restore image downloaded from the network (this file exists only if the tool runs without arguments).
3. Launch `macOSVirtualMachineSampleApp` to run the macOS guest operating system. The sample app starts the VM and configures a graphical view that you interact with. The virtual Mac continues running until you shut it down from inside the guest OS, or quit the app. To reinstall the virtual machine, delete the `VM.bundle` package and run `InstallationTool` again.

##### Install Macos From a Restore Image

After downloading a restore image, you can install macOS from that restore image.

##### Set Up the Virtual Machine

The sample app uses a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) object to configure the basic characteristics of the guest, such as the CPU count, memory size, various device configurations, and a [`VZMacOSBootLoader`](vzmacosbootloader.md) object to load the operating system from the disk image, as the following example shows:

Inside the `createVirtualMachine` method, the app also creates a platform configuration for the VM. [`VZMacPlatformConfiguration`](vzmacplatformconfiguration.md) configures important macOS-specific data that the macOS guest needs to run, including the specific [`hardwareModel`](vzmacosconfigurationrequirements/hardwaremodel.md) that the image supports, as well as a [`machineIdentifier`](vzmacplatformconfiguration/machineidentifier.md) that uniquely identifies the current VM instance and differentiates it from any others.

After creating the platform configuration, the app creates an instance of  [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) and adds video, virtual drives, and other devices to the system.

The Virtualization framework checks the configuration to make sure it supports saving and restoring.

##### Start the Vm

After building the configuration data for the VM, the sample app uses the [`VZVirtualMachine`](vzvirtualmachine.md) object to start the execution of the macOS guest operating system.

Before calling the [`start(completionHandler:)`](vzvirtualmachine/start(completionhandler:).md) or [`restoreMachineStateFrom(url:completionHandler:)`](vzvirtualmachine/restoremachinestatefrom(url:completionhandler:).md) methods, the sample app configures a delegate object to receive messages about the state of the virtual machine. When the macOS guest operating system shuts down, the virtual machine calls the delegate’s [`guestDidStop(_:)`](vzvirtualmachinedelegate/guestdidstop(_:).md) method. In response, the delegate method prints a message and exits the app. If the macOS guest stops for any reason other than a normal shutdown, the delegate prints an error message and the app exits.

If the virtual machine was running when the sample app last exited, the app calls `restoreVirtualMachine` to restore the state. If the virtual machine was in a shutdown state, the app calls `startVirtualMachine` to reboot the machine. Both methods start the VM asynchronously in the background. The VM loads the system image and boots macOS. After macOS starts, the user interacts with a [`VZVirtualMachineView`](vzvirtualmachineview.md) window that displays the macOS UI and handles keyboard and mouse input through a [`VZMacGraphicsDeviceConfiguration`](vzmacgraphicsdeviceconfiguration.md) as though the user is interacting directly with the Mac hardware. The `VZVirtualMachineView` automatically resizes the virtual machine display when window size changes, and to capture system keys such, as the Globe key on a Mac keyboard.

The `startVirtualMachine` method calls the VM’s [`start(completionHandler:)`](vzvirtualmachine/start(completionhandler:).md) method.

Or, if the app previously had the VM save its state to `SaveFile.vzvmsave`, `restoreVirtualMachine` calls the VM’s [`restoreMachineStateFrom(url:completionHandler:)`](vzvirtualmachine/restoremachinestatefrom(url:completionhandler:).md) and [`resume(completionHandler:)`](vzvirtualmachine/resume(completionhandler:).md) methods.

If the restore fails, the framework causes the virtual machine to reboot. In either case, the framework deletes `SaveFile.vzvmsave`  after restore completes because the VM disk no longer matches the state in the file.

##### Save the Vm

When you close the sample app, it calls the VM’s [`pause(completionHandler:)`](vzvirtualmachine/pause(completionhandler:).md) and [`saveMachineStateTo(url:completionHandler:)`](vzvirtualmachine/savemachinestateto(url:completionhandler:).md) methods. This captures the runtime state of the VM to `SaveFile.vzvmsave`, which the app uses when calling `startOrRestoreVirtualMachine` to resume running the VM at the same point when you relaunch the sample app.

The system defers app termination until the [`saveMachineStateTo(url:completionHandler:)`](vzvirtualmachine/savemachinestateto(url:completionhandler:).md) method completes.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/running-macos-in-a-virtual-machine-on-apple-silicon)*