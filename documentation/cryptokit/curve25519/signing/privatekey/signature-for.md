# signature(for:)

**Framework**: Apple CryptoKit  
**Kind**: method

Generates an EdDSA signature over Curve25519.

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
func signature<D>(for data: D) throws -> Data where D : DataProtocol
```

#### Return Value

The signature for the data. Although not required by [`RFC 8032`](https://developer.apple.comhttps://tools.ietf.org/html/rfc8032), which describes the Edwards-Curve Digital Signature Algorithm (EdDSA), the CryptoKit implementation of the algorithm employs randomization to generate a different signature on every call, even for the same data and key, to guard against side-channel attacks.

## Parameters

- `data`: The data to sign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/curve25519/signing/privatekey/signature(for:))*