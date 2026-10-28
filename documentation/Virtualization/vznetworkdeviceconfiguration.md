# VZNetworkDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The common configuration traits for network devices.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZNetworkDeviceConfiguration
```

```objc
@interface VZNetworkDeviceConfiguration : NSObject
```

## Overview

Don’t instantiate the [`VZNetworkDeviceConfiguration`](./vznetworkdeviceconfiguration.md) class directly. Instead, instantiate one of its subclasses, such as [`VZVirtioNetworkDeviceConfiguration`](./vzvirtionetworkdeviceconfiguration.md). Then use the properties of this class to configure the network device.

## Topics

### Setting configuration attributes
- [var attachment: VZNetworkDeviceAttachment?](./vznetworkdeviceconfiguration/attachment.md)
  The object that defines how the virtual network device communicates with the host system.
- [var macAddress: VZMACAddress](./vznetworkdeviceconfiguration/macaddress.md)
  The media access control (MAC) address to assign to the network device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZVirtioNetworkDeviceConfiguration](./vzvirtionetworkdeviceconfiguration.md)
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
- [class VZVirtioNetworkDeviceConfiguration](./vzvirtionetworkdeviceconfiguration.md)
  A configuration object that requests the creation of a network device for the guest system.
- [class VZMACAddress](./vzmacaddress.md)
  The media access control (MAC) address for a network interface in your virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkdeviceconfiguration)*