# allChildren

**Framework**: USDKit  
**Kind**: property  
**Role**: Instance Property

The child prims of this prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var allChildren: [USDPrim] { get }
```

## See Also

### Traversing the hierarchy
- [var children: [USDPrim]](./children.md)
  The active, loaded, defined, non-abstract child prims of this prim.
- [var descendants: [USDPrim]](./descendants.md)
  The active, loaded, defined, non-abstract descendant prims of this prim, in depth-first order.
- [var allDescendants: [USDPrim]](./alldescendants.md)
  The descendant prims of this prim.
- [var nextSibling: USDPrim?](./nextsibling.md)
  The active, loaded, defined, non-abstract successor of this prim in its parent’s list of children.
- [func children(where: USDPrim.Predicate) -> [USDPrim]](./children%28where%29.md)
  Returns the child prims of this prim that satisfy the given predicate.
- [func descendants(where: USDPrim.Predicate) -> [USDPrim]](./descendants%28where%29.md)
  Returns the descendant prims of this prim that satisfy the given predicate.
- [func nextSibling(where: USDPrim.Predicate) -> USDPrim](./nextsibling%28where%29.md)
  The successor of this prim in its parent’s list of children that satisfies the given predicate.
- [func prim(at: USDLayer.Path) -> USDPrim](./prim%28at%29.md)
  Returns the prim at a given path, relative to this prim.
- [USDPrim.Predicate](./predicate.md)
  A filter which returns true or false for prims based on their flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/allchildren)*