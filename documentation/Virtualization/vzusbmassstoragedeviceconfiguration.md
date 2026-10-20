# VZUSBMassStorageDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The configuration object that represents a USB Mass storage device.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZUSBMassStorageDeviceConfiguration
```

```objc
@interface VZUSBMassStorageDeviceConfiguration : VZStorageDeviceConfiguration
```

## Topics

### Creating the configuration object
- [init(attachment: VZStorageDeviceAttachment)](./vzusbmassstoragedeviceconfiguration/init%28attachment%29.md)
  Creates a new storage device configuration with the specified attachment.

## Relationships

### Inherits From
- [VZStorageDeviceConfiguration](./vzstoragedeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [VZUSBDeviceConfiguration](./vzusbdeviceconfiguration.md)

## See Also

### Configurations
- [class VZVirtioBlockDeviceConfiguration](./vzvirtioblockdeviceconfiguration.md)
  The configuration object that requests the creation of a virtual storage device in the guest system.
- [class VZStorageDeviceConfiguration](./vzstoragedeviceconfiguration.md)
  The common configuration traits for storage device requests.
- [enum VZDiskImageCachingMode](./vzdiskimagecachingmode.md)
  An integer that describes the disk image caching mode.
- [enum VZDiskImageSynchronizationMode](./vzdiskimagesynchronizationmode.md)
  An integer that describes the disk image synchronization mode.
- [class VZNVMExpressControllerDeviceConfiguration](./vznvmexpresscontrollerdeviceconfiguration.md)
  The configuration object that represents an NVM Express Controller storage device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbmassstoragedeviceconfiguration)*