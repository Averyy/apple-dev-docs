# USDPlayer.DeformationData.BlendShapeData.Update

**Framework**: USDKit  
**Kind**: struct

Delta update carrying only the blend shape fields that changed since the last frame.

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
- [let positionOffsets: [[SIMD3<Float>]]?](usdplayer/deformationdata/blendshapedata/update/positionoffsets.md)
  Changed position delta offsets.
- [let weights: [Float]?](usdplayer/deformationdata/blendshapedata/update/weights.md)
  Changed blend shape weights.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata/blendshapedata/update)*