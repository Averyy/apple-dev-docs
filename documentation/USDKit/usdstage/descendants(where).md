# descendants(where:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Returns the descendant prims of this stage that satisfy the given predicate.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func descendants(where predicate: USDPrim.Predicate) -> [USDPrim]
```

## See Also

### Traversing the scene
- [var descendants: [USDPrim]](./descendants.md)
  The active, loaded, defined, non-abstract descendant prims of this stage’s pseudo-root.
- [var allDescendants: [USDPrim]](./alldescendants.md)
  All descendant prims of this stage’s pseudo-root.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/descendants(where:))*