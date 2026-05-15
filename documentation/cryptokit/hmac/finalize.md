# finalize()

**Framework**: Apple CryptoKit  
**Kind**: method

Finalizes the message authentication computation and returns the computed code.

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
func finalize() -> HMAC<H>.MAC
```

#### Return Value

The message authentication code.

## See Also

- [init(key: SymmetricKey)](hmac/init(key:).md)
  Creates a message authentication code generator.
- [func update<D>(data: D)](hmac/update(data:).md)
  Updates the message authentication code computation with a block of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hmac/finalize())*