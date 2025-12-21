# VZVmnetNetworkDeviceAttachment

**Framework**: Virtualization  
**Kind**: class

A network device attachment that allows a custom network topology.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class VZVmnetNetworkDeviceAttachment
```

#### Overview

The Virtualization framework backs this attachment by a logical network which the client creates and customizes through the [`vmnet`](https://developer.apple.com/documentation/vmnet) framework APIs to allow custom network topology which allows multiple virtual machines to appear on the same network and connect with each other.

## Topics

### Creating the vmnet network device attachment
- [init(network: vmnet_network_ref)](vzvmnetnetworkdeviceattachment/init(network:).md)
  Creates the attachment and configures it with the specified data.
- [var network: vmnet_network_ref](vzvmnetnetworkdeviceattachment/network.md)
  The network object that the you initialize the attachment with.

## Relationships

### Inherits From
- [VZNetworkDeviceAttachment](vznetworkdeviceattachment.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZBridgedNetworkDeviceAttachment](vzbridgednetworkdeviceattachment.md)
  A network device that interacts directly with a physical network interface on the host computer.
- [class VZFileHandleNetworkDeviceAttachment](vzfilehandlenetworkdeviceattachment.md)
  A network device that transmits raw network packets and frames using a datagram socket.
- [class VZNATNetworkDeviceAttachment](vznatnetworkdeviceattachment.md)
  A device that routes network requests through the host computer and performs network address translation on the resulting packets.
- [class VZNetworkDeviceAttachment](vznetworkdeviceattachment.md)
  The common behaviors for the network attachment points of your virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvmnetnetworkdeviceattachment)*