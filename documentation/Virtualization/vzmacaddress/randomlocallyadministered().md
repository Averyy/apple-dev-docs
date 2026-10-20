# randomLocallyAdministered()

**Framework**: Virtualization  
**Kind**: method  
**Role**: Type Method

Returns a valid, random, locally administered, unicast MAC address.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class func randomLocallyAdministered() -> Self
```

```objc
+ (instancetype) randomLocallyAdministeredAddress;
```

#### Return Value

A MAC address suitable for use in your network devices.

#### Discussion

This method doesn’t guarantee the generation of a unique MAC address.

## See Also

### Creating a MAC address
- [convenience init?(string: String)](./init%28string%29.md)
  Creates a MAC address object from a specially formatted string.
- [init(ethernetAddress: ether_addr_t)](./init%28ethernetaddress%29.md)
  Creates a MAC address from the specified 48-bit Ethernet address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/randomlocallyadministered())*