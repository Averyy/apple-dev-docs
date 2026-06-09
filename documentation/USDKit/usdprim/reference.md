# USDPrim.Reference

**Framework**: USDKit  
**Kind**: struct

A reference to an external layer or asset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Reference
```

#### Overview

References are composition arcs that bring content from another layer into this prim. A reference specifies the asset path, an optional target prim path within that asset, a time offset for remapping animation, and arbitrary custom metadata.

## Topics

### Initializers
- [init(assetPath: String?, primPath: USDLayer.Path?, layerOffset: USDLayer.TimeOffset, customData: Dictionary<String, USDValue>)](usdprim/reference/init(assetpath:primpath:layeroffset:customdata:).md)
  Creates a reference.
### Instance Properties
- [var assetPath: String?](usdprim/reference/assetpath.md)
  The asset path the reference targets, or `nil` for an internal reference.
- [var customData: Dictionary<String, USDValue>](usdprim/reference/customdata.md)
  Custom metadata authored alongside the reference.
- [var isInternal: Bool](usdprim/reference/isinternal.md)
  Whether this is an internal reference (empty asset path).
- [var layerOffset: USDLayer.TimeOffset](usdprim/reference/layeroffset.md)
  Time-axis remap applied to the reference’s animation.
- [var primPath: USDLayer.Path?](usdprim/reference/primpath.md)
  The target prim path within the referenced asset, or `nil` to use the asset’s default prim.
### Instance Methods
- [func setCustomData(String, to: USDValue)](usdprim/reference/setcustomdata(_:to:).md)
  Sets `key` in `customData` to `value`.

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
- [USDPrim.ReferenceCollection](usdprim/referencecollection.md)
- [USDPrim.Payload](usdprim/payload.md)
  A payload to an external asset.
- [USDPrim.ListPosition](usdprim/listposition.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/reference)*