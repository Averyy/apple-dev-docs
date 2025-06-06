# VZStorageDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

The common configuration traits for storage device requests.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZStorageDeviceConfiguration
```

#### Overview

Don’t create a [`VZStorageDeviceConfiguration`](vzstoragedeviceconfiguration.md) object directly. Instead, instantiate one of its subclasses, such as [`VZVirtioBlockDeviceConfiguration`](vzvirtioblockdeviceconfiguration.md). Use the [`attachment`](vzstoragedeviceconfiguration/attachment.md) property of this class to access the device’s underlying storage.

## Topics

### Getting the attachment point
- [var attachment: VZStorageDeviceAttachment](vzstoragedeviceconfiguration/attachment.md)
  The attachment object that provides the underlying storage for the device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZNVMExpressControllerDeviceConfiguration](vznvmexpresscontrollerdeviceconfiguration.md)
- [VZUSBMassStorageDeviceConfiguration](vzusbmassstoragedeviceconfiguration.md)
- [VZVirtioBlockDeviceConfiguration](vzvirtioblockdeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtioBlockDeviceConfiguration](vzvirtioblockdeviceconfiguration.md)
  The configuration object that requests the creation of a virtual storage device in the guest system.
- [class VZUSBMassStorageDeviceConfiguration](vzusbmassstoragedeviceconfiguration.md)
  The configuration object that represents a USB Mass storage device.
- [enum VZDiskImageCachingMode](vzdiskimagecachingmode.md)
  An integer that describes the disk image caching mode.
- [enum VZDiskImageSynchronizationMode](vzdiskimagesynchronizationmode.md)
  An integer that describes the disk image synchronization mode.
- [class VZNVMExpressControllerDeviceConfiguration](vznvmexpresscontrollerdeviceconfiguration.md)
  The configuration object that represents an NVM Express Controller storage device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzstoragedeviceconfiguration)*