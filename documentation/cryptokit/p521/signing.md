# P521.Signing

**Framework**: Apple CryptoKit  
**Kind**: enum

A mechanism used to create or verify a cryptographic signature using the NIST P-521 elliptic curve digital signature algorithm (ECDSA).

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
enum Signing
```

## Topics

### Using keys
- [P521.Signing.PrivateKey](p521/signing/privatekey.md)
  A P-521 private key used to create cryptographic signatures.
- [P521.Signing.PublicKey](p521/signing/publickey.md)
  A P-521 public key used to verify cryptographic signatures.
### Structures
- [P521.Signing.ECDSASignature](p521/signing/ecdsasignature.md)
  A P-521 elliptic curve digital signature algorithm (ECDSA) signature.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [P521.KeyAgreement](p521/keyagreement.md)
  A mechanism used to create a shared secret between two users by performing NIST P-521 elliptic curve Diffie Hellman (ECDH) key exchange.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/signing)*