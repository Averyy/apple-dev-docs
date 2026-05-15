# HPKEKEMPublicKey

**Framework**: Apple CryptoKit  
**Kind**: protocol

A type that represents the public key in HPKE

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 1.0+
- watchOS 26.0+

## Declaration

```swift
@preconcurrency
protocol HPKEKEMPublicKey : HPKEPublicKeySerialization, KEMPublicKey
```

## Topics

### Associated Types
- [associatedtype EphemeralPrivateKey : HPKEKEMPrivateKeyGeneration](hpkekempublickey/ephemeralprivatekey.md)
  The type of the ephemeral private key.

## Relationships

### Inherits From
- [HPKEPublicKeySerialization](hpkepublickeyserialization.md)
- [KEMPublicKey](kempublickey.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [XWingMLKEM768X25519.PublicKey](xwingmlkem768x25519/publickey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpkekempublickey)*