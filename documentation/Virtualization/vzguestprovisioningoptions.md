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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZMacGuestProvisioningOptions](vzmacguestprovisioningoptions.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZMacGuestProvisioningOptions](vzmacguestprovisioningoptions.md)
  The configuration for guest setup during macOS virtual machine startup.
- [class VZGuestMemoryMapping](vzguestmemorymapping.md)
  An object that represents a chunk of the guest operating system’s dynamic random access memory (DRAM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzguestprovisioningoptions)*