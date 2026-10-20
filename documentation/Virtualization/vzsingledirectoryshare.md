# VZSingleDirectoryShare

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

An object that defines the directory share for a single directory.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZSingleDirectoryShare
```

```objc
@interface VZSingleDirectoryShare : VZDirectoryShare
```

#### Overview

This directory share exposes a single directory from the host file system to the guest.

## Topics

### Creating a directory share
- [init(directory: VZSharedDirectory)](./vzsingledirectoryshare/init%28directory%29.md)
  Creates a directory share with a directory that you specify on the host.
### Accessing directory properties
- [var directory: VZSharedDirectory](./vzsingledirectoryshare/directory.md)
  The directory on the host to share with the guest VM.

## Relationships

### Inherits From
- [VZDirectoryShare](./vzdirectoryshare.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZDirectorySharingDeviceConfiguration](./vzdirectorysharingdeviceconfiguration.md)
  The base class for a directory sharing device configuration.
### Directory Shares
- [class VZMultipleDirectoryShare](./vzmultipledirectoryshare.md)
  An object that describes a directory share for multiple directories.
- [class VZSharedDirectory](./vzshareddirectory.md)
  A directory on the host that you can expose to a guest.
- [class VZDirectoryShare](./vzdirectoryshare.md)
  The base class for a directory share.
- [class VZLinuxRosettaDirectoryShare](./vzlinuxrosettadirectoryshare.md)
  The Linux directory share for Rosetta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzsingledirectoryshare)*