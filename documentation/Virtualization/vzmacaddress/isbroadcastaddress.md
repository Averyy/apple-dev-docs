# isBroadcastAddress

**Framework**: Virtualization  
**Kind**: property

A Boolean value that indicates whether the address is a broadcast address.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var isBroadcastAddress: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the address is a broadcast address, or [`false`](https://developer.apple.com/documentation/swift/false) if it isn’t.

## See Also

- [var isMulticastAddress: Bool](vzmacaddress/ismulticastaddress.md)
  A Boolean value that indicates whether the address is a multicast address.
- [var isUnicastAddress: Bool](vzmacaddress/isunicastaddress.md)
  A Boolean value that indicates whether the address is a unicast address.
- [var isLocallyAdministeredAddress: Bool](vzmacaddress/islocallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a locally administered address (LAA).
- [var isUniversallyAdministeredAddress: Bool](vzmacaddress/isuniversallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a universally adminstered address (UAA).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/isbroadcastaddress)*