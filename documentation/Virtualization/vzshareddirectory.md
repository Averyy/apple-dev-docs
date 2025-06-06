# VZSharedDirectory

**Framework**: Virtualization  
**Kind**: class

A directory on the host that you can expose to a guest.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZSharedDirectory
```

#### Overview

This exposes a directory from the host file system to the guest.

## Topics

### Creating a Shared Directory
- [init(url: URL, readOnly: Bool)](vzshareddirectory/init(url:readonly:).md)
  Initialize with a host directory.
### Accessing Directory Properties
- [var url: URL](vzshareddirectory/url.md)
  A file URL to a directory on the host system to expose to the guest.
- [var isReadOnly: Bool](vzshareddirectory/isreadonly.md)
  A Boolean value that indicates whether the directory is read-only to the guest.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZMultipleDirectoryShare](vzmultipledirectoryshare.md)
  An object that describes a directory share for multiple directories.
- [class VZSingleDirectoryShare](vzsingledirectoryshare.md)
  An object that defines the directory share for a single directory.
- [class VZDirectoryShare](vzdirectoryshare.md)
  The base class for a directory share.
- [class VZLinuxRosettaDirectoryShare](vzlinuxrosettadirectoryshare.md)
  The Linux directory share for Rosetta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzshareddirectory)*