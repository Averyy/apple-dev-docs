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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZVirtioTraditionalMemoryBalloonDeviceConfiguration](vzvirtiotraditionalmemoryballoondeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtioTraditionalMemoryBalloonDeviceConfiguration](vzvirtiotraditionalmemoryballoondeviceconfiguration.md)
  A configuration object that provides a way to reclaim memory from the guest system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmemoryballoondeviceconfiguration)*