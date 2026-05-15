# combined

**Framework**: Apple CryptoKit  
**Kind**: property

A combined element composed of the tag, the nonce, and the ciphertext.

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
let combined: Data
```

#### Discussion

The data layout of the combined representation is: nonce, ciphertext, then tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/chachapoly/sealedbox/combined)*