# init()

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a SHA3-512 hash function.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 2.0+
- watchOS 26.0+

## Declaration

```swift
init()
```

#### Discussion

Initialize a new hash function by calling this method if you want to hash data iteratively, such as when you don’t have a buffer large enough to hold all the data at once. Provide data blocks to the hash function using the `update(data:)` or [`update(bufferPointer:)`](sha3_512/update(bufferpointer:).md) method. After providing all the data, call [`finalize()`](sha3_512/finalize().md) to get the digest.

If your data fits into a single buffer, you can use the `hash(data:)` method instead, to compute the digest in a single call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/sha3_512/init())*