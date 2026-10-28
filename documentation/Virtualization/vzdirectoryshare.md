# VZDirectoryShare

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The base class for a directory share.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZDirectoryShare
```

```objc
@interface VZDirectoryShare : NSObject
```

## Overview

A directory share defines how the system exposes host directories to a guest VM.

Don’t instantiate `VZDirectoryShare` directly, use one of its subclasses such as [`VZSingleDirectoryShare`](./vzsingledirectoryshare.md) or [`VZMultipleDirectoryShare`](./vzmultipledirectoryshare.md) instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZLinuxRosettaDirectoryShare](./vzlinuxrosettadirectoryshare.md)
- [VZMultipleDirectoryShare](./vzmultipledirectoryshare.md)
- [VZSingleDirectoryShare](./vzsingledirectoryshare.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Directory Shares
- [class VZMultipleDirectoryShare](./vzmultipledirectoryshare.md)
  An object that describes a directory share for multiple directories.
- [class VZSingleDirectoryShare](./vzsingledirectoryshare.md)
  An object that defines the directory share for a single directory.
- [class VZSharedDirectory](./vzshareddirectory.md)
  A directory on the host that you can expose to a guest.
- [class VZLinuxRosettaDirectoryShare](./vzlinuxrosettadirectoryshare.md)
  The Linux directory share for Rosetta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdirectoryshare)*