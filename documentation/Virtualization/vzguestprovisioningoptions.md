# VZGuestProvisioningOptions

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The base class for guest provisioning options.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class VZGuestProvisioningOptions
```

```objc
@interface VZGuestProvisioningOptions : NSObject
```

## Overview

Don’t instantiate `VZGuestProvisioningOptions` directly; instead, use one of its subclasses, such as [`VZMacGuestProvisioningOptions`](./vzmacguestprovisioningoptions.md).

## Topics

### Instance Methods
- [func validate() throws](./vzguestprovisioningoptions/validate%28%29.md)
  Validates the provisioning options.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZMacGuestProvisioningOptions](./vzmacguestprovisioningoptions.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Provisioning options
- [class VZMacGuestProvisioningOptions](./vzmacguestprovisioningoptions.md)
  The configuration for guest setup during macOS virtual machine startup.
- [class VZGuestMemoryMapping](./vzguestmemorymapping.md)
  An object that represents a chunk of the guest operating system’s dynamic random access memory (DRAM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzguestprovisioningoptions)*