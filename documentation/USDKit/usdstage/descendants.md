# descendants

**Framework**: USDKit  
**Kind**: property

The active, loaded, defined, non-abstract descendant prims of this stage’s pseudo-root.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var descendants: [USDPrim] { get }
```

## See Also

- [func descendants(where: USDPrim.Predicate) -> [USDPrim]](usdstage/descendants(where:).md)
  Returns the descendant prims of this stage that satisfy the given predicate.
- [var allDescendants: [USDPrim]](usdstage/alldescendants.md)
  All descendant prims of this stage’s pseudo-root.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/descendants)*