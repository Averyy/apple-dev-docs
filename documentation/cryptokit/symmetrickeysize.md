# SymmetricKeySize

**Framework**: Apple CryptoKit  
**Kind**: struct

The sizes that a symmetric cryptographic key can take.

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
struct SymmetricKeySize
```

#### Overview

When creating a new [`SymmetricKey`](symmetrickey.md) instance with a call to its [`init(size:)`](symmetrickey/init(size:).md) initializer, you typically use one of the standard key sizes, like [`bits128`](symmetrickeysize/bits128.md), [`bits192`](symmetrickeysize/bits192.md), or [`bits256`](symmetrickeysize/bits256.md). When you need a key with a non-standard length, use the [`init(bitCount:)`](symmetrickeysize/init(bitcount:).md) initializer to create a `SymmetricKeySize` instance with a custom bit count.

## Topics

### Using standard key lengths
- [static var bits128: SymmetricKeySize](symmetrickeysize/bits128.md)
  A size of 128 bits.
- [static var bits192: SymmetricKeySize](symmetrickeysize/bits192.md)
  A size of 192 bits.
- [static var bits256: SymmetricKeySize](symmetrickeysize/bits256.md)
  A size of 256 bits.
### Creating a nonstandard key length
- [init(bitCount: Int)](symmetrickeysize/init(bitcount:).md)
  Creates a new key size of the given length.
### Getting the length
- [let bitCount: Int](symmetrickeysize/bitcount.md)
  The number of bits in the key.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct HMAC](hmac.md)
  A hash-based message authentication algorithm.
- [struct SymmetricKey](symmetrickey.md)
  A symmetric cryptographic key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/symmetrickeysize)*