# init(ethernetAddress:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Creates a MAC address from the specified 48-bit Ethernet address.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(ethernetAddress: ether_addr_t)
```

```objc
- (instancetype) initWithEthernetAddress:(ether_addr_t) ethernetAddress;
```

## Return Value

A MAC address object with the specified Ethernet address.

## Parameters

- `ethernetAddress`: A 48-bit Ethernet address.

## See Also

### Creating a MAC address
- [class func randomLocallyAdministered() -> Self](./randomlocallyadministered%28%29.md)
  Returns a valid, random, locally administered, unicast MAC address.
- [convenience init?(string: String)](./init%28string%29.md)
  Creates a MAC address object from a specially formatted string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/init(ethernetaddress:))*