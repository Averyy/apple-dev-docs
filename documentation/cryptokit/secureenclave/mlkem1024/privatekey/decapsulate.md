# decapsulate(_:)

**Framework**: Apple CryptoKit  
**Kind**: method

Decapsulates the encapsulated shared secret

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func decapsulate<D>(_ encapsulated: D) throws -> SymmetricKey where D : DataProtocol
```

#### Return Value

The decapsulated shared secret

## Parameters

- `encapsulated`: The encapsulated shared secret


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem1024/privatekey/decapsulate(_:))*