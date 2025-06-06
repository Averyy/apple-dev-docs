# VZNVMExpressControllerDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

The configuration object that represents an NVM Express Controller storage device.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class VZNVMExpressControllerDeviceConfiguration
```

#### Overview

This device configuration creates a storage device that conforms to the [`NVM Express specification revision 1.1b`](https://developer.apple.comhttps://nvmexpress.org/wp-content/uploads/NVM-Express-1_1b-1.pdf).

The device configuration is valid only if used with [`VZGenericPlatformConfiguration`](vzgenericplatformconfiguration.md).

## Topics

### Creating a new device configuration
- [init(attachment: VZStorageDeviceAttachment)](vznvmexpresscontrollerdeviceconfiguration/init(attachment:).md)
  Creates a new NVM Express controller configuration with the storage device attachment you provide.

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

- [class VZGenericPlatformConfiguration](vzgenericplatformconfiguration.md)
  The platform configuration for a generic Intel or ARM virtual machine.
- [class VZVirtioBlockDeviceConfiguration](vzvirtioblockdeviceconfiguration.md)
  The configuration object that requests the creation of a virtual storage device in the guest system.
- [class VZStorageDeviceConfiguration](vzstoragedeviceconfiguration.md)
  The common configuration traits for storage device requests.
- [class VZUSBMassStorageDeviceConfiguration](vzusbmassstoragedeviceconfiguration.md)
  The configuration object that represents a USB Mass storage device.
- [enum VZDiskImageCachingMode](vzdiskimagecachingmode.md)
  An integer that describes the disk image caching mode.
- [enum VZDiskImageSynchronizationMode](vzdiskimagesynchronizationmode.md)
  An integer that describes the disk image synchronization mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznvmexpresscontrollerdeviceconfiguration)*