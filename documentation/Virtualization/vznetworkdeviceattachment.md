# VZNetworkDeviceAttachment

**Framework**: Virtualization  
**Kind**: class

The common behaviors for the network attachment points of your virtual machine.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZNetworkDeviceAttachment
```

#### Overview

Don’t create a [`VZNetworkDeviceAttachment`](vznetworkdeviceattachment.md) object directly. Instead, instantiate one of its concrete subclasses and use that object to configure your network devices. Each concrete subclass represents a specific type of network interface on the host computer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZBridgedNetworkDeviceAttachment](vzbridgednetworkdeviceattachment.md)
- [VZFileHandleNetworkDeviceAttachment](vzfilehandlenetworkdeviceattachment.md)
- [VZNATNetworkDeviceAttachment](vznatnetworkdeviceattachment.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkdeviceattachment)*