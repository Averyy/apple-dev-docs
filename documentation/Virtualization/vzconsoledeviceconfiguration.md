# VZConsoleDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

The base class for a console device configuration.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZConsoleDeviceConfiguration
```

#### Overview

Don’t instantiate VZConsoleDeviceConfiguration directly, instead use one of its subclasses like [`VZVirtioConsoleDeviceConfiguration`](vzvirtioconsoledeviceconfiguration.md) instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZVirtioConsoleDeviceConfiguration](vzvirtioconsoledeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZConsolePortConfiguration](vzconsoleportconfiguration.md)
  The base class for a console port configuration.
- [class VZVirtioConsoleDeviceConfiguration](vzvirtioconsoledeviceconfiguration.md)
  A console device that enables communication between the host and the guest using console ports through a Virtio interface.
- [class VZVirtioConsolePortConfiguration](vzvirtioconsoleportconfiguration.md)
  A class that represents the configuration options you can set on a Virtio console port.
- [class VZVirtioConsolePortConfigurationArray](vzvirtioconsoleportconfigurationarray.md)
  A class that represents a collection of Virtio console port configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzconsoledeviceconfiguration)*