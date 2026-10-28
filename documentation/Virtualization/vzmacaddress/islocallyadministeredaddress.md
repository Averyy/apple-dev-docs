# isLocallyAdministeredAddress

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the address is a locally administered address (LAA).

**Availability**:
- macOS 11.0+

## Declaration

```swift
var isLocallyAdministeredAddress: Bool { get }
```

```objc
@property (readonly, getter=isLocallyAdministeredAddress) BOOL isLocallyAdministeredAddress;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the address is locally administered, or [`false`](../../Swift/false.md) if it isn’t. A locally administered address different than the address burned in to the physical network interface.

## See Also

### Getting address attributes
- [var isBroadcastAddress: Bool](./isbroadcastaddress.md)
  A Boolean value that indicates whether the address is a broadcast address.
- [var isMulticastAddress: Bool](./ismulticastaddress.md)
  A Boolean value that indicates whether the address is a multicast address.
- [var isUnicastAddress: Bool](./isunicastaddress.md)
  A Boolean value that indicates whether the address is a unicast address.
- [var isUniversallyAdministeredAddress: Bool](./isuniversallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a universally adminstered address (UAA).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/islocallyadministeredaddress)*