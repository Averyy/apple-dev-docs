# VNSequenceRequestHandler

**Framework**: Vision  
**Kind**: class

An object that processes image-analysis requests for each frame in a sequence.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNSequenceRequestHandler
```

#### Overview

Instantiate this handler to perform Vision requests on a series of images. Unlike the [`VNImageRequestHandler`](vnimagerequesthandler.md), you don’t specify the image on creation. Instead, you supply each image frame one by one as you continue to call one of the `perform` methods.

## Topics

### Initializing a Sequence Request
- [init()](vnsequencerequesthandler/init.md)
  Initializes a sequence request handler.
### Performing a Sequence Request
- [func perform([VNRequest], on: CGImage) throws](vnsequencerequesthandler/perform(_:on:)-3zt7l.md)
  Schedules Vision requests to be performed on a Core Graphics image.
- [func perform([VNRequest], on: CGImage, orientation: CGImagePropertyOrientation) throws](vnsequencerequesthandler/perform(_:on:orientation:)-3gcmv.md)
  Schedules one or more Vision requests to be performed on a Core Graphics image with known orientation.
- [func perform([VNRequest], on: CIImage) throws](vnsequencerequesthandler/perform(_:on:)-9jtgj.md)
  Schedules one or more Vision requests to be performed on Core Image image data.
- [func perform([VNRequest], on: CIImage, orientation: CGImagePropertyOrientation) throws](vnsequencerequesthandler/perform(_:on:orientation:)-1bkm1.md)
  Schedules one or more Vision requests to be performed on Core Image image data with known orientation.
- [func perform([VNRequest], on: CVPixelBuffer) throws](vnsequencerequesthandler/perform(_:on:)-3d7nt.md)
  Schedules one or more Vision requests to be performed on a Core Video pixel buffer.
- [func perform([VNRequest], on: CVPixelBuffer, orientation: CGImagePropertyOrientation) throws](vnsequencerequesthandler/perform(_:on:orientation:)-2wvt8.md)
  Schedules one or more Vision requests to be performed on a Core Video pixel buffer with known orientation.
- [func perform([VNRequest], on: CMSampleBuffer) throws](vnsequencerequesthandler/perform(_:on:)-45e73.md)
  Performs one or more requests on an image contained within a sample buffer.
- [func perform([VNRequest], on: CMSampleBuffer, orientation: CGImagePropertyOrientation) throws](vnsequencerequesthandler/perform(_:on:orientation:)-6b7rk.md)
  Performs one or more requests on an image of a specified orientation contained within a sample buffer.
- [func perform([VNRequest], onImageData: Data) throws](vnsequencerequesthandler/perform(_:onimagedata:).md)
  Schedules one or more Vision requests to be performed on raw image data.
- [func perform([VNRequest], onImageData: Data, orientation: CGImagePropertyOrientation) throws](vnsequencerequesthandler/perform(_:onimagedata:orientation:).md)
  Schedules one or more Vision requests to be performed on raw data containing an image with known orientation.
- [func perform([VNRequest], onImageURL: URL) throws](vnsequencerequesthandler/perform(_:onimageurl:).md)
  Schedules one or more Vision requests to be performed on an image.
- [func perform([VNRequest], onImageURL: URL, orientation: CGImagePropertyOrientation) throws](vnsequencerequesthandler/perform(_:onimageurl:orientation:).md)
  Schedules one or more Vision requests to be performed on an image with known orientation, at a specific URL.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [class VNDetectDocumentSegmentationRequest](vndetectdocumentsegmentationrequest.md)
  An object that detects rectangular regions that contain text in the input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnsequencerequesthandler)*