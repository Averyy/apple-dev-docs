# VZVmnetNetworkDeviceAttachment

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A network device attachment that allows a custom network topology.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class VZVmnetNetworkDeviceAttachment
```

```objc
@interface VZVmnetNetworkDeviceAttachment : VZNetworkDeviceAttachment
```

## Overview

The Virtualization framework backs this attachment by a logical network which the client creates and customizes through the [vmnet](../vmnet/vmnet.md) framework APIs to allow custom network topology which allows multiple virtual machines to appear on the same network and connect with each other.

## Topics

### Creating the vmnet network device attachment
- [init(network: vmnet_network_ref)](./vzvmnetnetworkdeviceattachment/init%28network%29.md)
  Creates the attachment and configures it with the specified data.
- [var network: vmnet_network_ref](./vzvmnetnetworkdeviceattachment/network.md)
  The network object that the you initialize the attachment with.

## Relationships

### Inherits From
- [VZNetworkDeviceAttachment](./vznetworkdeviceattachment.md)
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
- [class VZNetworkDeviceAttachment](./vznetworkdeviceattachment.md)
  The common behaviors for the network attachment points of your virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvmnetnetworkdeviceattachment)*