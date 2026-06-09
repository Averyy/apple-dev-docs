# WAConnection

**Framework**: Wi-Fi Aware  
**Kind**: class

Provides access to the Wi-Fi Aware-specific configuration and information that underlies a given `Network/NetworkConnection`.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
class WAConnection<ApplicationProtocol> where ApplicationProtocol : NetworkProtocolOptions
```

## Topics

### Instance Methods
- [func deriveSharedSecret(for: WASharedSecret.ProtocolName, method: WASharedSecret.DerivationMethod, context: WASharedSecret.Context) async -> WASharedSecret?](waconnection/derivesharedsecret(for:method:context:).md)
  Derive a unique, high-entropy shared secret for this network connection, which can be used to pair and setup security for higher layer network protocols like TLS or IPSec without additional user action or entropy input.

## See Also

- [struct WAEndpoint](waendpoint.md)
  The endpoint of a Wi-Fi Aware connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waconnection)*