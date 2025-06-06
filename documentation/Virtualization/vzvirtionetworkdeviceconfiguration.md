# VZVirtioNetworkDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

A configuration object that requests the creation of a network device for the guest system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZVirtioNetworkDeviceConfiguration
```

## Mentions

- [Creating and Running a Linux Virtual Machine](creating-and-running-a-linux-virtual-machine.md)

#### Overview

Use a [`VZVirtioNetworkDeviceConfiguration`](vzvirtionetworkdeviceconfiguration.md) object to configure one network interface of your virtual machine. After creating this object, assign an appropriate value to its inherited [`attachment`](vznetworkdeviceconfiguration/attachment.md) property to define the type of network interface you want. You can also assign a specific MAC address, or let the system generate a random address for you.

After creating and configuring a [`VZVirtioNetworkDeviceConfiguration`](vzvirtionetworkdeviceconfiguration.md) object, assign it to the [`networkDevices`](vzvirtualmachineconfiguration/networkdevices.md) property of your virtual machine’s configuration.

## Topics

### Creating the configuration object
- [init()](vzvirtionetworkdeviceconfiguration/init.md)
  Creates a network device configuration object for you to configure.

## Relationships

### Inherits From
- [VZNetworkDeviceConfiguration](vznetworkdeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZNetworkDeviceConfiguration](vznetworkdeviceconfiguration.md)
  The common configuration traits for network devices.
- [class VZMACAddress](vzmacaddress.md)
  The media access control (MAC) address for a network interface in your virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtionetworkdeviceconfiguration)*