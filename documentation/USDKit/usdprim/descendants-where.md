# descendants(where:)

**Framework**: USDKit  
**Kind**: method

Returns the descendant prims of this prim that satisfy the given predicate.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func descendants(where predicate: USDPrim.Predicate) -> [USDPrim]
```

## See Also

- [var children: [USDPrim]](usdprim/children.md)
  The active, loaded, defined, non-abstract child prims of this prim.
- [var allChildren: [USDPrim]](usdprim/allchildren.md)
  The child prims of this prim.
- [var descendants: [USDPrim]](usdprim/descendants.md)
  The active, loaded, defined, non-abstract descendant prims of this prim, in depth-first order.
- [var allDescendants: [USDPrim]](usdprim/alldescendants.md)
  The descendant prims of this prim.
- [var nextSibling: USDPrim?](usdprim/nextsibling.md)
  The active, loaded, defined, non-abstract successor of this prim in its parent’s list of children.
- [func children(where: USDPrim.Predicate) -> [USDPrim]](usdprim/children(where:).md)
  Returns the child prims of this prim that satisfy the given predicate.
- [func nextSibling(where: USDPrim.Predicate) -> USDPrim](usdprim/nextsibling(where:).md)
  The successor of this prim in its parent’s list of children that satisfies the given predicate.
- [func prim(at: USDLayer.Path) -> USDPrim](usdprim/prim(at:).md)
  Returns the prim at a given path, relative to this prim.
- [USDPrim.Predicate](usdprim/predicate.md)
  A filter which returns true or false for prims based on their flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/descendants(where:))*