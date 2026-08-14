# USDPlayer.DeformationData.SkinningData

**Framework**: USDKit  
**Kind**: struct

Joint deformation data for a skinned mesh.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SkinningData
```

## Topics

### Structures
- [USDPlayer.DeformationData.SkinningData.Update](usdplayer/deformationdata/skinningdata/update.md)
  Delta update carrying only the skinning fields that changed since the last frame.
### Instance Properties
- [let geometryBindTransform: float4x4](usdplayer/deformationdata/skinningdata/geometrybindtransform.md)
  Transform from world space into bind space of the skinned mesh.
- [let influenceJointIndices: [UInt32]](usdplayer/deformationdata/skinningdata/influencejointindices.md)
  Joint indices for each vertex-influence slot, with `influencePerVertexCount` consecutive entries per vertex.
- [let influencePerVertexCount: UInt8](usdplayer/deformationdata/skinningdata/influencepervertexcount.md)
  Number of joint influences per vertex.
- [let influenceWeights: [Float]](usdplayer/deformationdata/skinningdata/influenceweights.md)
  Influence weights (0.0–1.0) corresponding 1:1 with `influenceJointIndices`.
- [let inverseBindPoses: [float4x4]](usdplayer/deformationdata/skinningdata/inversebindposes.md)
  Inverse bind-pose transformation matrix for each joint.
- [let jointTransforms: [float4x4]](usdplayer/deformationdata/skinningdata/jointtransforms.md)
  Current transformation matrices for each joint in the skeleton hierarchy, in joint order.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata/skinningdata)*