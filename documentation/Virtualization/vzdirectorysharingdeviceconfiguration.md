# VZDirectorySharingDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The base class for a directory sharing device configuration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZDirectorySharingDeviceConfiguration
```

```objc
@interface VZDirectorySharingDeviceConfiguration : NSObject
```

## Overview

Don’t instantiate `VZDirectorySharingDeviceConfiguration` directly. Instead use one of its subclasses, like [`VZVirtioFileSystemDeviceConfiguration`](./vzvirtiofilesystemdeviceconfiguration.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZVirtioFileSystemDeviceConfiguration](./vzvirtiofilesystemdeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configurations
- [class VZVirtioFileSystemDeviceConfiguration](./vzvirtiofilesystemdeviceconfiguration.md)
  An object that represents the configuration of a Virtio file system device.
- [class VZLinuxRosettaDirectoryShare](./vzlinuxrosettadirectoryshare.md)
  The Linux directory share for Rosetta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdirectorysharingdeviceconfiguration)*