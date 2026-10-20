# USDPrim.InheritCollection

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Manages inherit composition arcs on a prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct InheritCollection
```

#### Overview

Inheritance allows a prim to inherit opinions from another prim within the same layer stack, similar to class inheritance in object-oriented programming. Use `USDPrim.InheritCollection` to add, remove, and query inherit arcs on a prim.

## Topics

### Instance Properties
- [var inheritedPaths: [USDLayer.Path]](./inheritcollection/inheritedpaths.md)
  All paths this prim inherits from, including paths inherited transitively through inherited classes.
- [var prim: USDPrim](./inheritcollection/prim.md)
  The prim that owns these inherit arcs.
### Instance Methods
- [func add(USDLayer.Path, position: USDPrim.ListPosition) throws](./inheritcollection/add%28_,position%29.md)
  Adds an inherit arc to the prim.
- [func clear() throws](./inheritcollection/clear%28%29.md)
  Removes all inherit arcs from the prim.
- [func remove(USDLayer.Path) throws](./inheritcollection/remove%28_%29.md)
  Removes a specific inherit arc from the prim.
- [func set([USDLayer.Path]) throws](./inheritcollection/set%28_%29.md)
  Replaces all inherit arcs with the specified list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/inheritcollection)*