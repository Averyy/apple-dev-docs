# USDPrim.PayloadCollection

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Manages payload composition arcs on a prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct PayloadCollection
```

## Topics

### Instance Properties
- [var prim: USDPrim](./payloadcollection/prim.md)
  The prim that owns these payload arcs.
### Instance Methods
- [func add(USDPrim.Payload, position: USDPrim.ListPosition) throws](./payloadcollection/add%28_,position%29.md)
  Adds an existing payload arc to the prim.
- [func add(to: USDLayer.Path?, from: String, layerOffset: USDLayer.TimeOffset, position: USDPrim.ListPosition) throws](./payloadcollection/add%28to,from,layeroffset,position%29.md)
  Adds an external payload arc.
- [func add(to: USDLayer.Path, layerOffset: USDLayer.TimeOffset, position: USDPrim.ListPosition) throws](./payloadcollection/add%28to,layeroffset,position%29.md)
  Adds an internal payload arc that targets a prim in the same layer stack.
- [func clear() throws](./payloadcollection/clear%28%29.md)
  Removes all payload arcs from the prim.
- [func remove(USDPrim.Payload) throws](./payloadcollection/remove%28_%29.md)
  Removes a specific payload arc from the prim.
- [func set([USDPrim.Payload]) throws](./payloadcollection/set%28_%29.md)
  Replaces all payload arcs with the specified list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/payloadcollection)*