# VZMemoryBalloonDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The common configuration traits for memory balloon devices.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZMemoryBalloonDeviceConfiguration
```

```objc
@interface VZMemoryBalloonDeviceConfiguration : NSObject
```

#### Overview

Don’t instantiate this abstract class directly. Instead, instantiate one of its subclasses such as [`VZVirtioTraditionalMemoryBalloonDeviceConfiguration`](./vzvirtiotraditionalmemoryballoondeviceconfiguration.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZVirtioTraditionalMemoryBalloonDeviceConfiguration](./vzvirtiotraditionalmemoryballoondeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuration
- [class VZVirtioTraditionalMemoryBalloonDeviceConfiguration](./vzvirtiotraditionalmemoryballoondeviceconfiguration.md)
  A configuration object that provides a way to reclaim memory from the guest system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmemoryballoondeviceconfiguration)*