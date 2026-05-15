# sharedSecretFromKeyAgreement(with:)

**Framework**: Apple CryptoKit  
**Kind**: method  
**Required**: Yes

Performs a Diffie-Hellman Key Agreement.

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
func sharedSecretFromKeyAgreement(with publicKeyShare: Self.PublicKey) throws -> SharedSecret
```

#### Return Value

The resulting key agreement result.

## Parameters

- `publicKeyShare`: The public key share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/diffiehellmankeyagreement/sharedsecretfromkeyagreement(with:))*