# VZLinuxRosettaUnixSocketCachingOptions

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

An object that represents caching options for a UNIX domain socket.

**Availability**:
- macOS 14.0+

## Declaration

```objc
@interface VZLinuxRosettaUnixSocketCachingOptions : VZLinuxRosettaCachingOptions
```

## Overview

This object configures Rosetta to communicate with the Rosetta daemon using a UNIX domain socket.

## Topics

### Initializers
- [- init](./vzlinuxrosettaunixsocketcachingoptions/init.md)
  Creates a new Rosetta caching options object for a UNIX domain socket.
- [- initWithPath:error:](./vzlinuxrosettaunixsocketcachingoptions/initwithpath_error_.md)
  Creates a new Rosetta caching options object for a UNIX domain socket with the path you specify.
### Accessing the socket path
- [path](./vzlinuxrosettaunixsocketcachingoptions/path.md)
  The path to the UNIX domain socket that Rosetta uses.
### Type properties
- [maximumPathLength](./vzlinuxrosettaunixsocketcachingoptions/maximumpathlength.md)
  The maximum allowed length of the path to the UNIX domain socket.

## Relationships

### Inherits From
- [VZLinuxRosettaCachingOptions](./vzlinuxrosettacachingoptions.md)

## See Also

### Setting the ahead of time (AOT) caching options
- [options](./vzlinuxrosettadirectoryshare/options.md)
  The value that enables translation caching and configures the socket communication type for Rosetta.
- [VZLinuxRosettaAbstractSocketCachingOptions](./vzlinuxrosettaabstractsocketcachingoptions.md)
  Caching options for an abstract socket.
- [VZLinuxRosettaCachingOptions](./vzlinuxrosettacachingoptions.md)
  An abstract class that defines UNIX socket-based caching options for Rosetta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettaunixsocketcachingoptions)*