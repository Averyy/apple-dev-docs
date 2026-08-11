# captureQuality

**Framework**: Vision  
**Kind**: property

The quality of the face capture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
var captureQuality: FaceObservation.CaptureQuality?
```

#### Discussion

This value is nil for face observations produced by a `DetectFaceRectanglesRequest` analysis. Use [`DetectFaceCaptureQualityRequest`](detectfacecapturequalityrequest.md) to detect capture quality.

## See Also

- [FaceObservation.CaptureQuality](faceobservation/capturequality-swift.struct.md)
  An indicator of the quality of a face capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation/capturequality-swift.property)*