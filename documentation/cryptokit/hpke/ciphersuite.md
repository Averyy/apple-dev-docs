# HPKE.Ciphersuite

**Framework**: Apple CryptoKit  
**Kind**: struct

Cipher suites to use in hybrid public key encryption (HPKE).

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
struct Ciphersuite
```

#### Overview

HPKE cipher suites identify the authenticated encryption with additional data (AEAD) algorithm for encrypting and decrypting messages, the key derivation function (KDF) for deriving the shared key, and the key encapsulation mechanism (KEM) for sharing the symmetric key. The sender and recipient of encrypted messages need to use the same cipher suite.

## Topics

### Using post-quantum cipher suites
- [static let XWingMLKEM768X25519_SHA256_AES_GCM_256: HPKE.Ciphersuite](hpke/ciphersuite/xwingmlkem768x25519_sha256_aes_gcm_256.md)
  A cipher suite for HPKE that uses the X-Wing KEM (ML-KEM-768 with X25519), SHA-2 key derivation with a 256-bit digest, and the Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.
### Using elliptic curve cipher suites
- [static let Curve25519_SHA256_ChachaPoly: HPKE.Ciphersuite](hpke/ciphersuite/curve25519_sha256_chachapoly.md)
  A cipher suite for HPKE that uses X25519 elliptic curve key agreement, SHA-2 key derivation with a 256-bit digest, and the ChaCha20 stream cipher with the Poly1305 message authentication code.
- [static let P256_SHA256_AES_GCM_256: HPKE.Ciphersuite](hpke/ciphersuite/p256_sha256_aes_gcm_256.md)
  A cipher suite for HPKE that uses NIST P-256 elliptic curve key agreement, SHA-2 key derivation with a 256-bit digest, and the Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.
- [static let P384_SHA384_AES_GCM_256: HPKE.Ciphersuite](hpke/ciphersuite/p384_sha384_aes_gcm_256.md)
  A cipher suite that you use for HPKE using NIST P-384 elliptic curve key agreement, SHA-2 key derivation with a 384-bit digest, and the Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.
- [static let P521_SHA512_AES_GCM_256: HPKE.Ciphersuite](hpke/ciphersuite/p521_sha512_aes_gcm_256.md)
  A cipher suite for HPKE that uses NIST P-521 elliptic curve key agreement, SHA-2 key derivation with a 512-bit digest, and the Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.
### Creating a cipher suite
- [init(kem: HPKE.KEM, kdf: HPKE.KDF, aead: HPKE.AEAD)](hpke/ciphersuite/init(kem:kdf:aead:).md)
  Creates an HPKE cipher suite.
### Inspecting a cipher suite
- [let aead: HPKE.AEAD](hpke/ciphersuite/aead.md)
  The authenticated encryption with additional data (AEAD) algorithm for encrypting and decrypting messages.
- [let kdf: HPKE.KDF](hpke/ciphersuite/kdf.md)
  The key derivation function (KDF) for deriving the symmetric key.
- [let kem: HPKE.KEM](hpke/ciphersuite/kem.md)
  The key encapsulation mechanism (KEM) for encapsulating the symmetric key.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [HPKE.AEAD](hpke/aead.md)
  The authenticated encryption with associated data (AEAD) algorithms to use in HPKE.
- [HPKE.KDF](hpke/kdf.md)
  The key derivation functions to use in HPKE.
- [HPKE.KEM](hpke/kem.md)
  The key encapsulation mechanisms to use in HPKE.
- [HPKE.DHKEM](hpke/dhkem.md)
  A container for Diffie-Hellman key encapsulation mechanisms (KEMs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/ciphersuite)*