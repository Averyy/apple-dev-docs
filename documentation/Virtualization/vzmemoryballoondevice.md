# VZMemoryBalloonDevice

**Framework**: Virtualization  
**Kind**: class

The common behavior for memory devices.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZMemoryBalloonDevice
```

#### Overview

Don’t instantiate this class directly. To request a memory ballon device, add an appropriate configuration object to the [`memoryBalloonDevices`](vzvirtualmachineconfiguration/memoryballoondevices.md) property of the [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) object that you use to configure the virtual machine. In response, the system instantiates the subclass of [`VZMemoryBalloonDevice`](vzmemoryballoondevice.md) that matches your request. For example, if you supply a [`VZVirtioTraditionalMemoryBalloonDeviceConfiguration`](vzvirtiotraditionalmemoryballoondeviceconfiguration.md) object in your configuration, the system creates a [`VZVirtioTraditionalMemoryBalloonDevice`](vzvirtiotraditionalmemoryballoondevice.md) object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZVirtioTraditionalMemoryBalloonDevice](vzvirtiotraditionalmemoryballoondevice.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtioTraditionalMemoryBalloonDevice](vzvirtiotraditionalmemoryballoondevice.md)
  The object you use to change the amount of memory allocated to the guest system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmemoryballoondevice)*