# VNDetectDocumentSegmentationRequest

**Framework**: Vision  
**Kind**: class

An object that detects rectangular regions that contain text in the input image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectDocumentSegmentationRequest
```

#### Overview

Perform this request to detect a document in an image. The result that the request generates contains the four corner points of a document’s quadrilateral and saliency mask.

## Topics

### Accessing the Results
- [var results: [VNRectangleObservation]?](vndetectdocumentsegmentationrequest/results.md)
  The results of a document segmentation request.
- [class VNRectangleObservation](vnrectangleobservation.md)
  An object that represents the four vertices of a detected rectangle.
### Identifying Request Revisions
- [let VNDetectDocumentSegmentationRequestRevision1: Int](vndetectdocumentsegmentationrequestrevision1.md)
  A constant for specifying revision 1 of the document segmentation request.

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

- [Applying Matte Effects to People in Images and Video](applying-matte-effects-to-people-in-images-and-video.md)
  Generate image masks for people automatically by using semantic person-segmentation.
- [Detecting Human Actions in a Live Video Feed](../createml/detecting_human_actions_in_a_live_video_feed.md)
  Identify body movements by sending a person’s pose data from a series of video frames to an action-classification model.
- [Segmenting and colorizing individuals from a surrounding scene](segmenting-and-colorizing-individuals-from-a-surrounding-scene.md)
  Use the Vision framework to isolate and apply colors to people in an image.
- [class VNStatefulRequest](vnstatefulrequest.md)
  An abstract request type that builds evidence of a condition over time.
- [class VNGeneratePersonSegmentationRequest](vngeneratepersonsegmentationrequest.md)
  An object that produces a matte image for a person it finds in the input image.
- [class VNGeneratePersonInstanceMaskRequest](vngeneratepersoninstancemaskrequest.md)
  An object that produces a mask of individual people it finds in the input image.
- [class VNSequenceRequestHandler](vnsequencerequesthandler.md)
  An object that processes image-analysis requests for each frame in a sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectdocumentsegmentationrequest)*