# randomLocallyAdministered()

**Framework**: Virtualization  
**Kind**: method

Returns a valid, random, locally administered, unicast MAC address.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class func randomLocallyAdministered() -> Self
```

#### Return Value

A MAC address suitable for use in your network devices.

#### Discussion

This method doesn’t guarantee the generation of a unique MAC address.

## See Also

- [convenience init?(string: String)](vzmacaddress/init(string:).md)
  Creates a MAC address object from a specially formatted string.
- [init(ethernetAddress: ether_addr_t)](vzmacaddress/init(ethernetaddress:).md)
  Creates a MAC address from the specified 48-bit Ethernet address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/randomlocallyadministered())*