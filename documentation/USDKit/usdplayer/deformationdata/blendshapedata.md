# USDPlayer.DeformationData.BlendShapeData

**Framework**: USDKit  
**Kind**: struct

Blend shape targets and weights for morph-target deformation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct BlendShapeData
```

## Topics

### Structures
- [USDPlayer.DeformationData.BlendShapeData.Update](usdplayer/deformationdata/blendshapedata/update.md)
  Delta update carrying only the blend shape fields that changed since the last frame.
### Instance Properties
- [let positionOffsets: [[SIMD3<Float>]]](usdplayer/deformationdata/blendshapedata/positionoffsets.md)
  Per-vertex position delta vectors for each blend shape target.
- [let weights: [Float]](usdplayer/deformationdata/blendshapedata/weights.md)
  Weight values controlling each blend shape target’s influence.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata/blendshapedata)*