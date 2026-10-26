# VZLinuxRosettaAbstractSocketCachingOptions

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

Caching options for an abstract socket.

**Availability**:
- macOS 14.0+

## Declaration

```objc
@interface VZLinuxRosettaAbstractSocketCachingOptions : VZLinuxRosettaCachingOptions
```

#### Overview

Use this object to configure Rosetta to communicate with the Rosetta daemon using an abstract socket.

## Topics

### Initalizers
- [- initWithName:error:](./vzlinuxrosettaabstractsocketcachingoptions/initwithname_error_.md)
  Initialize options to set on a Rosetta directory share.
### Accessing the socket name
- [name](./vzlinuxrosettaabstractsocketcachingoptions/name.md)
  The name of the abstract socket that Rosetta uses.
### Type properties
- [maximumNameLength](./vzlinuxrosettaabstractsocketcachingoptions/maximumnamelength.md)
  The maximum length of name that the framework allows.

## Relationships

### Inherits From
- [VZLinuxRosettaCachingOptions](./vzlinuxrosettacachingoptions.md)

## See Also

### Setting the ahead of time (AOT) caching options
- [options](./vzlinuxrosettadirectoryshare/options.md)
  The value that enables translation caching and configures the socket communication type for Rosetta.
- [VZLinuxRosettaCachingOptions](./vzlinuxrosettacachingoptions.md)
  An abstract class that defines UNIX socket-based caching options for Rosetta.
- [VZLinuxRosettaUnixSocketCachingOptions](./vzlinuxrosettaunixsocketcachingoptions.md)
  An object that represents caching options for a UNIX domain socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettaabstractsocketcachingoptions)*