# VZMACAddress

**Framework**: Virtualization  
**Kind**: class

The media access control (MAC) address for a network interface in your virtual machine.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZMACAddress
```

#### Overview

A [`VZMACAddress`](vzmacaddress.md) object contains the hardware address of your network interface. Every network device has a unique 48-bit MAC address that the system uses to route network packets to that device.

Call the [`randomLocallyAdministered()`](vzmacaddress/randomlocallyadministered().md) method to get a local MAC address suitable for use with your network interfaces. Alternatively, you can create a [`VZMACAddress`](vzmacaddress.md) object yourself from a string or `ether_addr_t` structure.

## Topics

### Creating a MAC address
- [class func randomLocallyAdministered() -> Self](vzmacaddress/randomlocallyadministered.md)
  Returns a valid, random, locally administered, unicast MAC address.
- [convenience init?(string: String)](vzmacaddress/init(string:).md)
  Creates a MAC address object from a specially formatted string.
- [init(ethernetAddress: ether_addr_t)](vzmacaddress/init(ethernetaddress:).md)
  Creates a MAC address from the specified 48-bit Ethernet address.
### Getting the address
- [var string: String](vzmacaddress/string.md)
  The MAC address as a formatted string.
- [var ethernetAddress: ether_addr_t](vzmacaddress/ethernetaddress.md)
  The MAC address as an Ethernet data structure.
### Getting address attributes
- [var isBroadcastAddress: Bool](vzmacaddress/isbroadcastaddress.md)
  A Boolean value that indicates whether the address is a broadcast address.
- [var isMulticastAddress: Bool](vzmacaddress/ismulticastaddress.md)
  A Boolean value that indicates whether the address is a multicast address.
- [var isUnicastAddress: Bool](vzmacaddress/isunicastaddress.md)
  A Boolean value that indicates whether the address is a unicast address.
- [var isLocallyAdministeredAddress: Bool](vzmacaddress/islocallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a locally administered address (LAA).
- [var isUniversallyAdministeredAddress: Bool](vzmacaddress/isuniversallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a universally adminstered address (UAA).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtioNetworkDeviceConfiguration](vzvirtionetworkdeviceconfiguration.md)
  A configuration object that requests the creation of a network device for the guest system.
- [class VZNetworkDeviceConfiguration](vznetworkdeviceconfiguration.md)
  The common configuration traits for network devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress)*