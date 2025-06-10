# referenceURL

**Framework**: Uniform Type Identifiers  
**Kind**: property

The reference URL for the type.

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
var referenceURL: URL? { get }
```

#### Discussion

A reference URL is a human-readable document that describes a type. Most types don’t specify reference URLs.

> ⚠️ **Warning**:  The system doesn’t validate the URL, nor does it guarantee its scheme or structure.

## See Also

- [var isDeclared: Bool](uttype-swift.struct/isdeclared.md)
  A Boolean value that indicates whether the system declares the type.
- [var isDynamic: Bool](uttype-swift.struct/isdynamic.md)
  A Boolean value that indicates whether the system generates the type.
- [var isPublic: Bool](uttype-swift.struct/ispublic.md)
  A Boolean value that indicates whether the type is in the public domain.
- [var version: Int?](uttype-swift.struct/version.md)
  The type’s version, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/referenceurl)*