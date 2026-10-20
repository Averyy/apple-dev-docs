# USDPrim.ReferenceCollection

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Manages reference composition arcs on a prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ReferenceCollection
```

## Topics

### Instance Properties
- [var prim: USDPrim](./referencecollection/prim.md)
  The prim that owns these reference arcs.
### Instance Methods
- [func add(USDPrim.Reference, position: USDPrim.ListPosition) throws](./referencecollection/add%28_,position%29.md)
  Adds an existing reference arc to the prim.
- [func add(to: USDLayer.Path?, from: String, layerOffset: USDLayer.TimeOffset, position: USDPrim.ListPosition) throws](./referencecollection/add%28to,from,layeroffset,position%29.md)
  Adds an external reference arc.
- [func add(to: USDLayer.Path, layerOffset: USDLayer.TimeOffset, position: USDPrim.ListPosition) throws](./referencecollection/add%28to,layeroffset,position%29.md)
  Adds an internal reference arc that targets a prim in the same layer stack.
- [func clear() throws](./referencecollection/clear%28%29.md)
  Removes all reference arcs from the prim.
- [func remove(USDPrim.Reference) throws](./referencecollection/remove%28_%29.md)
  Removes a specific reference arc from the prim.
- [func set([USDPrim.Reference]) throws](./referencecollection/set%28_%29.md)
  Replaces all reference arcs with the specified list.

## See Also

### Composing references and payloads
- [var references: USDPrim.ReferenceCollection](./references.md)
  The reference composition arcs on this prim.
- [USDPrim.Reference](./reference.md)
  A reference to an external layer or asset.
- [USDPrim.Payload](./payload.md)
  A payload to an external asset.
- [USDPrim.ListPosition](./listposition.md)
  Where a new composition arc should be inserted relative to existing arcs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/referencecollection)*