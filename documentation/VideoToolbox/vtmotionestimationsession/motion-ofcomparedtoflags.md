# motion(of:comparedTo:flags:)

**Framework**: Video Toolbox  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func motion(of currentImage: CVReadOnlyPixelBuffer, comparedTo referenceImage: CVReadOnlyPixelBuffer, flags: VTMotionEstimationSession.FrameFlags = .init(rawValue:0)) async throws -> VTMotionEstimationSession.Motion
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationsession/motion(of:comparedto:flags:))*