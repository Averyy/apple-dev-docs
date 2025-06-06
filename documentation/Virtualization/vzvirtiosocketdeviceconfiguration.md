# VZVirtioSocketDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

A configuration object that requests the creation of a socket device to communicate with the guest system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZVirtioSocketDeviceConfiguration
```

#### Overview

Use a [`VZVirtioSocketDeviceConfiguration`](vzvirtiosocketdeviceconfiguration.md) object to implement port-based communication between the guest operating system and the host computer. When you add this object to the [`socketDevices`](vzvirtualmachineconfiguration/socketdevices.md) property of your [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md), the virtual machine provides a corresponding [`VZVirtioSocketDevice`](vzvirtiosocketdevice.md) object to use to configure the ports. Add only one [`VZVirtioSocketDeviceConfiguration`](vzvirtiosocketdeviceconfiguration.md) to your virtual machine’s configuration.

## Topics

### Creating the Configuration Object
- [init()](vzvirtiosocketdeviceconfiguration/init.md)
  Creates a socket device configuration object.

## Relationships

### Inherits From
- [VZSocketDeviceConfiguration](vzsocketdeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZSocketDeviceConfiguration](vzsocketdeviceconfiguration.md)
  The common configuration traits for socket device requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketdeviceconfiguration)*