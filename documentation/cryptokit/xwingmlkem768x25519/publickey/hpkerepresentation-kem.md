# hpkeRepresentation(kem:)

**Framework**: Apple CryptoKit  
**Kind**: method

Creates a serialized representation of the public key.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func hpkeRepresentation(kem: HPKE.KEM) throws -> Data
```

#### Return Value

The serialized representation of the public key.

#### Discussion

- kem: The Key Encapsulation Mechanism to use with the public key.

> **Note**: [`HPKE.Errors.inconsistentCiphersuiteAndKey`](hpke/errors/inconsistentciphersuiteandkey.md) if the key encapsulation mechanism requested is incompatible with this public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/publickey/hpkerepresentation(kem:))*