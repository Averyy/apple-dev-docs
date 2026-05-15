# HPKE.AEAD.exportOnly

**Framework**: Apple CryptoKit  
**Kind**: case

An export-only mode.

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
case exportOnly
```

#### Discussion

In export-only mode, HPKE negotiates key derivation, but you can’t use it to encrypt or decrypt data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/aead/exportonly)*