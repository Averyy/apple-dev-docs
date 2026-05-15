# Curve25519.Signing.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct

A Curve25519 public key used to verify cryptographic signatures.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct PublicKey
```

## Topics

### Creating a public key
- [init<D>(rawRepresentation: D) throws](curve25519/signing/publickey/init(rawrepresentation:).md)
  Creates a Curve25519 public key from a data representation.
### Representing the key
- [var rawRepresentation: Data](curve25519/signing/publickey/rawrepresentation.md)
  A representation of the public key.
### Verifying a signature
- [func isValidSignature<S, D>(S, for: D) -> Bool](curve25519/signing/publickey/isvalidsignature(_:for:).md)
  Verifies an EdDSA signature over Curve25519.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Curve25519.Signing.PrivateKey](curve25519/signing/privatekey.md)
  A Curve25519 private key used to create cryptographic signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/curve25519/signing/publickey)*