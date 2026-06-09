# USDPrim.Payload

**Framework**: USDKit  
**Kind**: struct

A payload to an external asset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Payload
```

#### Overview

Payloads are similar to references but designed for deferred loading. Heavy assets like detailed geometry can be added as payloads and loaded on demand rather than at composition time.

## Topics

### Initializers
- [init(assetPath: String?, primPath: USDLayer.Path?, layerOffset: USDLayer.TimeOffset)](usdprim/payload/init(assetpath:primpath:layeroffset:).md)
  Creates a payload.
### Instance Properties
- [var assetPath: String?](usdprim/payload/assetpath.md)
  The asset path the payload targets, or `nil` if not yet set.
- [var layerOffset: USDLayer.TimeOffset](usdprim/payload/layeroffset.md)
  Time-axis remap applied to the payload’s animation.
- [var primPath: USDLayer.Path?](usdprim/payload/primpath.md)
  The target prim path within the referenced asset, or `nil` to use the asset’s default prim.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var references: USDPrim.ReferenceCollection](usdprim/references.md)
  The reference composition arcs on this prim.
- [USDPrim.Reference](usdprim/reference.md)
  A reference to an external layer or asset.
- [USDPrim.ReferenceCollection](usdprim/referencecollection.md)
- [USDPrim.ListPosition](usdprim/listposition.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/payload)*