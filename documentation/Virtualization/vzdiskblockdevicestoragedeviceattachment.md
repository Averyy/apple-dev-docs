# VZDiskBlockDeviceStorageDeviceAttachment

**Framework**: Virtualization  
**Kind**: class

A storage device attachment that uses a disk to store data.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class VZDiskBlockDeviceStorageDeviceAttachment
```

#### Overview

The disk block device implements a storage attachment by using an actual disk rather than a disk image on a file system.

> ⚠️ **Warning**:  Handle the disk passed to this attachment with caution. If the disk has a file system formatted on it, the guest can destroy data in a way that isn’t recoverable.

In the following example, a disk device at `/dev/rdisk42` executes the I/O operations directly on that disk rather than through a file system:

By default, only the `root` user can access the disk file handle. Running virtual machines as `root` isn’t recommended. The best practice is to open the file in a separate process that has `root` privileges, then pass the open file descriptor using XPC or a Unix socket to a non-`root` process running Virtualization. For more information about Unix sockets, see [`Streams, Sockets, and Ports`](https://developer.apple.com/documentation/Foundation/streams-sockets-and-ports); for more information on XPC services, see the [`XPC`](https://developer.apple.com/documentation/XPC) framework documentation.

> ❗ **Important**:  You can’t use this method of privilege escalation in apps distributed on the Mac App Store.

## Topics

### Initializers
- [init(fileHandle: FileHandle, readOnly: Bool, synchronizationMode: VZDiskSynchronizationMode) throws](vzdiskblockdevicestoragedeviceattachment/init(filehandle:readonly:synchronizationmode:).md)
  Creates a new block storage device attachment from a file handle and with the specified access mode, synchronization mode, and error object that you provide.
### Getting the block storage device details
- [var fileHandle: FileHandle](vzdiskblockdevicestoragedeviceattachment/filehandle.md)
  A file handle to a block device.
- [var isReadOnly: Bool](vzdiskblockdevicestoragedeviceattachment/isreadonly.md)
  A Boolean value that indicates whether this disk attachment is read-only; otherwise, if the file handle allows writes, the device can write data into it.
- [var synchronizationMode: VZDiskSynchronizationMode](vzdiskblockdevicestoragedeviceattachment/synchronizationmode.md)
  The value that defines how the disk synchronizes with the underlying storage when the guest operating system flushes data.

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

- [class VZVirtioBlockDeviceConfiguration](vzvirtioblockdeviceconfiguration.md)
  The configuration object that requests the creation of a virtual storage device in the guest system.
- [class VZDiskImageStorageDeviceAttachment](vzdiskimagestoragedeviceattachment.md)
  A device that stores content in a disk image.
- [class VZNetworkBlockDeviceStorageDeviceAttachment](vznetworkblockdevicestoragedeviceattachment.md)
  A storage device attachment backed by a Network Block Device (NBD) client.
- [class VZStorageDeviceAttachment](vzstoragedeviceattachment.md)
  The common behaviors for storage devices in the guest system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskblockdevicestoragedeviceattachment)*