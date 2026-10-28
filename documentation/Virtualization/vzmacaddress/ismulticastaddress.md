# isMulticastAddress

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the address is a multicast address.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var isMulticastAddress: Bool { get }
```

```objc
@property (readonly, getter=isMulticastAddress) BOOL isMulticastAddress;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the address is a multicast address, or [`false`](../../Swift/false.md) if it isn’t.

## See Also

### Getting address attributes
- [var isBroadcastAddress: Bool](./isbroadcastaddress.md)
  A Boolean value that indicates whether the address is a broadcast address.
- [var isUnicastAddress: Bool](./isunicastaddress.md)
  A Boolean value that indicates whether the address is a unicast address.
- [var isLocallyAdministeredAddress: Bool](./islocallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a locally administered address (LAA).
- [var isUniversallyAdministeredAddress: Bool](./isuniversallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a universally adminstered address (UAA).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/ismulticastaddress)*