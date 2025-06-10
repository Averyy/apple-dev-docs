# Running Intel Binaries in Linux VMs with Rosetta

**Framework**: Virtualization

Run x86_64 Linux binaries under ARM Linux on Apple silicon.

#### Overview

In macOS 13 and later on Mac computers with Apple silicon chips, the Virtualization framework supports Rosetta in ARM Linux virtual machines (VMs). Rosetta is a translation process that allows users to run apps that contain x86_64 instructions on Apple silicon. In macOS, this allows apps built for Intel-based Mac computers to run seamlessly on Apple silicon; Rosetta allows the same capability for Intel Linux apps in ARM Linux VMs.

> **Note**:  Rosetta doesn’t support the bootstrapping or installation of Intel Linux distributions on Mac computers with Apple silicon using the Virtualization framework. Intel Linux distributions can run using the Virtualization framework on Intel-based Mac computers without the need for this translation capability.

##### Test for Rosetta Availability

Before trying to install, run, or activate Rosetta, your app should check to ensure that the capability is available in the version of macOS running on the host computer. The [`availability`](vzlinuxrosettadirectoryshare/availability.md) class method returns a value from the [`VZLinuxRosettaAvailability`](vzlinuxrosettaavailability.md) enumeration that describes whether the current host supports Rosetta or if the capability is already installed on the host Mac. The example below shows the process for checking for Rosetta availability:

##### Install Rosetta

Installing Rosetta is a one-time process per computer that requires the user to grant permission for the system to install Rosetta. If Rosetta is already installed in macOS, the system activates it for use under the Virtualization framework; if Rosetta isn’t installed, the framework downloads the installer from the network and performs the installation. The installer interactively prompts the user for authorization, and your app should handle any of the possible error conditions that could occur during the authorization, download, and installation process. The example below shows how to start the installation:

##### Create the Rosetta Directory Share

After installing Rosetta, your app needs to configure a Rosetta directory share in the Linux guest. The shared directory must have a tag that uniquely identifies the share and that you validate using [`validateTag(_:)`](vzvirtiofilesystemdeviceconfiguration/validatetag(_:).md) to ensure it conforms to the length and format for file system tags:

##### Mount the Shared Directory and Register Rosetta

In order to use Rosetta in the Linux guest, the user must mount the Rosetta share in the guest VM and install Rosetta as the application the system uses to run x86_64 binaries using the following process:

> ❗ **Important**:  The remaining steps required to activate Rosetta in a Linux guest aren’t commands that your app can execute or that you can script from inside your application to a Linux VM; the user must perform them either interactively or as part of a script while logged in to the Linux guest. You must communicate these requirements to the user of your app.

1. Install the `update-binfmts` command, if necessary. The command is part of the binfmt-support package in most Linux distributions; installation methods vary by distribution. Additionally, in order to run this command, the user must be able to use the `sudo` command, which requires adding their username to the system’s `/etc/sudoers` file.
2. Create a directory as a mount point.
3. Mount the VirtioFS file system tag to the mount point. This is the file system tag the app uses to identify the share and must be the same as the tag the user specifies on the command line demonstrated here.
4. Check if the mounted directory has the Rosetta runtime. You should see `rosetta` in the mounted directory.
5. Register the Rosetta runtime binary as the handler for x86_64 ELF format executable files using the `update-binfmts` command. The `magic` parameter describes the first 20 bytes of the ELF header for x86_64 binaries. The Linux kernel performs a bitwise logical `AND` with the first 20 bytes of a binary a user attempts to run with the `mask` value. If it matches the `magic` value, the kernel uses the registered handler as the interpreter for that binary. If the system can’t find a handler for the specified binary, it reports an error.

The example below lists the commands, with the exception of the `update-binfmts` command installation, required to enable Rosetta in the Linux guest:

> ❗ **Important**:  When using Rosetta in macOS 13, set the `preserve` option to `no.`

```bash
% mkdir /tmp/mountpoint
% sudo mount -t virtiofs EXAMPLE_TAG /tmp/mountpoint
% ls /tmp/mountpoint rosetta
% sudo /usr/sbin/update-binfmts --install rosetta /tmp/mountpoint/rosetta \
    --magic "\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x3e\x00" \
    --mask "\xff\xff\xff\xff\xff\xfe\xfe\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff" \
    --credentials yes --preserve yes --fix-binary yes
```

##### Ensure Shared Libraries Are Available for Dynamically Linked Apps

Rosetta can run statically linked x86_64 binaries without additional configuration. Binaries that are dynamically linked and that depend on shared libraries require the installation of the shared libraries, or library hierarchies, in the Linux guest in paths that are accessible to both the user and to Rosetta.

##### Configure Rosettas Ahead of Time Aot Caching Options

In macOS 14 and later, Rosetta supports options that allow you control the ahead of time (AOT) cache characteristics; this can improve the performance of some X86 workloads.

There are two modes of operation for AOT caching: The first is communication using a Unix Domain Socket where the Virtualization framework shares a file that represents the socket between the Rosetta daemon and Rosetta runtime through a symlink or bind-mount. The second is communication through an abstract socket where the framework defines a shared name rather than a shared file. 

You enable these options after you create the Rosetta directory share by setting one of the [`VZLinuxRosettaDirectoryShare.CachingOptions`](vzlinuxrosettadirectoryshare/cachingoptions-swift.enum.md) using [`setCachingOptions(_:)`](vzlinuxrosettadirectoryshare/setcachingoptions(_:).md). This example shows how to configure Rosetta’s caching options in a new virtual machine configuration using a Unix Domain Socket though a shared, named file:

The following example shows how to configure Rosetta’s caching options in a new virtual machine configuration using an abstract socket:

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
- [Virtualize Linux on a Mac](virtualize-linux-on-a-mac.md)
  Configure and run Linux guests on Apple silicon and Intel-based Mac computers.
- [Accelerating the performance of Rosetta](accelerating-the-performance-of-rosetta.md)
  Improve Rosetta performance by adding support for the total store ordering (TSO) memory model to your Linux kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/running-intel-binaries-in-linux-vms-with-rosetta)*