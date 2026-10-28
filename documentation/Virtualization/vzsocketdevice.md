# VZSocketDevice

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The common behavior of socket devices.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZSocketDevice
```

```objc
@interface VZSocketDevice : NSObject
```

## Overview

Don’t create or use a [`VZSocketDevice`](./vzsocketdevice.md) object directly. If your virtual machine’s configuration includes a [`VZVirtioSocketDeviceConfiguration`](./vzvirtiosocketdeviceconfiguration.md) object, the virtual machine returns a [`VZVirtioSocketDevice`](./vzvirtiosocketdevice.md) object in its [`socketDevices`](./vzvirtualmachine/socketdevices.md) property. Use that object to configure the port-based communications for your virtual machine.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZVirtioSocketDevice](./vzvirtiosocketdevice.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Devices
- [class VZVirtioSocketDevice](./vzvirtiosocketdevice.md)
  A device that manages port-based connections between the guest system and the host computer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzsocketdevice)*