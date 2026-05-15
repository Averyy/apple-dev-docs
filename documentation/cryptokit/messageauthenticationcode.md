# MessageAuthenticationCode

**Framework**: Apple CryptoKit  
**Kind**: protocol

A type that represents a message authentication code.

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
@preconcurrency
protocol MessageAuthenticationCode : ContiguousBytes, CustomStringConvertible, Hashable, Sendable, Sequence where Self.Element == UInt8
```

## Topics

### Retrieving the code length
- [var byteCount: Int](messageauthenticationcode/bytecount.md)
  The number of bytes in the message authentication code.
### Comparing codes
- [static func == <D>(Self, D) -> Bool](messageauthenticationcode/==(_:_:)-3rxc4.md)
  Returns a Boolean value indicating whether a message authentication code is equivalent to a collection of binary data.
- [static func == (Self, Self) -> Bool](messageauthenticationcode/==(_:_:)-b90.md)
  Returns a Boolean value indicating whether two message authentication codes are equal.
### Default Implementations
- [CustomStringConvertible Implementations](messageauthenticationcode/customstringconvertible-implementations.md)

## Relationships

### Inherits From
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)
### Conforming Types
- [HashedAuthenticationCode](hashedauthenticationcode.md)

## See Also

- [typealias MAC](hmac/mac.md)
  An alias for a hash-based message authentication code.
- [struct HashedAuthenticationCode](hashedauthenticationcode.md)
  A hash-based message authentication code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/messageauthenticationcode)*