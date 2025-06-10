# motion(of:comparedTo:flags:)

**Framework**: Video Toolbox  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func motion(of currentImage: CVReadOnlyPixelBuffer, comparedTo referenceImage: CVReadOnlyPixelBuffer, flags: VTMotionEstimationSession.FrameFlags = .init(rawValue:0)) async throws -> VTMotionEstimationSession.Motion
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationsession/motion(of:comparedto:flags:))*