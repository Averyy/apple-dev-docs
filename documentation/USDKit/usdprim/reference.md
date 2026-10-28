# USDPrim.Reference

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A reference to an external layer or asset.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Reference
```

## Overview

References are composition arcs that bring content from another layer into this prim. A reference specifies the asset path, an optional target prim path within that asset, a time offset for remapping animation, and arbitrary custom metadata.

## Topics

### Initializers
- [init(assetPath: String?, primPath: USDLayer.Path?, layerOffset: USDLayer.TimeOffset, customData: Dictionary<String, USDValue>)](./reference/init%28assetpath,primpath,layeroffset,customdata%29.md)
  Creates a reference.
### Instance Properties
- [var assetPath: String?](./reference/assetpath.md)
  The asset path the reference targets, or `nil` for an internal reference.
- [var customData: Dictionary<String, USDValue>](./reference/customdata.md)
  Custom metadata authored alongside the reference.
- [var isInternal: Bool](./reference/isinternal.md)
  Whether this is an internal reference (empty asset path).
- [var layerOffset: USDLayer.TimeOffset](./reference/layeroffset.md)
  Time-axis remap applied to the reference’s animation.
- [var primPath: USDLayer.Path?](./reference/primpath.md)
  The target prim path within the referenced asset, or `nil` to use the asset’s default prim.
### Instance Methods
- [func setCustomData(String, to: USDValue)](./reference/setcustomdata%28_,to%29.md)
  Sets `key` in `customData` to `value`.

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
- [USDPrim.ReferenceCollection](./referencecollection.md)
  Manages reference composition arcs on a prim.
- [USDPrim.Payload](./payload.md)
  A payload to an external asset.
- [USDPrim.ListPosition](./listposition.md)
  Where a new composition arc should be inserted relative to existing arcs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/reference)*