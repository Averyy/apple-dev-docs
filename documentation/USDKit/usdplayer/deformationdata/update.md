# USDPlayer.DeformationData.Update

**Framework**: USDKit  
**Kind**: struct

Delta update carrying only the deformation fields that changed since the last frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Update
```

## Topics

### Instance Properties
- [let blendShapes: USDPlayer.DeformationData.BlendShapeData.Update?](usdplayer/deformationdata/update/blendshapes.md)
  Changed blend shape data.
- [let id: USDPlayer.DeformationID](usdplayer/deformationdata/update/id.md)
  Unique identifier for the deformation resource being updated.
- [let renormalization: USDPlayer.DeformationData.RenormalizationData.Update?](usdplayer/deformationdata/update/renormalization.md)
  Changed renormalization data.
- [let skinning: USDPlayer.DeformationData.SkinningData.Update?](usdplayer/deformationdata/update/skinning.md)
  Changed skinning data.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata/update)*