# VZDiskImageCachingMode

**Framework**: Virtualization  
**Kind**: enum

An integer that describes the disk image caching mode.

**Availability**:
- macOS 12.0+

## Declaration

```swift
enum VZDiskImageCachingMode
```

## Topics

### Disk image caching modes
- [VZDiskImageCachingMode.automatic](vzdiskimagecachingmode/automatic.md)
  Allows the virtualization framework to automatically determine whether to enable data caching.
- [VZDiskImageCachingMode.cached](vzdiskimagecachingmode/cached.md)
  Enables data caching.
- [VZDiskImageCachingMode.uncached](vzdiskimagecachingmode/uncached.md)
  Disables data caching.
### Initializers
- [init?(rawValue: Int)](vzdiskimagecachingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class VZVirtioBlockDeviceConfiguration](vzvirtioblockdeviceconfiguration.md)
  The configuration object that requests the creation of a virtual storage device in the guest system.
- [class VZStorageDeviceConfiguration](vzstoragedeviceconfiguration.md)
  The common configuration traits for storage device requests.
- [class VZUSBMassStorageDeviceConfiguration](vzusbmassstoragedeviceconfiguration.md)
  The configuration object that represents a USB Mass storage device.
- [enum VZDiskImageSynchronizationMode](vzdiskimagesynchronizationmode.md)
  An integer that describes the disk image synchronization mode.
- [class VZNVMExpressControllerDeviceConfiguration](vznvmexpresscontrollerdeviceconfiguration.md)
  The configuration object that represents an NVM Express Controller storage device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskimagecachingmode)*