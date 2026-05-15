# KEMPublicKey

**Framework**: Apple CryptoKit  
**Kind**: protocol

The public key for a key encapsulation mechanism.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@preconcurrency
protocol KEMPublicKey : Sendable
```

## Topics

### Instance Methods
- [func encapsulate() throws -> KEM.EncapsulationResult](kempublickey/encapsulate.md)
  Generates and encapsulates a shared secret.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [HPKEKEMPublicKey](hpkekempublickey.md)
### Conforming Types
- [MLKEM1024.PublicKey](mlkem1024/publickey.md)
- [MLKEM768.PublicKey](mlkem768/publickey.md)
- [XWingMLKEM768X25519.PublicKey](xwingmlkem768x25519/publickey.md)

## See Also

- [protocol KEMPrivateKey](kemprivatekey.md)
  The private key for a key encapsulation mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/kempublickey)*