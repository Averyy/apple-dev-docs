# isPublic

**Framework**: Uniform Type Identifiers  
**Kind**: property

A Boolean value that indicates whether the type is in the public domain.

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
var isPublic: Bool { get }
```

#### Discussion

Types in the public domain have identifiers starting with `public`, and are generally defined by a standards body or by convention. Public types aren’t dynamic.

## See Also

- [var isDeclared: Bool](uttype-swift.struct/isdeclared.md)
  A Boolean value that indicates whether the system declares the type.
- [var isDynamic: Bool](uttype-swift.struct/isdynamic.md)
  A Boolean value that indicates whether the system generates the type.
- [var referenceURL: URL?](uttype-swift.struct/referenceurl.md)
  The reference URL for the type.
- [var version: Int?](uttype-swift.struct/version.md)
  The type’s version, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/ispublic)*