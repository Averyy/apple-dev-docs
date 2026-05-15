# wrap(_:using:)

**Framework**: Apple CryptoKit  
**Kind**: method

Wraps a key using the AES wrap algorithm.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func wrap(_ keyToWrap: SymmetricKey, using kek: SymmetricKey) throws -> Data
```

#### Return Value

The wrapped key.

#### Discussion

Wrap is an implementation of the AES key wrap algorithm as specified in IETF RFC 3394.

## Parameters

- `keyToWrap`: The key to wrap.
- `kek`: The key encryption key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/keywrap/wrap(_:using:))*