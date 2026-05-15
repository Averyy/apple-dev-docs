# signature(for:)

**Framework**: Apple CryptoKit  
**Kind**: method

Generates an elliptic curve digital signature algorithm (ECDSA) signature of the given data over the P-256 elliptic curve, using SHA-256 as the hash function.

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
func signature<D>(for data: D) throws -> P256.Signing.ECDSASignature where D : DataProtocol
```

#### Return Value

A cryptographic signature. The signing algorithm employs randomization to generate a different signature on every call, even for the same data and key.

## Parameters

- `data`: The data to sign.

## See Also

- [func signature<D>(for: D) throws -> P256.Signing.ECDSASignature](secureenclave/p256/signing/privatekey/signature(for:)-3xogs.md)
  Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-256 elliptic curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/p256/signing/privatekey/signature(for:)-76j0u)*