# USDPlayer.DeformationData

**Framework**: USDKit  
**Kind**: struct

Deformation data for a single deformable mesh.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DeformationData
```

## Topics

### Structures
- [USDPlayer.DeformationData.BlendShapeData](usdplayer/deformationdata/blendshapedata.md)
  Blend shape targets and weights for morph-target deformation.
- [USDPlayer.DeformationData.RenormalizationData](usdplayer/deformationdata/renormalizationdata.md)
  Triangle adjacency data for post-deformation normal renormalization.
- [USDPlayer.DeformationData.SkinningData](usdplayer/deformationdata/skinningdata.md)
  Joint deformation data for a skinned mesh.
- [USDPlayer.DeformationData.Update](usdplayer/deformationdata/update.md)
  Delta update carrying only the deformation fields that changed since the last frame.
### Instance Properties
- [let blendShapes: USDPlayer.DeformationData.BlendShapeData?](usdplayer/deformationdata/blendshapes.md)
  Blend shape deformation data.
- [let id: USDPlayer.DeformationID](usdplayer/deformationdata/id.md)
  Unique identifier for this deformation resource.
- [let renormalization: USDPlayer.DeformationData.RenormalizationData?](usdplayer/deformationdata/renormalization.md)
  Renormalization data.
- [let skinning: USDPlayer.DeformationData.SkinningData?](usdplayer/deformationdata/skinning.md)
  Skinning deformation data.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata)*