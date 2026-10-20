# VZLinuxRosettaDirectoryShare.CachingOptions

**Framework**: Virtualization  
**Kind**: enum  
**Role**: Enumeration

Socket values you specify to configure Rosetta’s caching capabilities.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum CachingOptions
```

## Mentions

- [Running Intel Binaries in Linux VMs](../running-intel-binaries-in-linux-vms.md)

## Topics

### Socket types
- [VZLinuxRosettaDirectoryShare.CachingOptions.abstractSocket(_:)](./cachingoptions-swift.enum/abstractsocket%28_%29.md)
  The value that describes an abstract socket with a name you specify.
- [VZLinuxRosettaDirectoryShare.CachingOptions.unixSocket(_:)](./cachingoptions-swift.enum/unixsocket%28_%29.md)
  The value that describes an UNIX domain socket at a path that you specify.
### Type properties
- [static var defaultUnixSocket: VZLinuxRosettaDirectoryShare.CachingOptions](./cachingoptions-swift.enum/defaultunixsocket.md)
  The options to use for a default UNIX domain socket.
- [static var maximumNameLength: Int](./cachingoptions-swift.enum/maximumnamelength.md)
  The maximum length of the name of an abstract socket.
- [static var maximumPathLength: Int](./cachingoptions-swift.enum/maximumpathlength.md)
  The maximum length of the path to a UNIX domain socket.

## See Also

### Setting the ahead of time (AOT) caching options
- [var cachingOptions: VZLinuxRosettaDirectoryShare.CachingOptions?](./cachingoptions-swift.property.md)
  The value that enables translation caching and configures the socket communication type for Rosetta.
- [func setCachingOptions(VZLinuxRosettaDirectoryShare.CachingOptions?) throws](./setcachingoptions%28_%29.md)
  Sets the Rosetta caching options using the options you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettadirectoryshare/cachingoptions-swift.enum)*