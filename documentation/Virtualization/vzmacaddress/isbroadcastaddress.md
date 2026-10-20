# isBroadcastAddress

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the address is a broadcast address.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var isBroadcastAddress: Bool { get }
```

```objc
@property (readonly, getter=isBroadcastAddress) BOOL isBroadcastAddress;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the address is a broadcast address, or [`false`](../../Swift/false.md) if it isn’t.

## See Also

### Getting address attributes
- [var isMulticastAddress: Bool](./ismulticastaddress.md)
  A Boolean value that indicates whether the address is a multicast address.
- [var isUnicastAddress: Bool](./isunicastaddress.md)
  A Boolean value that indicates whether the address is a unicast address.
- [var isLocallyAdministeredAddress: Bool](./islocallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a locally administered address (LAA).
- [var isUniversallyAdministeredAddress: Bool](./isuniversallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a universally adminstered address (UAA).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/isbroadcastaddress)*