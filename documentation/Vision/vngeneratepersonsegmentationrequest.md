# VNGeneratePersonSegmentationRequest

**Framework**: Vision  
**Kind**: class

An object that produces a matte image for a person it finds in the input image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class VNGeneratePersonSegmentationRequest
```

#### Overview

Perform this request to detect and generate an image mask for a person in an image. The request returns the resulting image mask in an instance of [`VNPixelBufferObservation`](vnpixelbufferobservation.md).

## Topics

### Creating a Request
- [init()](vngeneratepersonsegmentationrequest/init.md)
  Creates a generate person segmentation request.
- [init(completionHandler: VNRequestCompletionHandler?)](vngeneratepersonsegmentationrequest/init(completionhandler:).md)
  Creates a generate person segmentation request with a completion handler.
### Configuring the Request
- [var outputPixelFormat: OSType](vngeneratepersonsegmentationrequest/outputpixelformat.md)
  The pixel format of the output image.
- [var qualityLevel: VNGeneratePersonSegmentationRequest.QualityLevel](vngeneratepersonsegmentationrequest/qualitylevel-swift.property.md)
  A value that indicates how the request balances accuracy and performance.
- [VNGeneratePersonSegmentationRequest.QualityLevel](vngeneratepersonsegmentationrequest/qualitylevel-swift.enum.md)
  Constants that define the levels of quality for a person segmentation request.
### Getting the supported output pixel formats
- [func supportedOutputPixelFormats() throws -> [NSNumber]](vngeneratepersonsegmentationrequest/supportedoutputpixelformats.md)
  Returns a list of output pixel formats that the request supports.
### Accessing the Results
- [var results: [VNPixelBufferObservation]?](vngeneratepersonsegmentationrequest/results.md)
  The results of the segmentation request.
- [class VNPixelBufferObservation](vnpixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.
### Identifying Request Revisions
- [let VNGeneratePersonSegmentationRequestRevision1: Int](vngeneratepersonsegmentationrequestrevision1.md)
  A constant for specifying revision 1 of the person segmentation generation request.

## Relationships

### Inherits From
- [VNStatefulRequest](vnstatefulrequest.md)
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
- [Detecting human actions in a live video feed](../CreateML/detecting-human-actions-in-a-live-video-feed.md)
  Identify body movements by sending a person’s pose data from a series of video frames to an action-classification model.
- [Segmenting and colorizing individuals from a surrounding scene](segmenting-and-colorizing-individuals-from-a-surrounding-scene.md)
  Use the Vision framework to isolate and apply colors to people in an image.
- [class VNStatefulRequest](vnstatefulrequest.md)
  An abstract request type that builds evidence of a condition over time.
- [class VNGeneratePersonInstanceMaskRequest](vngeneratepersoninstancemaskrequest.md)
  An object that produces a mask of individual people it finds in the input image.
- [class VNDetectDocumentSegmentationRequest](vndetectdocumentsegmentationrequest.md)
  An object that detects rectangular regions that contain text in the input image.
- [class VNSequenceRequestHandler](vnsequencerequesthandler.md)
  An object that processes image-analysis requests for each frame in a sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngeneratepersonsegmentationrequest)*