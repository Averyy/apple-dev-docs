# VZNVMExpressControllerDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The configuration object that represents an NVM Express Controller storage device.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class VZNVMExpressControllerDeviceConfiguration
```

```objc
@interface VZNVMExpressControllerDeviceConfiguration : VZStorageDeviceConfiguration
```

#### Overview

This device configuration creates a storage device that conforms to the [NVM Express specification revision 1.1b](https://nvmexpress.org/wp-content/uploads/NVM-Express-1_1b-1.pdf).

The device configuration is valid only if used with [`VZGenericPlatformConfiguration`](./vzgenericplatformconfiguration.md).

## Topics

### Creating a new device configuration
- [init(attachment: VZStorageDeviceAttachment)](./vznvmexpresscontrollerdeviceconfiguration/init%28attachment%29.md)
  Creates a new NVM Express controller configuration with the storage device attachment you provide.

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

## See Also

### Related Documentation
- [class VZGenericPlatformConfiguration](./vzgenericplatformconfiguration.md)
  The platform configuration for a generic Intel or ARM virtual machine.
### Configurations
- [class VZVirtioBlockDeviceConfiguration](./vzvirtioblockdeviceconfiguration.md)
  The configuration object that requests the creation of a virtual storage device in the guest system.
- [class VZStorageDeviceConfiguration](./vzstoragedeviceconfiguration.md)
  The common configuration traits for storage device requests.
- [class VZUSBMassStorageDeviceConfiguration](./vzusbmassstoragedeviceconfiguration.md)
  The configuration object that represents a USB Mass storage device.
- [enum VZDiskImageCachingMode](./vzdiskimagecachingmode.md)
  An integer that describes the disk image caching mode.
- [enum VZDiskImageSynchronizationMode](./vzdiskimagesynchronizationmode.md)
  An integer that describes the disk image synchronization mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznvmexpresscontrollerdeviceconfiguration)*