# WIMACAddress.Hash

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct  
**Role**: Structure

The hash of a MAC Address, which you may use to identify a device the accessory discovers over the air.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct Hash
```

## Topics

### Initializers
- [init?(address: WIMACAddress, method: WIMACAddress.Hash.Method)](./hash/init%28address,method%29.md)
  Creates a new `Hash` from the given MAC Address, using a randomly-generated salt.
### Instance Properties
- [var description: String](./hash/description.md)
  A string description of the MAC Address Hash, for debugging purposes.
- [let hash: Data](./hash/hash.md)
  The hashed value of a MAC Address
- [let method: WIMACAddress.Hash.Method](./hash/method-swift.property.md)
  The method used to generate the hash.
- [let salt: Data](./hash/salt.md)
  The salt used to generate the hash.
### Instance Methods
- [func matches(address: WIMACAddress) -> Bool](./hash/matches%28address%29.md)
  `true` if the provided MAC address matches this hash, `false` otherwise.
### Enumerations
- [WIMACAddress.Hash.Method](./hash/method-swift.enum.md)
  The method used to hash the MAC Address

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wimacaddress/hash)*