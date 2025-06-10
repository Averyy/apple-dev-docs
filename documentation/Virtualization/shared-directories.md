# Shared directories

**Framework**: Virtualization

Configure devices that share directories from the host into the guest system.

#### Overview

Shared directories allow you expose specific directories in the macOS file system to the guest operating system running in a VM, this allows your user to share files between the host and guest operating system. To enable shared directory device support in Linux, configure the Linux guest kernel to enable the `CONFIG_VIRTIO_FS` support.

Configure a VIRTIO file system device using a [`VZVirtioFileSystemDeviceConfiguration`](vzvirtiofilesystemdeviceconfiguration.md). The guest can use the [`tag`](vzvirtiofilesystemdeviceconfiguration/tag.md) label to mount and access the host resources.

The [`VZDirectoryShare`](vzdirectoryshare.md) on the configuration defines the host directories to expose to the guest. To limit or expose new directories to the guest while the VM is running, you can update the directory share with [`VZVirtioFileSystemDevice`](vzvirtiofilesystemdevice.md).

Use [`VZSingleDirectoryShare`](vzsingledirectoryshare.md) to share the immediate contents of a single directory on the host, or use [`VZMultipleDirectoryShare`](vzmultipledirectoryshare.md) to share multiple directories from the host and include a specific name for each shared directory.

> **Note**:  Shared directories in macOS VMs are only available in macOS 13 and later.

## Topics

### Configurations
- [class VZVirtioFileSystemDeviceConfiguration](vzvirtiofilesystemdeviceconfiguration.md)
  An object that represents the configuration of a Virtio file system device.
- [class VZDirectorySharingDeviceConfiguration](vzdirectorysharingdeviceconfiguration.md)
  The base class for a directory sharing device configuration.
- [class VZLinuxRosettaDirectoryShare](vzlinuxrosettadirectoryshare.md)
  The Linux directory share for Rosetta.
### Shared directory devices
- [class VZVirtioFileSystemDevice](vzvirtiofilesystemdevice.md)
  An object the defines a VIRTIO file system device.
- [class VZDirectorySharingDevice](vzdirectorysharingdevice.md)
  The base class that represents a directory sharing device in a VM.
### Directory Shares
- [class VZMultipleDirectoryShare](vzmultipledirectoryshare.md)
  An object that describes a directory share for multiple directories.
- [class VZSingleDirectoryShare](vzsingledirectoryshare.md)
  An object that defines the directory share for a single directory.
- [class VZSharedDirectory](vzshareddirectory.md)
  A directory on the host that you can expose to a guest.
- [class VZDirectoryShare](vzdirectoryshare.md)
  The base class for a directory share.
- [class VZLinuxRosettaDirectoryShare](vzlinuxrosettadirectoryshare.md)
  The Linux directory share for Rosetta.

## See Also

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
- [Sockets](sockets.md)
  Configure a device that manages port-based communication with the guest system.
- [Storage](storage.md)
  Configure the block-storage devices that represent the disks of the guest system.
- [Consoles](consoles.md)
  Configure a device that manages multiport console communication with the guest system.
- [Clipboard sharing](clipboard-sharing.md)
  Share the pasteboard between the host and guest system.
- [USB Devices](usb-devices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/shared-directories)*