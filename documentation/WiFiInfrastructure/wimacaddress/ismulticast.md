# isMulticast

**Framework**: Wi-Fi Infrastructure  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this a multicast MAC Address.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var isMulticast: Bool { get }
```

#### Discussion

The value of this property is `true` if this MAC address is a multicast MAC Address, `false` otherwise.

## See Also

### Checking MAC Address properties
- [var isZero: Bool](./iszero.md)
  A Boolean value that indicates whether this MAC address is the all-zero MAC Address.
- [var isBroadcast: Bool](./isbroadcast.md)
  A Boolean value that indicates whether this is the broadcast MAC Address.
- [var isLocallyAdministered: Bool](./islocallyadministered.md)
  A Boolean value that indicates whether this a locally administered MAC Address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wimacaddress/ismulticast)*