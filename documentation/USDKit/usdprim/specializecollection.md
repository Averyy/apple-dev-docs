# USDPrim.SpecializeCollection

**Framework**: USDKit  
**Kind**: struct

Manages specializes composition arcs on a prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SpecializeCollection
```

#### Overview

Specialization is similar to inheritance but with different composition strength. Specialized opinions are weaker than direct opinions but stronger than inherited opinions. Use `USDPrim.SpecializeCollection` to add, remove, and query specializes arcs on a prim.

## Topics

### Instance Properties
- [var prim: USDPrim](usdprim/specializecollection/prim.md)
  The prim that owns these specializes arcs.
### Instance Methods
- [func add(USDLayer.Path, position: USDPrim.ListPosition) throws](usdprim/specializecollection/add(_:position:).md)
  Adds a specializes arc to the prim.
- [func clear() throws](usdprim/specializecollection/clear.md)
  Removes all specializes arcs from the prim.
- [func remove(USDLayer.Path) throws](usdprim/specializecollection/remove(_:).md)
  Removes a specific specializes arc from the prim.
- [func set([USDLayer.Path]) throws](usdprim/specializecollection/set(_:).md)
  Replaces all specializes arcs with the specified list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/specializecollection)*