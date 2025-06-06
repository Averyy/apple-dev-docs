# init(string:)

**Framework**: Virtualization  
**Kind**: init

Creates a MAC address object from a specially formatted string.

**Availability**:
- macOS 11.0+

## Declaration

```swift
convenience init?(string: String)
```

#### Return Value

A MAC address object with the specified value, or `nil` if the string is formatted incorrectly.

## Parameters

- `string`: A string that contains the 6 hexadecimal bytes of the MAC address separated by colon characters. An example string is  . The string is case-insensitive, so you may use uppercase or lowercase for alphabetical characters.

## See Also

- [class func randomLocallyAdministered() -> Self](vzmacaddress/randomlocallyadministered.md)
  Returns a valid, random, locally administered, unicast MAC address.
- [init(ethernetAddress: ether_addr_t)](vzmacaddress/init(ethernetaddress:).md)
  Creates a MAC address from the specified 48-bit Ethernet address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/init(string:))*