# VTMotionEstimationSession

**Framework**: Video Toolbox  
**Kind**: class  
**Role**: Class

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

### Creating a motion estimation session
- [init(width: UInt32, height: UInt32, motionVectorSize: VTMotionEstimationSession.BlockSize, useMultiPassSearch: Bool, label: String?) throws](./vtmotionestimationsession/init%28width,height,motionvectorsize,usemultipasssearch,label%29.md)
### Estimating motion
- [func motion(of: CVReadOnlyPixelBuffer, comparedTo: CVReadOnlyPixelBuffer, flags: VTMotionEstimationSession.FrameFlags) async throws -> VTMotionEstimationSession.Motion](./vtmotionestimationsession/motion%28of,comparedto,flags%29.md)
- [VTMotionEstimationSession.FrameFlags](./vtmotionestimationsession/frameflags.md)
### Inspecting the session
- [var label: String?](./vtmotionestimationsession/label.md)
- [var motionVectorSize: VTMotionEstimationSession.BlockSize](./vtmotionestimationsession/motionvectorsize.md)
- [var sourcePixelBufferAttributes: [String : any Sendable]](./vtmotionestimationsession/sourcepixelbufferattributes.md)
- [var useMultiPassSearch: Bool](./vtmotionestimationsession/usemultipasssearch.md)
### Inspecting the motion result
- [VTMotionEstimationSession.Motion](./vtmotionestimationsession/motion.md)
- [VTMotionEstimationSession.BlockSize](./vtmotionestimationsession/blocksize.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationsession)*