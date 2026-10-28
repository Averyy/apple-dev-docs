# VZEntropyDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The common configuration traits for entropy devices.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZEntropyDeviceConfiguration
```

```objc
@interface VZEntropyDeviceConfiguration : NSObject
```

## Overview

Don’t create a VZEntropyDeviceConfiguration object directly. Instead, instantiate a subclass such as [`VZVirtioEntropyDeviceConfiguration`](./vzvirtioentropydeviceconfiguration.md) to configure a source of entropy for your virtual machine.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZVirtioEntropyDeviceConfiguration](./vzvirtioentropydeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configurations
- [class VZVirtioEntropyDeviceConfiguration](./vzvirtioentropydeviceconfiguration.md)
  A source of entropy for the guest’s random number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzentropydeviceconfiguration)*