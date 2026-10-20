# USDPlayer.DeformationData.SkinningData.Update

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Delta update carrying only the skinning fields that changed since the last frame.

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
- [let geometryBindTransform: float4x4?](./update/geometrybindtransform.md)
  Changed geometry bind transform.
- [let influenceJointIndices: [UInt32]?](./update/influencejointindices.md)
  Changed joint influence indices.
- [let influenceWeights: [Float]?](./update/influenceweights.md)
  Changed joint influence weights.
- [let inverseBindPoses: [float4x4]?](./update/inversebindposes.md)
  Changed inverse bind poses.
- [let jointTransforms: [float4x4]?](./update/jointtransforms.md)
  Changed joint transforms.

## Relationships

### Conforms To
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata/skinningdata/update)*