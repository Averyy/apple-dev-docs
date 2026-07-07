# USDPlayer.DeformationData

**Framework**: USDKit  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
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
- [USDPlayer.DeformationData.RenormalizationData](usdplayer/deformationdata/renormalizationdata.md)
- [USDPlayer.DeformationData.SkinningData](usdplayer/deformationdata/skinningdata.md)
- [USDPlayer.DeformationData.Update](usdplayer/deformationdata/update.md)
### Instance Properties
- [let blendShapes: USDPlayer.DeformationData.BlendShapeData?](usdplayer/deformationdata/blendshapes.md)
  Blend shape deformation data; nil when the mesh has no blend shapes
- [let id: USDPlayer.DeformationID](usdplayer/deformationdata/id.md)
- [let renormalization: USDPlayer.DeformationData.RenormalizationData?](usdplayer/deformationdata/renormalization.md)
  Renormalization adjacency data; present whenever skinning or blend shape data is present
- [let skinning: USDPlayer.DeformationData.SkinningData?](usdplayer/deformationdata/skinning.md)
  Skinning deformation data; nil when the mesh has no skeleton

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata)*