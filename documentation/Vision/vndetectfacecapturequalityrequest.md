# VNDetectFaceCaptureQualityRequest

**Framework**: Vision  
**Kind**: class

A request that produces a floating-point number that represents the capture quality of a face in a photo.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectFaceCaptureQualityRequest
```

#### Overview

This request produces or updates a [`VNFaceObservation`](vnfaceobservation.md) object’s property [`faceCaptureQuality`](vnfaceobservation/facecapturequality-bjg5.md) with a floating-point value. The value ranges from `0` to `1`. Faces with quality closer to `1` are better lit, sharper, and more centrally positioned than faces with quality closer to `0`.

If you don’t execute the request, or the request fails, the property [`faceCaptureQuality`](vnfaceobservation/facecapturequality-bjg5.md) is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0).

## Topics

### Accessing the Results
- [var results: [VNFaceObservation]?](vndetectfacecapturequalityrequest/results.md)
  The results of the face-capture quality request.
- [class VNFaceObservation](vnfaceobservation.md)
  Face or facial-feature information that an image analysis request detects.
### Identifying Request Revisions
- [let VNDetectFaceCaptureQualityRequestRevision2: Int](vndetectfacecapturequalityrequestrevision2.md)
  Revision 2 of the request algorithm.
- [let VNDetectFaceCaptureQualityRequestRevision1: Int](vndetectfacecapturequalityrequestrevision1.md)
  A constant for specifying revision 1 of the face capture detection request.

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
- [VNFaceObservationAccepting](vnfaceobservationaccepting.md)

## See Also

- [Selecting a selfie based on capture quality](selecting-a-selfie-based-on-capture-quality.md)
  Compare face-capture quality in a set of images by using Vision.
- [class VNDetectFaceLandmarksRequest](vndetectfacelandmarksrequest.md)
  An image-analysis request that finds facial features like eyes and mouth in an image.
- [class VNDetectFaceRectanglesRequest](vndetectfacerectanglesrequest.md)
  A request that finds faces within an image.
- [class VNDetectHumanRectanglesRequest](vndetecthumanrectanglesrequest.md)
  A request that finds rectangular regions that contain people in an image.
- [class VNHumanObservation](vnhumanobservation.md)
  An object that represents a person that the request detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectfacecapturequalityrequest)*