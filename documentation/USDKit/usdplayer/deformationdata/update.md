# USDPlayer.DeformationData.Update

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Delta update carrying only the deformation fields that changed since the last frame.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Update
```

## Topics

### Instance Properties
- [let blendShapes: USDPlayer.DeformationData.BlendShapeData.Update?](./update/blendshapes.md)
  Changed blend shape data.
- [let id: USDPlayer.DeformationID](./update/id.md)
  Unique identifier for the deformation resource being updated.
- [let renormalization: USDPlayer.DeformationData.RenormalizationData.Update?](./update/renormalization.md)
  Changed renormalization data.
- [let skinning: USDPlayer.DeformationData.SkinningData.Update?](./update/skinning.md)
  Changed skinning data.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata/update)*