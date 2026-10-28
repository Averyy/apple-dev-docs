# VZVirtioTraditionalMemoryBalloonDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A configuration object that provides a way to reclaim memory from the guest system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZVirtioTraditionalMemoryBalloonDeviceConfiguration
```

```objc
@interface VZVirtioTraditionalMemoryBalloonDeviceConfiguration : VZMemoryBalloonDeviceConfiguration
```

## Overview

Create a `VZVirtioTraditionalMemoryBalloonDeviceConfiguration` object when you want the ability to reclaim memory from the guest operating system. After creating this object, add it to the [`memoryBalloonDevices`](./vzvirtualmachineconfiguration/memoryballoondevices.md) property of your [`VZVirtualMachineConfiguration`](./vzvirtualmachineconfiguration.md) object. In response, the virtual machine provides a [`VZVirtioTraditionalMemoryBalloonDevice`](./vzvirtiotraditionalmemoryballoondevice.md) object, which you use to initiate memory-related requests with the guest system. Access that object from the [`memoryBalloonDevices`](./vzvirtualmachine/memoryballoondevices.md) property of [`VZVirtualMachine`](./vzvirtualmachine.md).

> ❗ **Important**:  Create only one `VZVirtioTraditionalMemoryBalloonDeviceConfiguration` object for your virtual machine.

## Topics

### Creating the Configuration Object
- [init()](./vzvirtiotraditionalmemoryballoondeviceconfiguration/init%28%29.md)
  Creates a memory ballon device configuration object to include with your virtual machine’s configuration data.

## Relationships

### Inherits From
- [VZMemoryBalloonDeviceConfiguration](./vzmemoryballoondeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuration
- [class VZMemoryBalloonDeviceConfiguration](./vzmemoryballoondeviceconfiguration.md)
  The common configuration traits for memory balloon devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiotraditionalmemoryballoondeviceconfiguration)*