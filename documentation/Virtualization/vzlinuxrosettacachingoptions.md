# VZLinuxRosettaCachingOptions

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

An abstract class that defines UNIX socket-based caching options for Rosetta.

**Availability**:
- macOS 14.0+

## Declaration

```objc
@interface VZLinuxRosettaCachingOptions : NSObject
```

## Overview

`VZLinuxRosettaCachingOptions` define the communication mechanism between the Rosetta daemon and the Rosetta runtime.

Don’t instantiate `VZLinuxRosettaCachingOptions` directly. Use one of its subclasses, such as [`VZLinuxRosettaUnixSocketCachingOptions`](./vzlinuxrosettaunixsocketcachingoptions.md) or [`VZLinuxRosettaAbstractSocketCachingOptions`](./vzlinuxrosettaabstractsocketcachingoptions.md) instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZLinuxRosettaAbstractSocketCachingOptions](./vzlinuxrosettaabstractsocketcachingoptions.md)
- [VZLinuxRosettaUnixSocketCachingOptions](./vzlinuxrosettaunixsocketcachingoptions.md)

## See Also

### Setting the ahead of time (AOT) caching options
- [options](./vzlinuxrosettadirectoryshare/options.md)
  The value that enables translation caching and configures the socket communication type for Rosetta.
- [VZLinuxRosettaAbstractSocketCachingOptions](./vzlinuxrosettaabstractsocketcachingoptions.md)
  Caching options for an abstract socket.
- [VZLinuxRosettaUnixSocketCachingOptions](./vzlinuxrosettaunixsocketcachingoptions.md)
  An object that represents caching options for a UNIX domain socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettacachingoptions)*