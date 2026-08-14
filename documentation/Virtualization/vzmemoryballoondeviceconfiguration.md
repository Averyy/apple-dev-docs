# VZMemoryBalloonDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

The common configuration traits for memory balloon devices.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZMemoryBalloonDeviceConfiguration
```

#### Overview

Don’t instantiate this abstract class directly. Instead, instantiate one of its subclasses such as [`VZVirtioTraditionalMemoryBalloonDeviceConfiguration`](vzvirtiotraditionalmemoryballoondeviceconfiguration.md).

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [VZVirtioTraditionalMemoryBalloonDeviceConfiguration](vzvirtiotraditionalmemoryballoondeviceconfiguration.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZVirtioTraditionalMemoryBalloonDeviceConfiguration](vzvirtiotraditionalmemoryballoondeviceconfiguration.md)
  A configuration object that provides a way to reclaim memory from the guest system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmemoryballoondeviceconfiguration)*