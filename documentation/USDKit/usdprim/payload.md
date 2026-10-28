# USDPrim.Payload

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A payload to an external asset.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Payload
```

## Overview

Payloads are similar to references but designed for deferred loading. Heavy assets like detailed geometry can be added as payloads and loaded on demand rather than at composition time.

## Topics

### Initializers
- [init(assetPath: String?, primPath: USDLayer.Path?, layerOffset: USDLayer.TimeOffset)](./payload/init%28assetpath,primpath,layeroffset%29.md)
  Creates a payload.
### Instance Properties
- [var assetPath: String?](./payload/assetpath.md)
  The asset path the payload targets, or `nil` if not yet set.
- [var layerOffset: USDLayer.TimeOffset](./payload/layeroffset.md)
  Time-axis remap applied to the payload’s animation.
- [var primPath: USDLayer.Path?](./payload/primpath.md)
  The target prim path within the referenced asset, or `nil` to use the asset’s default prim.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Composing references and payloads
- [var references: USDPrim.ReferenceCollection](./references.md)
  The reference composition arcs on this prim.
- [USDPrim.Reference](./reference.md)
  A reference to an external layer or asset.
- [USDPrim.ReferenceCollection](./referencecollection.md)
  Manages reference composition arcs on a prim.
- [USDPrim.ListPosition](./listposition.md)
  Where a new composition arc should be inserted relative to existing arcs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/payload)*