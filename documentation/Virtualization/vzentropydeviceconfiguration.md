# VZEntropyDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

The common configuration traits for entropy devices.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZEntropyDeviceConfiguration
```

#### Overview

Don’t create a VZEntropyDeviceConfiguration object directly. Instead, instantiate a subclass such as [`VZVirtioEntropyDeviceConfiguration`](vzvirtioentropydeviceconfiguration.md) to configure a source of entropy for your virtual machine.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZVirtioEntropyDeviceConfiguration](vzvirtioentropydeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtioEntropyDeviceConfiguration](vzvirtioentropydeviceconfiguration.md)
  A source of entropy for the guest’s random number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzentropydeviceconfiguration)*