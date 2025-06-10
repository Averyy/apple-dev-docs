# VZLinuxRosettaDirectoryShare.CachingOptions.unixSocket(_:)

**Framework**: Virtualization  
**Kind**: case

The value that describes an UNIX domain socket at a path that you specify.

**Availability**:
- macOS 14.0+

## Declaration

```swift
case unixSocket(String)
```

#### Discussion

> ❗ **Important**:  The guest operating system needs to have a directory at `path` created in order for translation caching to operate correctly.

## Parameters

- `path`: The path of the Unix Domain Socket for Rosetta to use.

## See Also

- [VZLinuxRosettaDirectoryShare.CachingOptions.abstractSocket(_:)](vzlinuxrosettadirectoryshare/cachingoptions-swift.enum/abstractsocket(_:).md)
  The value that describes an abstract socket with a name you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettadirectoryshare/cachingoptions-swift.enum/unixsocket(_:))*