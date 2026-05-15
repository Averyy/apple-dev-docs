# init(key:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a message authentication code generator.

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
init(key: SymmetricKey)
```

## Parameters

- `key`: The symmetric key used to secure the computation.

## See Also

- [func update<D>(data: D)](hmac/update(data:).md)
  Updates the message authentication code computation with a block of data.
- [func finalize() -> HMAC<H>.MAC](hmac/finalize.md)
  Finalizes the message authentication computation and returns the computed code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hmac/init(key:))*