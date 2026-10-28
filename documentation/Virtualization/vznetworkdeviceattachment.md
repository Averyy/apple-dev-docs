# VZNetworkDeviceAttachment

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The common behaviors for the network attachment points of your virtual machine.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZNetworkDeviceAttachment
```

```objc
@interface VZNetworkDeviceAttachment : NSObject
```

## Overview

Don’t create a [`VZNetworkDeviceAttachment`](./vznetworkdeviceattachment.md) object directly. Instead, instantiate one of its concrete subclasses and use that object to configure your network devices. Each concrete subclass represents a specific type of network interface on the host computer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZBridgedNetworkDeviceAttachment](./vzbridgednetworkdeviceattachment.md)
- [VZFileHandleNetworkDeviceAttachment](./vzfilehandlenetworkdeviceattachment.md)
- [VZNATNetworkDeviceAttachment](./vznatnetworkdeviceattachment.md)
- [VZVmnetNetworkDeviceAttachment](./vzvmnetnetworkdeviceattachment.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Attachment points
- [class VZBridgedNetworkDeviceAttachment](./vzbridgednetworkdeviceattachment.md)
  A network device that interacts directly with a physical network interface on the host computer.
- [class VZFileHandleNetworkDeviceAttachment](./vzfilehandlenetworkdeviceattachment.md)
  A network device that transmits raw network packets and frames using a datagram socket.
- [class VZNATNetworkDeviceAttachment](./vznatnetworkdeviceattachment.md)
  A device that routes network requests through the host computer and performs network address translation on the resulting packets.
- [class VZVmnetNetworkDeviceAttachment](./vzvmnetnetworkdeviceattachment.md)
  A network device attachment that allows a custom network topology.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkdeviceattachment)*