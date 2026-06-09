# WIMACAddress

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

A Wi-Fi MAC Address.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct WIMACAddress
```

## Topics

### Working with MAC Addresses as data
- [init?(Data)](wimacaddress/init(_:)-6044i.md)
  Create a MAC Address from the provided data.
- [let data: Data](wimacaddress/data.md)
  The raw data value of the MAC Address.
### Working with MAC Addresses as strings
- [init?(String)](wimacaddress/init(_:)-7kdi9.md)
  Creates a MAC Address from the provided case-insensitive string, of the format `"XX:XX:XX:XX:XX:XX"`.
- [var stringRepresentation: String](wimacaddress/stringrepresentation.md)
  The MAC Address as an uppercase string, in the format `"XX:XX:XX:XX:XX:XX"`.
### Working with MAC Addresses as octet components
- [init?([UInt8])](wimacaddress/init(_:)-9xhxx.md)
  Create a MAC Address from the provided octet components.
- [var components: [UInt8]](wimacaddress/components.md)
  The MAC Address as a list of octets.
### Checking MAC Address properties
- [var isZero: Bool](wimacaddress/iszero.md)
  A Boolean value that indicates whether this MAC address is the all-zero MAC Address.
- [var isBroadcast: Bool](wimacaddress/isbroadcast.md)
  A Boolean value that indicates whether this is the broadcast MAC Address.
- [var isMulticast: Bool](wimacaddress/ismulticast.md)
  A Boolean value that indicates whether this a multicast MAC Address.
- [var isLocallyAdministered: Bool](wimacaddress/islocallyadministered.md)
  A Boolean value that indicates whether this a locally administered MAC Address.
### Referencing Common MAC Addresses
- [static let zero: WIMACAddress](wimacaddress/zero.md)
  The all-zero MAC Address.
- [static let broadcast: WIMACAddress](wimacaddress/broadcast.md)
  The broadcast MAC Address, all-ones.
### Getting a description
- [var description: String](wimacaddress/description.md)
  A string description of the MAC Address, for debugging purposes.
### Structures
- [WIMACAddress.Hash](wimacaddress/hash.md)
  The hash of a MAC Address, which you may use to identify a device the accessory discovers over the air.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WISSID](wissid.md)
  The Service Set Identifier (SSID) for a Wi-Fi network, from which applications derive the human-readable network name.
- [struct WIChannel](wichannel.md)
  A WiFi Channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wimacaddress)*