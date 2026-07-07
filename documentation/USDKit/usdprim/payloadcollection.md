# USDPrim.PayloadCollection

**Framework**: USDKit  
**Kind**: struct

Manages payload composition arcs on a prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct PayloadCollection
```

## Topics

### Instance Properties
- [var prim: USDPrim](usdprim/payloadcollection/prim.md)
  The prim that owns these payload arcs.
### Instance Methods
- [func add(USDPrim.Payload, position: USDPrim.ListPosition) throws](usdprim/payloadcollection/add(_:position:).md)
  Adds an existing payload arc to the prim.
- [func add(to: USDLayer.Path?, from: String, layerOffset: USDLayer.TimeOffset, position: USDPrim.ListPosition) throws](usdprim/payloadcollection/add(to:from:layeroffset:position:).md)
  Adds an external payload arc.
- [func add(to: USDLayer.Path, layerOffset: USDLayer.TimeOffset, position: USDPrim.ListPosition) throws](usdprim/payloadcollection/add(to:layeroffset:position:).md)
  Adds an internal payload arc that targets a prim in the same layer stack.
- [func clear() throws](usdprim/payloadcollection/clear.md)
  Removes all payload arcs from the prim.
- [func remove(USDPrim.Payload) throws](usdprim/payloadcollection/remove(_:).md)
  Removes a specific payload arc from the prim.
- [func set([USDPrim.Payload]) throws](usdprim/payloadcollection/set(_:).md)
  Replaces all payload arcs with the specified list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/payloadcollection)*