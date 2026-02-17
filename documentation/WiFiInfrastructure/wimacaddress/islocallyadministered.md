# isLocallyAdministered

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

A Boolean value that indicates whether this a locally administered MAC Address.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
var isLocallyAdministered: Bool { get }
```

#### Discussion

The value of this property is `true` if the MAC address is locally administered, `false` if it has a global OUI (Organizationally Unique Identifier).

## See Also

- [var isZero: Bool](wimacaddress/iszero.md)
  A Boolean value that indicates whether this MAC address is the all-zero MAC Address.
- [var isBroadcast: Bool](wimacaddress/isbroadcast.md)
  A Boolean value that indicates whether this is the broadcast MAC Address.
- [var isMulticast: Bool](wimacaddress/ismulticast.md)
  A Boolean value that indicates whether this a multicast MAC Address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wimacaddress/islocallyadministered)*