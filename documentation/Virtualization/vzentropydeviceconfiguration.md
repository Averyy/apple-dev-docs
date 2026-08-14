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
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [VZVirtioEntropyDeviceConfiguration](vzvirtioentropydeviceconfiguration.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZVirtioEntropyDeviceConfiguration](vzvirtioentropydeviceconfiguration.md)
  A source of entropy for the guest’s random number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzentropydeviceconfiguration)*