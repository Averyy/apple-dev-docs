# VZVirtioBlockDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

The configuration object that requests the creation of a virtual storage device in the guest system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZVirtioBlockDeviceConfiguration
```

#### Overview

Use a [`VZVirtioBlockDeviceConfiguration`](vzvirtioblockdeviceconfiguration.md) object to create an emulated storage device in your virtual machine. When you add this object to your virtual machine configuration, the virtual machine creates an emulated disk for the guest operating system to use to read and write files. The emulated storage device conforms to the Virtio Block Device specification.

When you create a [`VZVirtioBlockDeviceConfiguration`](vzvirtioblockdeviceconfiguration.md) object, specify the attachment object that implements the underlying storage. For example, specify a [`VZDiskImageStorageDeviceAttachment`](vzdiskimagestoragedeviceattachment.md) object to configure the storage device using a disk image in the local file system. Assign your configuration object to the [`storageDevices`](vzvirtualmachineconfiguration/storagedevices.md) property of your [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) object before creating your virtual machine.

## Topics

### Creating the configuration object
- [init(attachment: VZStorageDeviceAttachment)](vzvirtioblockdeviceconfiguration/init(attachment:).md)
  Creates a block device configuration object that uses the specified storage medium.
### Identifying a block device
- [var blockDeviceIdentifier: String](vzvirtioblockdeviceconfiguration/blockdeviceidentifier.md)
  The string that identifies the VIRTIO block device.
### Validating device identifiers
- [class func validateBlockDeviceIdentifier(String) throws](vzvirtioblockdeviceconfiguration/validateblockdeviceidentifier(_:).md)
  Checks the validity of a block device identifier.

## Relationships

### Inherits From
- [VZStorageDeviceConfiguration](vzstoragedeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZStorageDeviceConfiguration](vzstoragedeviceconfiguration.md)
  The common configuration traits for storage device requests.
- [class VZUSBMassStorageDeviceConfiguration](vzusbmassstoragedeviceconfiguration.md)
  The configuration object that represents a USB Mass storage device.
- [enum VZDiskImageCachingMode](vzdiskimagecachingmode.md)
  An integer that describes the disk image caching mode.
- [enum VZDiskImageSynchronizationMode](vzdiskimagesynchronizationmode.md)
  An integer that describes the disk image synchronization mode.
- [class VZNVMExpressControllerDeviceConfiguration](vznvmexpresscontrollerdeviceconfiguration.md)
  The configuration object that represents an NVM Express Controller storage device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioblockdeviceconfiguration)*