# init()

**Framework**: Apple CryptoKit  
**Kind**: init  
**Required**: Yes

Creates a hash function.

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
init()
```

#### Discussion

Initialize a new hash function by calling this method if you want to hash the data iteratively, such as when you don’t have a buffer large enough to hold all the data at once. Provide data blocks to the hash function using the [`update(data:)`](hashfunction/update(data:).md) or [`update(bufferPointer:)`](hashfunction/update(bufferpointer:).md) method. After providing all the data, call [`finalize()`](hashfunction/finalize().md) to get the digest.

If your data fits into a single buffer, you can use the [`hash(data:)`](hashfunction/hash(data:).md) method instead to compute the digest in a single call.

## See Also

- [func update<D>(data: D)](hashfunction/update(data:).md)
  Incrementally updates the hash function with the given data.
- [func update(bufferPointer: UnsafeRawBufferPointer)](hashfunction/update(bufferpointer:).md)
  Incrementally updates the hash function with the contents of the buffer.
- [func finalize() -> Self.Digest](hashfunction/finalize.md)
  Finalizes the hash function and returns the computed digest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hashfunction/init())*