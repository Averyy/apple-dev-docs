# isUniversallyAdministeredAddress

**Framework**: Virtualization  
**Kind**: property

A Boolean value that indicates whether the address is a universally adminstered address (UAA).

**Availability**:
- macOS 11.0+

## Declaration

```swift
var isUniversallyAdministeredAddress: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the address is universally administered, or [`false`](https://developer.apple.com/documentation/swift/false) if it isn’t. The manufacturer of a device assigns an address of this type, and the address includes the organization’s unique identification code.

## See Also

- [var isBroadcastAddress: Bool](vzmacaddress/isbroadcastaddress.md)
  A Boolean value that indicates whether the address is a broadcast address.
- [var isMulticastAddress: Bool](vzmacaddress/ismulticastaddress.md)
  A Boolean value that indicates whether the address is a multicast address.
- [var isUnicastAddress: Bool](vzmacaddress/isunicastaddress.md)
  A Boolean value that indicates whether the address is a unicast address.
- [var isLocallyAdministeredAddress: Bool](vzmacaddress/islocallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a locally administered address (LAA).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/isuniversallyadministeredaddress)*