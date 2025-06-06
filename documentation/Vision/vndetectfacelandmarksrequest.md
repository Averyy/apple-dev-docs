# VNDetectFaceLandmarksRequest

**Framework**: Vision  
**Kind**: class

An image-analysis request that finds facial features like eyes and mouth in an image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectFaceLandmarksRequest
```

#### Overview

By default, a face landmarks request first locates all faces in the input image, then analyzes each to detect facial features.

If you’ve already located all the faces in an image, or want to detect landmarks in only a subset of the faces in the image, set the [`inputFaceObservations`](vnfaceobservationaccepting/inputfaceobservations.md) property to an array of [`VNFaceObservation`](vnfaceobservation.md) objects representing the faces you want to analyze. You can either use face observations output by a [`VNDetectFaceRectanglesRequest`](vndetectfacerectanglesrequest.md) or manually create [`VNFaceObservation`](vnfaceobservation.md) instances with the bounding boxes of the faces you want to analyze.

## Topics

### Configuring a Face Landmarks Request
- [protocol VNFaceObservationAccepting](vnfaceobservationaccepting.md)
  An image analysis request that operates on face observations.
### Accessing the Results
- [var results: [VNFaceObservation]?](vndetectfacelandmarksrequest/results.md)
  The results of the face landmarks request.
- [class VNFaceObservation](vnfaceobservation.md)
  Face or facial-feature information that an image analysis request detects.
### Locating Face Landmarks
- [var constellation: VNRequestFaceLandmarksConstellation](vndetectfacelandmarksrequest/constellation.md)
  A variable that describes how a face landmarks request orders or enumerates the resulting features.
- [enum VNRequestFaceLandmarksConstellation](vnrequestfacelandmarksconstellation.md)
  An enumeration of face landmarks in a constellation object.
### Identifying Request Revisions
- [class func revision(Int, supportsConstellation: VNRequestFaceLandmarksConstellation) -> Bool](vndetectfacelandmarksrequest/revision(_:supportsconstellation:).md)
  Returns a Boolean value that indicates whether a revision supports a constellation.
- [let VNDetectFaceLandmarksRequestRevision3: Int](vndetectfacelandmarksrequestrevision3.md)
  A constant for specifying revision 3 of the face landmarks detection request.
- [let VNDetectFaceLandmarksRequestRevision2: Int](vndetectfacelandmarksrequestrevision2.md)
  A constant for specifying revision 2 of the face landmarks detection request.
- [let VNDetectFaceLandmarksRequestRevision1: Int](vndetectfacelandmarksrequestrevision1.md)
  A constant for specifying revision 1 of the face landmarks detection request.

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
- [class VNDetectFaceCaptureQualityRequest](vndetectfacecapturequalityrequest.md)
  A request that produces a floating-point number that represents the capture quality of a face in a photo.
- [class VNDetectFaceRectanglesRequest](vndetectfacerectanglesrequest.md)
  A request that finds faces within an image.
- [class VNDetectHumanRectanglesRequest](vndetecthumanrectanglesrequest.md)
  A request that finds rectangular regions that contain people in an image.
- [class VNHumanObservation](vnhumanobservation.md)
  An object that represents a person that the request detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectfacelandmarksrequest)*