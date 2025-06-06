# supertypes

**Framework**: Uniform Type Identifiers  
**Kind**: property

The set of types the type directly or indirectly conforms to.

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
var supertypes: Set<UTType> { get }
```

## See Also

- [func conforms(to: UTType) -> Bool](uttype-swift.struct/conforms(to:).md)
  Returns a Boolean value that indicates whether a type conforms to the type.
- [func isSubtype(of: UTType) -> Bool](uttype-swift.struct/issubtype(of:).md)
  Returns a Boolean value that indicates whether a type is higher in a hierarchy than the type.
- [func isSupertype(of: UTType) -> Bool](uttype-swift.struct/issupertype(of:).md)
  Returns a Boolean value that indicates whether a type is lower in a hierarchy than the type.
- [Navigating Hierarchical Data Using Outline and Split Views](../AppKit/navigating-hierarchical-data-using-outline-and-split-views.md)
  Build a structured user interface that simplifies navigation in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/supertypes)*