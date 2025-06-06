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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZVirtioSocketDeviceConfiguration](vzvirtiosocketdeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtioSocketDeviceConfiguration](vzvirtiosocketdeviceconfiguration.md)
  A configuration object that requests the creation of a socket device to communicate with the guest system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzsocketdeviceconfiguration)*