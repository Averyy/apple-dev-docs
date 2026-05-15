# finalize()

**Framework**: Apple CryptoKit  
**Kind**: method

Finalizes the hash function and returns the computed digest.

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
func finalize() -> SHA3_256.Digest
```

#### Return Value

The computed digest of the data.

#### Discussion

Call this method after you provide the hash function with all the data to hash by making one or more calls to the `update(data:)` or [`update(bufferPointer:)`](sha3_256/update(bufferpointer:).md) method. After finalizing the hash function, discard it. To compute a new digest, create a new hash function with a call to the [`init()`](sha3_256/init().md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/sha3_256/finalize())*