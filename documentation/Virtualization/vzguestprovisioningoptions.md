# VZGuestProvisioningOptions

**Framework**: Virtualization  
**Kind**: class

The base class for guest provisioning options.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZGuestProvisioningOptions
```

#### Overview

Don’t instantiate `VZGuestProvisioningOptions` directly; instead, use one of its subclasses, such as [`VZMacGuestProvisioningOptions`](vzmacguestprovisioningoptions.md).

## Topics

### Instance Methods
- [func validate() throws](vzguestprovisioningoptions/validate.md)
  Validates the provisioning options.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [VZMacGuestProvisioningOptions](vzmacguestprovisioningoptions.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZMacGuestProvisioningOptions](vzmacguestprovisioningoptions.md)
  The configuration for guest setup during macOS virtual machine startup.
- [class VZGuestMemoryMapping](vzguestmemorymapping.md)
  An object that represents a chunk of the guest operating system’s dynamic random access memory (DRAM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzguestprovisioningoptions)*