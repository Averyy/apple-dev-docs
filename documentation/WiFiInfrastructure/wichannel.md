# WIChannel

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

A WiFi Channel.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct WIChannel
```

## Topics

### Instance Properties
- [let band: WIChannel.Band](wichannel/band-swift.property.md)
  The Wi-Fi band of a given channel.
- [var description: String](wichannel/description.md)
  A string description of the channel, for debugging.
- [let number: Int](wichannel/number.md)
  The channel number.
### Enumerations
- [WIChannel.Band](wichannel/band-swift.enum.md)
  The Wi-Fi band of a given channel.

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
- [struct WIMACAddress](wimacaddress.md)
  A Wi-Fi MAC Address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wichannel)*