# isUnicastAddress

**Framework**: Virtualization  
**Kind**: property

A Boolean value that indicates whether the address is a unicast address.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var isUnicastAddress: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the address is a unicast address, or [`false`](https://developer.apple.com/documentation/Swift/false) if it isn’t.

## See Also

- [var isBroadcastAddress: Bool](vzmacaddress/isbroadcastaddress.md)
  A Boolean value that indicates whether the address is a broadcast address.
- [var isMulticastAddress: Bool](vzmacaddress/ismulticastaddress.md)
  A Boolean value that indicates whether the address is a multicast address.
- [var isLocallyAdministeredAddress: Bool](vzmacaddress/islocallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a locally administered address (LAA).
- [var isUniversallyAdministeredAddress: Bool](vzmacaddress/isuniversallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a universally adminstered address (UAA).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/isunicastaddress)*