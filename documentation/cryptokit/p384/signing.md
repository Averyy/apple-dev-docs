# P384.Signing

**Framework**: Apple CryptoKit  
**Kind**: enum

A mechanism used to create or verify a cryptographic signature using the NIST P-384 elliptic curve digital signature algorithm (ECDSA).

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
- [P384.Signing.PrivateKey](p384/signing/privatekey.md)
  A P-384 private key used to create cryptographic signatures.
- [P384.Signing.PublicKey](p384/signing/publickey.md)
  A P-384 public key used to verify cryptographic signatures.
### Structures
- [P384.Signing.ECDSASignature](p384/signing/ecdsasignature.md)
  A P-384 elliptic curve digital signature algorithm (ECDSA) signature.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [P384.KeyAgreement](p384/keyagreement.md)
  A mechanism used to create a shared secret between two users by performing NIST P-384 elliptic curve Diffie Hellman (ECDH) key exchange.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p384/signing)*