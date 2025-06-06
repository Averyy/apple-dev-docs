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

Use a [`VZDiskImageStorageDeviceAttachment`](vzdiskimagestoragedeviceattachment.md) object to manage the storage for a disk in the virtual machine. The guest operating system sees the storage as a disk. When the guest operating system writes files to disk, the virtual machine stores those files in the disk image you provide.

Create a RAW disk image in the file system of the host computer, and use that disk image to initialize your [`VZDiskImageStorageDeviceAttachment`](vzdiskimagestoragedeviceattachment.md) object. Use the attachment object to configure the [`VZVirtioBlockDeviceConfiguration`](vzvirtioblockdeviceconfiguration.md) object that you add to your virtual machine’s configuration.

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