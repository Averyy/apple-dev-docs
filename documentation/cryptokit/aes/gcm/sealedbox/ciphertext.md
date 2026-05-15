# ciphertext

**Framework**: Apple CryptoKit  
**Kind**: property

The encrypted data.

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
var ciphertext: Data { get }
```

#### Discussion

The length of the ciphertext of a sealed box is the same as the length of the plaintext you encrypt.

## See Also

- [var nonce: AES.GCM.Nonce](aes/gcm/sealedbox/nonce.md)
  The nonce used to encrypt the data.
- [var tag: Data](aes/gcm/sealedbox/tag.md)
  An authentication tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm/sealedbox/ciphertext)*