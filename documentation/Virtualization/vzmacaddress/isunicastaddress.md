# isUnicastAddress

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the address is a unicast address.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var isUnicastAddress: Bool { get }
```

```objc
@property (readonly, getter=isUnicastAddress) BOOL isUnicastAddress;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the address is a unicast address, or [`false`](../../Swift/false.md) if it isn’t.

## See Also

### Getting address attributes
- [var isBroadcastAddress: Bool](./isbroadcastaddress.md)
  A Boolean value that indicates whether the address is a broadcast address.
- [var isMulticastAddress: Bool](./ismulticastaddress.md)
  A Boolean value that indicates whether the address is a multicast address.
- [var isLocallyAdministeredAddress: Bool](./islocallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a locally administered address (LAA).
- [var isUniversallyAdministeredAddress: Bool](./isuniversallyadministeredaddress.md)
  A Boolean value that indicates whether the address is a universally adminstered address (UAA).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacaddress/isunicastaddress)*