# USDPlayer.DeformationData.BlendShapeData.Update

**Framework**: USDKit  
**Kind**: struct

Delta update carrying only the blend shape fields that changed since the last frame.

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