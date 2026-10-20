# VZBridgedNetworkDeviceAttachment

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A network device that interacts directly with a physical network interface on the host computer.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZBridgedNetworkDeviceAttachment
```

```objc
@interface VZBridgedNetworkDeviceAttachment : VZNetworkDeviceAttachment
```

#### Overview

A [`VZBridgedNetworkDeviceAttachment`](./vzbridgednetworkdeviceattachment.md) object represents a physical interface on the host computer. Use this object when configuring a network interface for your virtual machine. A bridged network device sends and receives packets on the same physical interface as the host computer, but does so using a different network layer.

> ❗ **Important**:  To use this attachment, your app must have the [`com.apple.vm.networking`](../BundleResources/entitlements/com.apple.vm.networking.md) entitlement. If it doesn’t, the use of this attachment point results in an invalid [`VZVirtualMachineConfiguration`](./vzvirtualmachineconfiguration.md) object.

To configure a network device with a bridged network interface:

1. Obtain a reference to one of the host’s physical network interfaces from the [`networkInterfaces`](./vzbridgednetworkinterface/networkinterfaces.md) property of [`VZBridgedNetworkInterface`](./vzbridgednetworkinterface.md).
2. Create the [`VZBridgedNetworkDeviceAttachment`](./vzbridgednetworkdeviceattachment.md) object using the network interface.
3. Assign the attachment object to the [`attachment`](./vznetworkdeviceconfiguration/attachment.md) property of a [`VZVirtioNetworkDeviceConfiguration`](./vzvirtionetworkdeviceconfiguration.md) object.
4. Add the [`VZVirtioNetworkDeviceConfiguration`](./vzvirtionetworkdeviceconfiguration.md) object to the [`networkDevices`](./vzvirtualmachineconfiguration/networkdevices.md) property of your [`VZVirtualMachineConfiguration`](./vzvirtualmachineconfiguration.md).

## Topics

### Creating the attachment point
- [init(interface: VZBridgedNetworkInterface)](./vzbridgednetworkdeviceattachment/init%28interface%29.md)
  Creates the attachment from a bridged network interface object.
### Getting the network interface
- [var interface: VZBridgedNetworkInterface](./vzbridgednetworkdeviceattachment/interface.md)
  The network interface assigned to this attachment.

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
- [class VZFileHandleNetworkDeviceAttachment](./vzfilehandlenetworkdeviceattachment.md)
  A network device that transmits raw network packets and frames using a datagram socket.
- [class VZNATNetworkDeviceAttachment](./vznatnetworkdeviceattachment.md)
  A device that routes network requests through the host computer and performs network address translation on the resulting packets.
- [class VZVmnetNetworkDeviceAttachment](./vzvmnetnetworkdeviceattachment.md)
  A network device attachment that allows a custom network topology.
- [class VZNetworkDeviceAttachment](./vznetworkdeviceattachment.md)
  The common behaviors for the network attachment points of your virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzbridgednetworkdeviceattachment)*