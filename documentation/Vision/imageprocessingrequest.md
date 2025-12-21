# ImageProcessingRequest

**Framework**: Vision  
**Kind**: protocol

A type for image-analysis requests that focus on a specific part of an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
protocol ImageProcessingRequest : VisionRequest
```

## Topics

### Setting the region
- [var regionOfInterest: NormalizedRect](imageprocessingrequest/regionofinterest.md)
  The region of the image where the framework performs the request.
### Performing a request
- [func perform(on: URL, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-80bya.md)
  Performs the request on an image URL and produces observations.
- [func perform(on: Data, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3f3f1.md)
  Performs the request on image data and produces observations.
- [func perform(on: CGImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-qxxx.md)
  Performs the request on a Core Graphics image and produces observations.
- [func perform(on: CVPixelBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-xspx.md)
  Performs the request on a pixel buffer and produces observations.
- [func perform(on: CMSampleBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3hddl.md)
  Performs the request on a Core Media buffer and produces observations.
- [func perform(on: CIImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-85ex1.md)
  Performs the request on a Core Image image and produces observations.

## Relationships

### Inherits From
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionRequest](visionrequest.md)
### Conforming Types
- [CalculateImageAestheticsScoresRequest](calculateimageaestheticsscoresrequest.md)
- [ClassifyImageRequest](classifyimagerequest.md)
- [CoreMLRequest](coremlrequest.md)
- [DetectAnimalBodyPoseRequest](detectanimalbodyposerequest.md)
- [DetectBarcodesRequest](detectbarcodesrequest.md)
- [DetectContoursRequest](detectcontoursrequest.md)
- [DetectDocumentSegmentationRequest](detectdocumentsegmentationrequest.md)
- [DetectFaceCaptureQualityRequest](detectfacecapturequalityrequest.md)
- [DetectFaceLandmarksRequest](detectfacelandmarksrequest.md)
- [DetectFaceRectanglesRequest](detectfacerectanglesrequest.md)
- [DetectHorizonRequest](detecthorizonrequest.md)
- [DetectHumanBodyPose3DRequest](detecthumanbodypose3drequest.md)
- [DetectHumanBodyPoseRequest](detecthumanbodyposerequest.md)
- [DetectHumanHandPoseRequest](detecthumanhandposerequest.md)
- [DetectHumanRectanglesRequest](detecthumanrectanglesrequest.md)
- [DetectLensSmudgeRequest](detectlenssmudgerequest.md)
- [DetectRectanglesRequest](detectrectanglesrequest.md)
- [DetectTextRectanglesRequest](detecttextrectanglesrequest.md)
- [DetectTrajectoriesRequest](detecttrajectoriesrequest.md)
- [GenerateAttentionBasedSaliencyImageRequest](generateattentionbasedsaliencyimagerequest.md)
- [GenerateForegroundInstanceMaskRequest](generateforegroundinstancemaskrequest.md)
- [GenerateImageFeaturePrintRequest](generateimagefeatureprintrequest.md)
- [GenerateObjectnessBasedSaliencyImageRequest](generateobjectnessbasedsaliencyimagerequest.md)
- [GeneratePersonInstanceMaskRequest](generatepersoninstancemaskrequest.md)
- [GeneratePersonSegmentationRequest](generatepersonsegmentationrequest.md)
- [RecognizeAnimalsRequest](recognizeanimalsrequest.md)
- [RecognizeDocumentsRequest](recognizedocumentsrequest.md)
- [RecognizeTextRequest](recognizetextrequest.md)
- [TrackHomographicImageRegistrationRequest](trackhomographicimageregistrationrequest.md)
- [TrackObjectRequest](trackobjectrequest.md)
- [TrackOpticalFlowRequest](trackopticalflowrequest.md)
- [TrackRectangleRequest](trackrectanglerequest.md)
- [TrackTranslationalImageRegistrationRequest](tracktranslationalimageregistrationrequest.md)

## See Also

- [protocol PoseProviding](poseproviding.md)
  An observation that provides a collection of joints that make up a pose.
- [protocol StatefulRequest](statefulrequest.md)
  The protocol for a type that builds evidence of a condition over time.
- [protocol TargetedRequest](targetedrequest.md)
  A type for analyzing two images together.
- [protocol VisionObservation](visionobservation.md)
  A type for objects produced by image-analysis requests.
- [protocol VisionRequest](visionrequest.md)
  A type for image-analysis requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imageprocessingrequest)*