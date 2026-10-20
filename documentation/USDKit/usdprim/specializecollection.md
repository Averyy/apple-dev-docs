# USDPrim.SpecializeCollection

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Manages specializes composition arcs on a prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct SpecializeCollection
```

#### Overview

Specialization is similar to inheritance but with different composition strength. Specialized opinions are weaker than direct opinions but stronger than inherited opinions. Use `USDPrim.SpecializeCollection` to add, remove, and query specializes arcs on a prim.

## Topics

### Instance Properties
- [var prim: USDPrim](./specializecollection/prim.md)
  The prim that owns these specializes arcs.
### Instance Methods
- [func add(USDLayer.Path, position: USDPrim.ListPosition) throws](./specializecollection/add%28_,position%29.md)
  Adds a specializes arc to the prim.
- [func clear() throws](./specializecollection/clear%28%29.md)
  Removes all specializes arcs from the prim.
- [func remove(USDLayer.Path) throws](./specializecollection/remove%28_%29.md)
  Removes a specific specializes arc from the prim.
- [func set([USDLayer.Path]) throws](./specializecollection/set%28_%29.md)
  Replaces all specializes arcs with the specified list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/specializecollection)*