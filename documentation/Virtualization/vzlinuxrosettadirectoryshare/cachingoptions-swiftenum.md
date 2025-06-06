# VZLinuxRosettaDirectoryShare.CachingOptions

**Framework**: Virtualization  
**Kind**: enum

Socket values you specify to configure Rosetta’s caching capabilities.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum CachingOptions
```

## Mentions

- [Running Intel Binaries in Linux VMs with Rosetta](running-intel-binaries-in-linux-vms-with-rosetta.md)

## Topics

### Socket types
- [VZLinuxRosettaDirectoryShare.CachingOptions.abstractSocket(_:)](vzlinuxrosettadirectoryshare/cachingoptions-swift.enum/abstractsocket(_:).md)
  The value that describes an abstract socket with a name you specify.
- [VZLinuxRosettaDirectoryShare.CachingOptions.unixSocket(_:)](vzlinuxrosettadirectoryshare/cachingoptions-swift.enum/unixsocket(_:).md)
  The value that describes an UNIX domain socket at a path that you specify.
### Type properties
- [static var defaultUnixSocket: VZLinuxRosettaDirectoryShare.CachingOptions](vzlinuxrosettadirectoryshare/cachingoptions-swift.enum/defaultunixsocket.md)
  The options to use for a default UNIX domain socket.
- [static var maximumNameLength: Int](vzlinuxrosettadirectoryshare/cachingoptions-swift.enum/maximumnamelength.md)
  The maximum length of the name of an abstract socket.
- [static var maximumPathLength: Int](vzlinuxrosettadirectoryshare/cachingoptions-swift.enum/maximumpathlength.md)
  The maximum length of the path to a UNIX domain socket.

## See Also

- [var cachingOptions: VZLinuxRosettaDirectoryShare.CachingOptions?](vzlinuxrosettadirectoryshare/cachingoptions-swift.property.md)
  The value that enables translation caching and configures the socket communication type for Rosetta.
- [func setCachingOptions(VZLinuxRosettaDirectoryShare.CachingOptions?) throws](vzlinuxrosettadirectoryshare/setcachingoptions(_:).md)
  Sets the Rosetta caching options using the options you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettadirectoryshare/cachingoptions-swift.enum)*