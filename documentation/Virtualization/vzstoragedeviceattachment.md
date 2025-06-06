# VZStorageDeviceAttachment

**Framework**: Virtualization  
**Kind**: class

The common behaviors for storage devices in the guest system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZStorageDeviceAttachment
```

#### Overview

A [`VZStorageDeviceAttachment`](vzstoragedeviceattachment.md) object defines the implementation of a storage interface in a virtual machine. You use the attachment object to specify the source of the storage on the host computer.

Don’t create [`VZStorageDeviceAttachment`](vzstoragedeviceattachment.md) objects directly. Instead, instantiate an appropriate subclass such as [`VZDiskImageStorageDeviceAttachment`](vzdiskimagestoragedeviceattachment.md), which provides storage using a disk image.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZDiskBlockDeviceStorageDeviceAttachment](vzdiskblockdevicestoragedeviceattachment.md)
- [VZDiskImageStorageDeviceAttachment](vzdiskimagestoragedeviceattachment.md)
- [VZNetworkBlockDeviceStorageDeviceAttachment](vznetworkblockdevicestoragedeviceattachment.md)
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
- [class VZDiskImageStorageDeviceAttachment](vzdiskimagestoragedeviceattachment.md)
  A device that stores content in a disk image.
- [class VZNetworkBlockDeviceStorageDeviceAttachment](vznetworkblockdevicestoragedeviceattachment.md)
  A storage device attachment backed by a Network Block Device (NBD) client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzstoragedeviceattachment)*