# update(data:)

**Framework**: Apple CryptoKit  
**Kind**: method

Updates the message authentication code computation with a block of data.

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
mutating func update<D>(data: D) where D : DataProtocol
```

## Parameters

- `data`: The data for which to compute the authentication code.

## See Also

- [init(key: SymmetricKey)](hmac/init(key:).md)
  Creates a message authentication code generator.
- [func finalize() -> HMAC<H>.MAC](hmac/finalize.md)
  Finalizes the message authentication computation and returns the computed code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hmac/update(data:))*