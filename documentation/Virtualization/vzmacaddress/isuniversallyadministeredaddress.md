# isUniversallyAdministeredAddress

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the address is a universally adminstered address (UAA).

**Availability**:
- macOS 11.0+

## Declaration

```swift
var isUniversallyAdministeredAddress: Bool { get }
```

```objc
@property (readonly, getter=isUniversallyAdministeredAddress) BOOL isUniversallyAdministeredAddress;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the address is universally administered, or [`false`](../../Swift/false.md) if it isn’t. The manufacturer of a device assigns an address of this type, and the address includes the organization’s unique identification code.

## See Also

### Getting address attributes
- [var isBroadcastAddress: Bool](./isbroadcastaddress.md)
  A Boolean value that indicates whether the address is a broadcast address.
- [var isMulticastAddress: Bool](./ismulticastaddress.md)
  A Boolean value that indicates whether the address is a multicast address.
- [var isUnicastAddress: Bool](./isunicastaddress.md)
  A Boolean value that indicates whether the address is a unicast address.
- [var isLocallyAdministeredAddress: Bool](./islocallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a locally administered address (LAA).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/isuniversallyadministeredaddress)*