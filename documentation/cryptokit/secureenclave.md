# SecureEnclave

**Framework**: Apple CryptoKit  
**Kind**: enum

A representation of a device’s hardware-based key manager.

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
enum SecureEnclave
```

## Topics

### Checking availability
- [static var isAvailable: Bool](secureenclave/isavailable.md)
  A Boolean value that indicates if the device supports Secure Enclave access.
### Using the secure enclave
- [SecureEnclave.P256](secureenclave/p256.md)
  An elliptic curve that enables NIST P-256 signatures and key agreement within the Secure Enclave.
- [SecureEnclave.MLKEM1024](secureenclave/mlkem1024.md)
  An implementation of the MLKEM1024 key encapsulation mechanism that operates within the Secure Enclave.
- [SecureEnclave.MLKEM768](secureenclave/mlkem768.md)
  An implementation of the MLKEM768 key encapsulation mechanism that operates within the Secure Enclave.
### Enumerations
- [SecureEnclave.MLDSA65](secureenclave/mldsa65.md)
- [SecureEnclave.MLDSA87](secureenclave/mldsa87.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum Curve25519](curve25519.md)
  An elliptic curve that enables X25519 key agreement and Ed25519 signatures.
- [enum P521](p521.md)
  An elliptic curve that enables NIST P-521 signatures and key agreement.
- [enum P384](p384.md)
  An elliptic curve that enables NIST P-384 signatures and key agreement.
- [enum P256](p256.md)
  An elliptic curve that enables NIST P-256 signatures and key agreement.
- [struct SharedSecret](sharedsecret.md)
  A key agreement result from which you can derive a symmetric cryptographic key.
- [enum HPKE](hpke.md)
  A container for hybrid public key encryption (HPKE) operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave)*