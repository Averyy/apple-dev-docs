# VZSharedDirectory

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A directory on the host that you can expose to a guest.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZSharedDirectory
```

```objc
@interface VZSharedDirectory : NSObject
```

## Overview

This exposes a directory from the host file system to the guest.

## Topics

### Creating a Shared Directory
- [init(url: URL, readOnly: Bool)](./vzshareddirectory/init%28url,readonly%29-8j5z.md)
  Initialize with a host directory.
### Accessing Directory Properties
- [var url: URL](./vzshareddirectory/url.md)
  A file URL to a directory on the host system to expose to the guest.
- [var isReadOnly: Bool](./vzshareddirectory/isreadonly.md)
  A Boolean value that indicates whether the directory is read-only to the guest.
### Initializers
- [init(URL: URL, readOnly: Bool)](./vzshareddirectory/init%28url,readonly%29-7xt6q.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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
- [class VZDirectoryShare](./vzdirectoryshare.md)
  The base class for a directory share.
- [class VZLinuxRosettaDirectoryShare](./vzlinuxrosettadirectoryshare.md)
  The Linux directory share for Rosetta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzshareddirectory)*