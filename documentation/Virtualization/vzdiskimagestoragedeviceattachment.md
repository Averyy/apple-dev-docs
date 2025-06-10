# VZDiskImageStorageDeviceAttachment

**Framework**: Virtualization  
**Kind**: class

A device that stores content in a disk image.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZDiskImageStorageDeviceAttachment
```

#### Overview

Use a [`VZDiskImageStorageDeviceAttachment`](vzdiskimagestoragedeviceattachment.md) object to manage the storage for a disk in a virtual machine (VM). The guest operating system sees the storage as a disk, and when the guest operating system writes files to the disk, the virtual machine stores the files in the disk image you provide.

The virtualization framework supports two disk image formats:

#### Create the Disk Image

Create disk images using `diskutil`, a command-line utility you can access through the Terminal app. The `diskutil` utility performs a number of functions. The command uses a specific structure that tells the app what function it’s performing, including many arguments documented in its online manual page documents. For more information, see the `diskutil` manual page by using the command `man diskutil` in Terminal.

The command to creates disk image files you use with VMs starts with `diskutil image create blank`, followed by three required arguments that describe the structure, size, and location of the disk image. The general format of the command follows the pattern shown here:

```None
diskutil image create blank --fs none --format FORMAT --size SIZE IMAGE_PATH
```

Use these parameters to specify the configuration of the disk image:

> ⚠️ **Warning**: Using `diskutil` improperly can result in data loss. Most commands don’t present confirmation prompts, so check to ensure you’re writing to the volume you expect. Also, back up your data before using any of these commands.

To create a RAW disk image in the file system of the host computer, open Terminal and run the following command, replacing the placeholder values with your own, for example:

```None
diskutil image create blank --fs none --format RAW --size SIZE IMAGE_PATH
```

A best practice is to give disk images a common and easily recognizable file extension, such as `.img`; for example `VM_Image.img`.

To create an ASIF image, replace `RAW` with `ASIF`, as shown here:

```None
diskutil image create blank --fs none --format ASIF --size SIZE IMAGE_PATH
```

You can execute `diskutil` commands under app control to create disk images programmatically.

You can also create `ASIF` or `RAW` disk images interactively using Disk Utility, a utility app that Apple provides with macOS. To create volumes with Disk Utility, open the app, then select File > New Image > Blank Image. Configure the form by selecting the disk format (either `ASIF` or `RAW`), volume size, and location for the new volume, and then click Save. For more information on using Disk Utility, see [`Disk Utility User Guide`](https://developer.apple.comhttps://support.apple.com/guide/disk-utility/welcome/mac).

Alternatively, you can create a raw disk image programmatically using the UNIX `open()` and `truncate()` standard library functions as shown here:

##### Initialize the Disk Image

After creating the disk image, you use it to initialize a VM’s [`VZDiskImageStorageDeviceAttachment`](vzdiskimagestoragedeviceattachment.md) object. Use the attachment object to configure the [`VZVirtioBlockDeviceConfiguration`](vzvirtioblockdeviceconfiguration.md) object that you add to your virtual machine’s configuration, as shown here:

## Topics

### Creating the attachment point
- [init(url: URL, readOnly: Bool) throws](vzdiskimagestoragedeviceattachment/init(url:readonly:).md)
  Creates the attachment object from the specified disk image.
- [init(url: URL, readOnly: Bool, cachingMode: VZDiskImageCachingMode, synchronizationMode: VZDiskImageSynchronizationMode) throws](vzdiskimagestoragedeviceattachment/init(url:readonly:cachingmode:synchronizationmode:).md)
  Initialize the attachment from a local file URL.
### Getting the disk image details
- [var url: URL](vzdiskimagestoragedeviceattachment/url.md)
  The URL of the underlying disk image.
- [var isReadOnly: Bool](vzdiskimagestoragedeviceattachment/isreadonly.md)
  A Boolean value that indicates whether the underlying disk image is read-only.
- [var cachingMode: VZDiskImageCachingMode](vzdiskimagestoragedeviceattachment/cachingmode.md)
  The current cacheing mode for the virtual disk image.
- [var synchronizationMode: VZDiskImageSynchronizationMode](vzdiskimagestoragedeviceattachment/synchronizationmode.md)
  The mode in which the disk image synchronizes data with the underlying storage device.

## Relationships

### Inherits From
- [VZStorageDeviceAttachment](vzstoragedeviceattachment.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZDiskBlockDeviceStorageDeviceAttachment](vzdiskblockdevicestoragedeviceattachment.md)
  A storage device attachment that uses a disk to store data.
- [class VZNetworkBlockDeviceStorageDeviceAttachment](vznetworkblockdevicestoragedeviceattachment.md)
  A storage device attachment backed by a Network Block Device (NBD) client.
- [class VZStorageDeviceAttachment](vzstoragedeviceattachment.md)
  The common behaviors for storage devices in the guest system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment)*