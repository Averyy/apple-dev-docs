# VNDetectFaceRectanglesRequest

**Framework**: Vision  
**Kind**: class

A request that finds faces within an image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectFaceRectanglesRequest
```

#### Overview

This request returns faces as rectangular bounding boxes with origin and size.

## Topics

### Accessing the Results
- [var results: [VNFaceObservation]?](vndetectfacerectanglesrequest/results.md)
  The results of the face detection request.
- [class VNFaceObservation](vnfaceobservation.md)
  Face or facial-feature information that an image analysis request detects.
### Identifying Request Revisions
- [let VNDetectFaceRectanglesRequestRevision3: Int](vndetectfacerectanglesrequestrevision3.md)
  A constant for specifying revision 3 of the face rectangles detection request.
- [let VNDetectFaceRectanglesRequestRevision2: Int](vndetectfacerectanglesrequestrevision2.md)
  A constant for specifying revision 2 of the face rectangles detection request.
- [let VNDetectFaceRectanglesRequestRevision1: Int](vndetectfacerectanglesrequestrevision1.md)
  A constant for specifying revision 1 of the face rectangles detection request.

## Relationships

### Inherits From
- [VNImageBasedRequest](vnimagebasedrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Selecting a selfie based on capture quality](selecting-a-selfie-based-on-capture-quality.md)
  Compare face-capture quality in a set of images by using Vision.
- [class VNDetectFaceCaptureQualityRequest](vndetectfacecapturequalityrequest.md)
  A request that produces a floating-point number that represents the capture quality of a face in a photo.
- [class VNDetectFaceLandmarksRequest](vndetectfacelandmarksrequest.md)
  An image-analysis request that finds facial features like eyes and mouth in an image.
- [class VNDetectHumanRectanglesRequest](vndetecthumanrectanglesrequest.md)
  A request that finds rectangular regions that contain people in an image.
- [class VNHumanObservation](vnhumanobservation.md)
  An object that represents a person that the request detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectfacerectanglesrequest)*