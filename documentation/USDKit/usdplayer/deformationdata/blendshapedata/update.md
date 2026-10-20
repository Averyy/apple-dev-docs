# USDPlayer.DeformationData.BlendShapeData.Update

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

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
- [let positionOffsets: [[SIMD3<Float>]]?](./update/positionoffsets.md)
  Changed position delta offsets.
- [let weights: [Float]?](./update/weights.md)
  Changed blend shape weights.

## Relationships

### Conforms To
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/deformationdata/blendshapedata/update)*