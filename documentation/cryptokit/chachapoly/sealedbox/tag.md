# tag

**Framework**: Apple CryptoKit  
**Kind**: property

An authentication tag.

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
var tag: Data { get }
```

#### Discussion

The authentication tag has a length of 16 bytes.

## See Also

- [var nonce: ChaChaPoly.Nonce](chachapoly/sealedbox/nonce.md)
  The nonce used to encrypt the data.
- [var ciphertext: Data](chachapoly/sealedbox/ciphertext.md)
  The encrypted data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/chachapoly/sealedbox/tag)*