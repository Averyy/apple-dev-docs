# VZVirtioConsolePortConfigurationArray

**Framework**: Virtualization  
**Kind**: class

A class that represents a collection of Virtio console port configurations.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZVirtioConsolePortConfigurationArray
```

#### Overview

This array stores a collection of port configurations for a [`VZVirtioConsoleDeviceConfiguration`](vzvirtioconsoledeviceconfiguration.md). The index in the array corresponds to the port index that the VM uses. You can set a [`maximumPortCount`](vzvirtioconsoleportarray/maximumportcount.md) value, but the value must be larger than the highest indexed port. If there’s no `maximumPortCount` value set, the framework uses the value the highest indexed port.

## Topics

### Determining the number of ports
- [var maximumPortCount: UInt32](vzvirtioconsoleportconfigurationarray/maximumportcount.md)
  An unsigned integer that represents the maximum number of ports allocated by this device.
### Accessing a specific port
- [subscript(Int) -> VZVirtioConsolePortConfiguration?](vzvirtioconsoleportconfigurationarray/subscript(_:).md)
  Returns the Virtio console port configuration as the specified index.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZConsoleDeviceConfiguration](vzconsoledeviceconfiguration.md)
  The base class for a console device configuration.
- [class VZConsolePortConfiguration](vzconsoleportconfiguration.md)
  The base class for a console port configuration.
- [class VZVirtioConsoleDeviceConfiguration](vzvirtioconsoledeviceconfiguration.md)
  A console device that enables communication between the host and the guest using console ports through a Virtio interface.
- [class VZVirtioConsolePortConfiguration](vzvirtioconsoleportconfiguration.md)
  A class that represents the configuration options you can set on a Virtio console port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoleportconfigurationarray)*