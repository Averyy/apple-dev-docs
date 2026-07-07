# USDPrim.InheritCollection

**Framework**: USDKit  
**Kind**: struct

Manages inherit composition arcs on a prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct InheritCollection
```

#### Overview

Inheritance allows a prim to inherit opinions from another prim within the same layer stack, similar to class inheritance in object-oriented programming. Use `USDPrim.InheritCollection` to add, remove, and query inherit arcs on a prim.

## Topics

### Instance Properties
- [var inheritedPaths: [USDLayer.Path]](usdprim/inheritcollection/inheritedpaths.md)
  All paths this prim inherits from, including paths inherited transitively through inherited classes.
- [var prim: USDPrim](usdprim/inheritcollection/prim.md)
  The prim that owns these inherit arcs.
### Instance Methods
- [func add(USDLayer.Path, position: USDPrim.ListPosition) throws](usdprim/inheritcollection/add(_:position:).md)
  Adds an inherit arc to the prim.
- [func clear() throws](usdprim/inheritcollection/clear.md)
  Removes all inherit arcs from the prim.
- [func remove(USDLayer.Path) throws](usdprim/inheritcollection/remove(_:).md)
  Removes a specific inherit arc from the prim.
- [func set([USDLayer.Path]) throws](usdprim/inheritcollection/set(_:).md)
  Replaces all inherit arcs with the specified list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/inheritcollection)*