# init(combined:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a sealed box from the given data.

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
init<D>(combined: D) throws where D : DataProtocol
```

## Parameters

- `combined`: The combined bytes of the tag and ciphertext.

## See Also

- [init<C, T>(nonce: ChaChaPoly.Nonce, ciphertext: C, tag: T) throws](chachapoly/sealedbox/init(nonce:ciphertext:tag:).md)
  Creates a sealed box from the given tag, nonce, and ciphertext.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/chachapoly/sealedbox/init(combined:))*