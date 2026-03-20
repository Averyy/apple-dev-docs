# WASharedSecret

**Framework**: Wi-Fi Aware  
**Kind**: struct

A high-entropy shared secret unique to this network connection.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct WASharedSecret
```

#### Discussion

Use a `WASharedSecret` to pair and set up security for higher layer network protocols such as TLS, QUIC, or IPSec without requiring manual action or data entry by someone using these capabilities. The framework can use the shared secret to authenticate a *password authenticated key agreement* ([`PAKE`](https://developer.apple.comhttps://en.wikipedia.org/wiki/Password-authenticated_key_agreement)) like SPAKE2, which it then uses to pair and derive long-term asymmetric keys for authentication and encryption of the upper-layer network protocol.

Both sides of a connection derive the same shared secret value if the same connection and input parameters are used:

- Your app and a remote app can derive the same shared secret value by calling the [`deriveSharedSecret(for:method:context:)`](WAConnection/deriveSharedSecret(for:method:context:).md) function on the same connection, with the same parameters.
- Devices and accessories can derive the same value as your app by using the derivation specified in the Wi-Fi Aware 5.0 standard, and providing the same parameters your app uses.

The following example shows how to generate a shared secret:

```swift
let secret = await connection.wifiAware?.deriveSharedSecret(for: .tlsPSK, method: .kdfHash256)
```

> ❗ **Important**: If needed, get a new shared secret for each new network connection. Don’t save this value, send it to other devices, reuse it across connections, or use it as a long-term authentication or encryption key. Instead, use this to pair higher layer protocols, and derive unique longer term asymmetric keys for those protocols when pairing them.

## Topics

### Structures
- [WASharedSecret.Context](washaredsecret/context.md)
  A unique value that is specific to your App and the use case a given connection will perform, which diversifies the generated secret so that it is unique to your App and connection.
- [WASharedSecret.DerivationMethod](washaredsecret/derivationmethod.md)
  An enumeration of methods that can be used to derive a shared secret, as specified in the Wi-Fi Aware standard.
- [WASharedSecret.ProtocolName](washaredsecret/protocolname.md)
  An object that uniquely identifies a particular network protocol and the pairing hanshake it uses for authentication.
### Instance Properties
- [let data: Data](washaredsecret/data.md)
  The secret data that is derived by both this device and the remote device for this connection.
- [let derivation: WASharedSecret.DerivationMethod](washaredsecret/derivation.md)
  The method used to derive the shared secret on both sides of the connection, as per the Wi-Fi Aware standard.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/washaredsecret)*