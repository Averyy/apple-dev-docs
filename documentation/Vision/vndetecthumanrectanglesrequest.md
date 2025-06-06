# VNDetectHumanRectanglesRequest

**Framework**: Vision  
**Kind**: class

A request that finds rectangular regions that contain people in an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectHumanRectanglesRequest
```

## Topics

### Configuring the Request
- [var upperBodyOnly: Bool](vndetecthumanrectanglesrequest/upperbodyonly.md)
  A Boolean value that indicates whether the request requires detecting a full body or upper body only to produce a result.
### Accessing the Results
- [var results: [VNHumanObservation]?](vndetecthumanrectanglesrequest/results.md)
  The results of the request to find rectangular regions that contain people in an image.
### Identifying Request Revisions
- [let VNDetectHumanRectanglesRequestRevision2: Int](vndetecthumanrectanglesrequestrevision2.md)
  A constant for specifying revision 2 of the human rectangles detection request.
- [let VNDetectHumanRectanglesRequestRevision1: Int](vndetecthumanrectanglesrequestrevision1.md)
  A constant for specifying revision 1 of the human rectangles detection request.

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
- [class VNDetectFaceRectanglesRequest](vndetectfacerectanglesrequest.md)
  A request that finds faces within an image.
- [class VNHumanObservation](vnhumanobservation.md)
  An object that represents a person that the request detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanrectanglesrequest)*