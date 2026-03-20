# WIMACAddress.Hash

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

The hash of a MAC Address, which you may use to identify a device the accessory discovers over the air.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct Hash
```

## Topics

### Initializers
- [init?(address: WIMACAddress, method: WIMACAddress.Hash.Method)](wimacaddress/hash/init(address:method:).md)
  Creates a new `Hash` from the given MAC Address, using a randomly-generated salt.
### Instance Properties
- [var description: String](wimacaddress/hash/description.md)
  A string description of the MAC Address Hash, for debugging purposes.
- [let hash: Data](wimacaddress/hash/hash.md)
  The hashed value of a MAC Address
- [let method: WIMACAddress.Hash.Method](wimacaddress/hash/method-swift.property.md)
  The method used to generate the hash.
- [let salt: Data](wimacaddress/hash/salt.md)
  The salt used to generate the hash.
### Instance Methods
- [func matches(address: WIMACAddress) -> Bool](wimacaddress/hash/matches(address:).md)
  `true` if the provided MAC address matches this hash, `false` otherwise.
### Enumerations
- [WIMACAddress.Hash.Method](wimacaddress/hash/method-swift.enum.md)
  The method used to hash the MAC Address

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wimacaddress/hash)*