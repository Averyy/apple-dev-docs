# isLocallyAdministeredAddress

**Framework**: Virtualization  
**Kind**: property

A Boolean value that indicates whether the address is a locally administered address (LAA).

**Availability**:
- macOS 11.0+

## Declaration

```swift
var isLocallyAdministeredAddress: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the address is locally administered, or [`false`](https://developer.apple.com/documentation/Swift/false) if it isn’t. A locally administered address different than the address burned in to the physical network interface.

## See Also

- [var isBroadcastAddress: Bool](vzmacaddress/isbroadcastaddress.md)
  A Boolean value that indicates whether the address is a broadcast address.
- [var isMulticastAddress: Bool](vzmacaddress/ismulticastaddress.md)
  A Boolean value that indicates whether the address is a multicast address.
- [var isUnicastAddress: Bool](vzmacaddress/isunicastaddress.md)
  A Boolean value that indicates whether the address is a unicast address.
- [var isUniversallyAdministeredAddress: Bool](vzmacaddress/isuniversallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a universally adminstered address (UAA).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/islocallyadministeredaddress)*