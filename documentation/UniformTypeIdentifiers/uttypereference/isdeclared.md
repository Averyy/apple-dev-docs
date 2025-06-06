# isDeclared

**Framework**: Uniform Type Identifiers  
**Kind**: property

A Boolean value that indicates whether the system declares the type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var isDeclared: Bool { get }
```

#### Discussion

The system either declares a type or dynamically generates a type, but not both.

## See Also

- [var isDynamic: Bool](uttypereference/isdynamic.md)
  A Boolean value that indicates whether the system generates the type.
- [var isPublic: Bool](uttypereference/ispublic.md)
  A Boolean value that indicates whether the type is in the public domain.
- [var referenceURL: URL?](uttype-swift.struct/referenceurl.md)
  The reference URL for the type.
- [var version: Int?](uttype-swift.struct/version.md)
  The type’s version, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/isdeclared)*