# VZDirectoryShare

**Framework**: Virtualization  
**Kind**: class

The base class for a directory share.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZDirectoryShare
```

#### Overview

A directory share defines how the system exposes host directories to a guest VM.

Don’t instantiate `VZDirectoryShare` directly, use one of its subclasses such as [`VZSingleDirectoryShare`](vzsingledirectoryshare.md) or [`VZMultipleDirectoryShare`](vzmultipledirectoryshare.md) instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZLinuxRosettaDirectoryShare](vzlinuxrosettadirectoryshare.md)
- [VZMultipleDirectoryShare](vzmultipledirectoryshare.md)
- [VZSingleDirectoryShare](vzsingledirectoryshare.md)
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
- [class VZSharedDirectory](vzshareddirectory.md)
  A directory on the host that you can expose to a guest.
- [class VZLinuxRosettaDirectoryShare](vzlinuxrosettadirectoryshare.md)
  The Linux directory share for Rosetta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdirectoryshare)*