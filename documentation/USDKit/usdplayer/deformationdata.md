# USDPlayer.DeformationData

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Deformation data for a single deformable mesh.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct DeformationData
```

## Topics

### Structures
- [USDPlayer.DeformationData.BlendShapeData](./deformationdata/blendshapedata.md)
  Blend shape targets and weights for morph-target deformation.
- [USDPlayer.DeformationData.RenormalizationData](./deformationdata/renormalizationdata.md)
  Triangle adjacency data for post-deformation normal renormalization.
- [USDPlayer.DeformationData.SkinningData](./deformationdata/skinningdata.md)
  Joint deformation data for a skinned mesh.
- [USDPlayer.DeformationData.Update](./deformationdata/update.md)
  Delta update carrying only the deformation fields that changed since the last frame.
### Instance Properties
- [let blendShapes: USDPlayer.DeformationData.BlendShapeData?](./deformationdata/blendshapes.md)
  Blend shape deformation data.
- [let id: USDPlayer.DeformationID](./deformationdata/id.md)
  Unique identifier for this deformation resource.
- [let renormalization: USDPlayer.DeformationData.RenormalizationData?](./deformationdata/renormalization.md)
  Renormalization data.
- [let skinning: USDPlayer.DeformationData.SkinningData?](./deformationdata/skinning.md)
  Skinning deformation data.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata)*