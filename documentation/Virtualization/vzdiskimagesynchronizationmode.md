# VZDiskImageSynchronizationMode

**Framework**: Virtualization  
**Kind**: enum  
**Role**: Enumeration

An integer that describes the disk image synchronization mode.

**Availability**:
- macOS 12.0+

## Declaration

```swift
enum VZDiskImageSynchronizationMode
```

```c
enum VZDiskImageSynchronizationMode : NSInteger;
```

## Topics

### Disk image synchronization modes
- [VZDiskImageSynchronizationMode.full](./vzdiskimagesynchronizationmode/full.md)
  Synchronizes data to the permanent storage holding the disk image.
- [VZDiskImageSynchronizationMode.fsync](./vzdiskimagesynchronizationmode/fsync.md)
  Synchronizes data to the drive using the system’s best-effort synchronization mode.
- [VZDiskImageSynchronizationMode.none](./vzdiskimagesynchronizationmode/none.md)
  Disables data synchronization with the permanent storage.
### Initializers
- [init?(rawValue: Int)](./vzdiskimagesynchronizationmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configurations
- [class VZVirtioBlockDeviceConfiguration](./vzvirtioblockdeviceconfiguration.md)
  The configuration object that requests the creation of a virtual storage device in the guest system.
- [class VZStorageDeviceConfiguration](./vzstoragedeviceconfiguration.md)
  The common configuration traits for storage device requests.
- [class VZUSBMassStorageDeviceConfiguration](./vzusbmassstoragedeviceconfiguration.md)
  The configuration object that represents a USB Mass storage device.
- [enum VZDiskImageCachingMode](./vzdiskimagecachingmode.md)
  An integer that describes the disk image caching mode.
- [class VZNVMExpressControllerDeviceConfiguration](./vznvmexpresscontrollerdeviceconfiguration.md)
  The configuration object that represents an NVM Express Controller storage device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskimagesynchronizationmode)*