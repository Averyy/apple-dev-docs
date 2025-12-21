# VTMotionEstimationSession

**Framework**: Video Toolbox  
**Kind**: class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final class VTMotionEstimationSession
```

## Topics

### Structures
- [VTMotionEstimationSession.FrameFlags](vtmotionestimationsession/frameflags.md)
- [VTMotionEstimationSession.Motion](vtmotionestimationsession/motion.md)
### Initializers
- [init(width: UInt32, height: UInt32, motionVectorSize: VTMotionEstimationSession.BlockSize, useMultiPassSearch: Bool, label: String?) throws](vtmotionestimationsession/init(width:height:motionvectorsize:usemultipasssearch:label:).md)
### Instance Properties
- [var label: String?](vtmotionestimationsession/label.md)
- [var motionVectorSize: VTMotionEstimationSession.BlockSize](vtmotionestimationsession/motionvectorsize.md)
- [var sourcePixelBufferAttributes: [String : any Sendable]](vtmotionestimationsession/sourcepixelbufferattributes.md)
- [var useMultiPassSearch: Bool](vtmotionestimationsession/usemultipasssearch.md)
### Instance Methods
- [func motion(of: CVReadOnlyPixelBuffer, comparedTo: CVReadOnlyPixelBuffer, flags: VTMotionEstimationSession.FrameFlags) async throws -> VTMotionEstimationSession.Motion](vtmotionestimationsession/motion(of:comparedto:flags:).md)
### Enumerations
- [VTMotionEstimationSession.BlockSize](vtmotionestimationsession/blocksize.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationsession)*