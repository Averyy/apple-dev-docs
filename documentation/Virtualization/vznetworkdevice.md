# VZNetworkDevice

**Framework**: Virtualization  
**Kind**: class

A base class that represents a network device in a virtual machine.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZNetworkDevice
```

#### Overview

Don’t instantiate a [`VZNetworkDevice`](vznetworkdevice.md) directly. When you create a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) instance with a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) the system creates the number of network devices based on the number of [`VZVirtioNetworkDeviceConfiguration`](vzvirtionetworkdeviceconfiguration.md) objects you specify in the VM configuration. Before initializing the virtual machine (VM), validate the configuration using [`validate()`](vzvirtualmachineconfiguration/validate().md) to ensure the user’s computer supports the number of network and other devices you’ve specified.  

For many purposes, a single network that uses a Network Address Translation (NAT) attachment and connects the VM to the host computer’s network is sufficient. You can use additional network interfaces for purposes of your own design, such as:

- Bridging several physical interfaces to connect to multiple networks.
- Using the file descriptor attachment to create specialized connections for different purposes.

You access the network devices through the `VZVirtualMachine`.[`networkDevices`](vzvirtualmachine/networkdevices.md) property. The network devices map to their respective configurations in a one to one relationship, where index `i` of `VZVirtualMachine.networkDevices` corresponds to the network device configuration at index `i` set on `VZVirtualMachineConfiguration`.[`networkDevices`](vzvirtualmachineconfiguration/networkdevices.md).

## Topics

### Getting the network attachment point
- [var attachment: VZNetworkDeviceAttachment?](vznetworkdevice/attachment.md)
  The network attachment that’s connected to this network device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZNetworkDeviceConfiguration](vznetworkdeviceconfiguration.md)
  The common configuration traits for network devices.
- [vmnet](../vmnet/vmnet.md)
  Connect with network interfaces to read and write packets on guest operating systems.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkdevice)*