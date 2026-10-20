# VZNATNetworkDeviceAttachment

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A device that routes network requests through the host computer and performs network address translation on the resulting packets.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZNATNetworkDeviceAttachment
```

```objc
@interface VZNATNetworkDeviceAttachment : VZNetworkDeviceAttachment
```

#### Overview

A [`VZNATNetworkDeviceAttachment`](./vznatnetworkdeviceattachment.md) works with the host computer to perform network address translation (NAT) on the guest system’s network packets, and then route those packets to outside networks. Use this attachment to give the guest system indirect access to external networks, instead of direct access through a shared physical network interface.

To configure a network device with a NAT attachment:

1. Create the [`VZNATNetworkDeviceAttachment`](./vznatnetworkdeviceattachment.md) object.
2. Assign the attachment object to the [`attachment`](./vznetworkdeviceconfiguration/attachment.md) property of a [`VZVirtioNetworkDeviceConfiguration`](./vzvirtionetworkdeviceconfiguration.md) object.
3. Add the [`VZVirtioNetworkDeviceConfiguration`](./vzvirtionetworkdeviceconfiguration.md) object to the [`networkDevices`](./vzvirtualmachineconfiguration/networkdevices.md) property of your [`VZVirtualMachineConfiguration`](./vzvirtualmachineconfiguration.md).

This attachment doesn’t require your app to have the [`com.apple.vm.networking`](../BundleResources/entitlements/com.apple.vm.networking.md) entitlement.

## Topics

### Creating the Attachment Point
- [init()](./vznatnetworkdeviceattachment/init%28%29.md)
  Creates an attachment that performs network address translation on the guest system’s network packets.

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
- [class VZVmnetNetworkDeviceAttachment](./vzvmnetnetworkdeviceattachment.md)
  A network device attachment that allows a custom network topology.
- [class VZNetworkDeviceAttachment](./vznetworkdeviceattachment.md)
  The common behaviors for the network attachment points of your virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznatnetworkdeviceattachment)*