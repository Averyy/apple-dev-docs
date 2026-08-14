# USDPlayer.DeformationData.SkinningData.Update

**Framework**: USDKit  
**Kind**: struct

Delta update carrying only the skinning fields that changed since the last frame.

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
- [let geometryBindTransform: float4x4?](usdplayer/deformationdata/skinningdata/update/geometrybindtransform.md)
  Changed geometry bind transform.
- [let influenceJointIndices: [UInt32]?](usdplayer/deformationdata/skinningdata/update/influencejointindices.md)
  Changed joint influence indices.
- [let influenceWeights: [Float]?](usdplayer/deformationdata/skinningdata/update/influenceweights.md)
  Changed joint influence weights.
- [let inverseBindPoses: [float4x4]?](usdplayer/deformationdata/skinningdata/update/inversebindposes.md)
  Changed inverse bind poses.
- [let jointTransforms: [float4x4]?](usdplayer/deformationdata/skinningdata/update/jointtransforms.md)
  Changed joint transforms.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata/skinningdata/update)*