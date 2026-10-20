# allDescendants

**Framework**: USDKit  
**Kind**: property  
**Role**: Instance Property

All descendant prims of this stage’s pseudo-root.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var allDescendants: [USDPrim] { get }
```

## See Also

### Traversing the scene
- [var descendants: [USDPrim]](./descendants.md)
  The active, loaded, defined, non-abstract descendant prims of this stage’s pseudo-root.
- [func descendants(where: USDPrim.Predicate) -> [USDPrim]](./descendants%28where%29.md)
  Returns the descendant prims of this stage that satisfy the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/alldescendants)*