# inputFaceObservations

**Framework**: Vision  
**Kind**: property

An array of face-observation objects to process as part of the request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var inputFaceObservations: [FaceObservation]?
```

#### Discussion

The default is `nil`. When `nil`, the framework first performs a [`DetectFaceRectanglesRequest`](detectfacerectanglesrequest.md) and processes all faces detected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectfacecapturequalityrequest/inputfaceobservations)*