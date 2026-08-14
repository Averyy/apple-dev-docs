# VZSocketDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

The common configuration traits for socket device requests.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZSocketDeviceConfiguration
```

#### Overview

Don’t create a [`VZSocketDeviceConfiguration`](vzsocketdeviceconfiguration.md) object directly. Instead, create a [`VZVirtioSocketDeviceConfiguration`](vzvirtiosocketdeviceconfiguration.md) object and add it to your virtual machine’s configuration.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [VZVirtioSocketDeviceConfiguration](vzvirtiosocketdeviceconfiguration.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZVirtioSocketDeviceConfiguration](vzvirtiosocketdeviceconfiguration.md)
  A configuration object that requests the creation of a socket device to communicate with the guest system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzsocketdeviceconfiguration)*