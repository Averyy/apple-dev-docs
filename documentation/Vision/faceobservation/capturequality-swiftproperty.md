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

## Declaration

```swift
var captureQuality: FaceObservation.CaptureQuality? { get }
```

#### Discussion

This value is nil for face observations produced by a `DetectFaceRectanglesRequest` analysis. Use [`DetectFaceCaptureQualityRequest`](detectfacecapturequalityrequest.md) to detect capture quality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation/capturequality-swift.property)*