# ethernetAddress

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The MAC address as an Ethernet data structure.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var ethernetAddress: ether_addr_t { get }
```

```objc
@property (readonly) ether_addr_t ethernetAddress;
```

#### Discussion

Use this property to obtain the individual octets of the Ethernet address. For more information, see `ether_addr_t`.

## See Also

### Getting the address
- [var string: String](./string.md)
  The MAC address as a formatted string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/ethernetaddress)*