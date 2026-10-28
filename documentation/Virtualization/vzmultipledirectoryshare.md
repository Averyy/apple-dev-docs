# VZMultipleDirectoryShare

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

An object that describes a directory share for multiple directories.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZMultipleDirectoryShare
```

```objc
@interface VZMultipleDirectoryShare : VZDirectoryShare
```

## Overview

This directory share exposes multiple directories from the host file system to the guest VM.

## Topics

### Creating a directory share
- [convenience init()](./vzmultipledirectoryshare/init%28%29.md)
  Initializes the directory share with an empty set of directories.
- [init(directories: [String : VZSharedDirectory])](./vzmultipledirectoryshare/init%28directories%29.md)
  Creates the directory share with a set of directories on the host.
### Accessing the shared directories
- [var directories: [String : VZSharedDirectory]](./vzmultipledirectoryshare/directories.md)
  The directories on the host to expose to the guest.
### Directory name utility methods
- [class func canonicalizedName(from: String) -> String?](./vzmultipledirectoryshare/canonicalizedname%28from%29.md)
  Transforms a string to be a valid directory name.
- [class func validateName(String) throws](./vzmultipledirectoryshare/validatename%28_%29.md)
  Check if a name is a valid directory name.

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
- [class VZSingleDirectoryShare](./vzsingledirectoryshare.md)
  An object that defines the directory share for a single directory.
- [class VZSharedDirectory](./vzshareddirectory.md)
  A directory on the host that you can expose to a guest.
- [class VZDirectoryShare](./vzdirectoryshare.md)
  The base class for a directory share.
- [class VZLinuxRosettaDirectoryShare](./vzlinuxrosettadirectoryshare.md)
  The Linux directory share for Rosetta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmultipledirectoryshare)*