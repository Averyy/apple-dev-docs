# landmarks

**Framework**: Vision  
**Kind**: property

The facial features of the detected face.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var landmarks: VNFaceLandmarks2D? { get }
```

#### Discussion

This value is `nil` for face observations produced by a [`VNDetectFaceRectanglesRequest`](vndetectfacerectanglesrequest.md) analysis. Use the [`VNDetectFaceLandmarksRequest`](vndetectfacelandmarksrequest.md) class to find facial features.

## See Also

- [class VNFaceLandmarks2D](vnfacelandmarks2d.md)
  A collection of facial features that a request detects.
- [class VNFaceLandmarkRegion2D](vnfacelandmarkregion2d.md)
  2D geometry information for a specific facial feature.
- [class VNFaceLandmarks](vnfacelandmarks.md)
  The abstract superclass for containers of face landmark information.
- [class VNFaceLandmarkRegion](vnfacelandmarkregion.md)
  The abstract superclass for information about a specific face landmark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfaceobservation/landmarks)*