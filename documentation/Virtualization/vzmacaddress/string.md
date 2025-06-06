# string

**Framework**: Virtualization  
**Kind**: property

The MAC address as a formatted string.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var string: String { get }
```

#### Discussion

The string contains the 6 hexadecimal bytes of the MAC address, separated by colon characters. Alphabetical characters are lowercase in the string. An example string is `01:23:45:ab:cd:ef`.

## See Also

- [var ethernetAddress: ether_addr_t](vzmacaddress/ethernetaddress.md)
  The MAC address as an Ethernet data structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/string)*