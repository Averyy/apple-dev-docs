# USDPrim.ReferenceCollection

**Framework**: USDKit  
**Kind**: struct

Manages reference composition arcs on a prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ReferenceCollection
```

## Topics

### Instance Properties
- [var prim: USDPrim](usdprim/referencecollection/prim.md)
  The prim that owns these reference arcs.
### Instance Methods
- [func add(USDPrim.Reference, position: USDPrim.ListPosition) throws](usdprim/referencecollection/add(_:position:).md)
  Adds an existing reference arc to the prim.
- [func add(to: USDLayer.Path?, from: String, layerOffset: USDLayer.TimeOffset, position: USDPrim.ListPosition) throws](usdprim/referencecollection/add(to:from:layeroffset:position:).md)
  Adds an external reference arc.
- [func add(to: USDLayer.Path, layerOffset: USDLayer.TimeOffset, position: USDPrim.ListPosition) throws](usdprim/referencecollection/add(to:layeroffset:position:).md)
  Adds an internal reference arc that targets a prim in the same layer stack.
- [func clear() throws](usdprim/referencecollection/clear.md)
  Removes all reference arcs from the prim.
- [func remove(USDPrim.Reference) throws](usdprim/referencecollection/remove(_:).md)
  Removes a specific reference arc from the prim.
- [func set([USDPrim.Reference]) throws](usdprim/referencecollection/set(_:).md)
  Replaces all reference arcs with the specified list.

## See Also

- [var references: USDPrim.ReferenceCollection](usdprim/references.md)
  The reference composition arcs on this prim.
- [USDPrim.Reference](usdprim/reference.md)
  A reference to an external layer or asset.
- [USDPrim.Payload](usdprim/payload.md)
  A payload to an external asset.
- [USDPrim.ListPosition](usdprim/listposition.md)
  Where a new composition arc should be inserted relative to existing arcs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/referencecollection)*