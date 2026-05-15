# isValidSignature(_:for:)

**Framework**: Apple CryptoKit  
**Kind**: method

Verifies an EdDSA signature over Curve25519.

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
func isValidSignature<S, D>(_ signature: S, for data: D) -> Bool where S : DataProtocol, D : DataProtocol
```

#### Return Value

A Boolean value that’s `true` when the signature is valid for the given data.

## Parameters

- `signature`: The signature to check against the given data.
- `data`: The data covered by the signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/curve25519/signing/publickey/isvalidsignature(_:for:))*