# VZUSBMassStorageDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

The configuration object that represents a USB Mass storage device.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZUSBMassStorageDeviceConfiguration
```

## Topics

### Creating the configuration object
- [init(attachment: VZStorageDeviceAttachment)](vzusbmassstoragedeviceconfiguration/init(attachment:).md)
  Creates a new storage device configuration with the specified attachment.

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
- [VZUSBDeviceConfiguration](vzusbdeviceconfiguration.md)

## See Also

- [class VZVirtioBlockDeviceConfiguration](vzvirtioblockdeviceconfiguration.md)
  The configuration object that requests the creation of a virtual storage device in the guest system.
- [class VZStorageDeviceConfiguration](vzstoragedeviceconfiguration.md)
  The common configuration traits for storage device requests.
- [enum VZDiskImageCachingMode](vzdiskimagecachingmode.md)
  An integer that describes the disk image caching mode.
- [enum VZDiskImageSynchronizationMode](vzdiskimagesynchronizationmode.md)
  An integer that describes the disk image synchronization mode.
- [class VZNVMExpressControllerDeviceConfiguration](vznvmexpresscontrollerdeviceconfiguration.md)
  The configuration object that represents an NVM Express Controller storage device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbmassstoragedeviceconfiguration)*