# VZVirtioSocketDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A configuration object that requests the creation of a socket device to communicate with the guest system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZVirtioSocketDeviceConfiguration
```

```objc
@interface VZVirtioSocketDeviceConfiguration : VZSocketDeviceConfiguration
```

## Overview

Use a [`VZVirtioSocketDeviceConfiguration`](./vzvirtiosocketdeviceconfiguration.md) object to implement port-based communication between the guest operating system and the host computer. When you add this object to the [`socketDevices`](./vzvirtualmachineconfiguration/socketdevices.md) property of your [`VZVirtualMachineConfiguration`](./vzvirtualmachineconfiguration.md), the virtual machine provides a corresponding [`VZVirtioSocketDevice`](./vzvirtiosocketdevice.md) object to use to configure the ports. Add only one [`VZVirtioSocketDeviceConfiguration`](./vzvirtiosocketdeviceconfiguration.md) to your virtual machine’s configuration.

## Topics

### Creating the Configuration Object
- [init()](./vzvirtiosocketdeviceconfiguration/init%28%29.md)
  Creates a socket device configuration object.

## Relationships

### Inherits From
- [VZSocketDeviceConfiguration](./vzsocketdeviceconfiguration.md)
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
- [class VZSocketDeviceConfiguration](./vzsocketdeviceconfiguration.md)
  The common configuration traits for socket device requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosocketdeviceconfiguration)*