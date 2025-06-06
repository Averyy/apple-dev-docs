# init(ethernetAddress:)

**Framework**: Virtualization  
**Kind**: init

Creates a MAC address from the specified 48-bit Ethernet address.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(ethernetAddress: ether_addr_t)
```

#### Return Value

A MAC address object with the specified Ethernet address.

## Parameters

- `ethernetAddress`: A 48-bit Ethernet address.

## See Also

- [class func randomLocallyAdministered() -> Self](vzmacaddress/randomlocallyadministered.md)
  Returns a valid, random, locally administered, unicast MAC address.
- [convenience init?(string: String)](vzmacaddress/init(string:).md)
  Creates a MAC address object from a specially formatted string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/init(ethernetaddress:))*