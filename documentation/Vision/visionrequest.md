# VisionRequest

**Framework**: Vision  
**Kind**: protocol

A type for image-analysis requests.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
protocol VisionRequest : CustomStringConvertible, Hashable, Sendable
```

## Topics

### Getting the compute device
- [func computeDevice(for: ComputeStage) -> MLComputeDevice?](visionrequest/computedevice(for:).md)
  Returns the compute device for a compute stage.
- [var supportedComputeStageDevices: [ComputeStage : [MLComputeDevice]]](visionrequest/supportedcomputestagedevices.md)
  The collection of compute devices per stage that a request supports.
- [enum ComputeStage](computestage.md)
  Types that represent the compute stage.
### Setting the compute device
- [func setComputeDevice(MLComputeDevice?, for: ComputeStage)](visionrequest/setcomputedevice(_:for:).md)
  Assigns a compute device for a compute stage.
### Performing the request
- [associatedtype Result](visionrequest/result.md)
  An associated type that represents the result.
- [enum VisionResult](visionresult.md)
  The result the framework produces by performing a request.
### Instance Properties
- [var descriptor: RequestDescriptor](visionrequest/descriptor.md)
  An enum that identifies the request and request revision.

## Relationships

### Inherits From
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [ImageProcessingRequest](imageprocessingrequest.md)
- [StatefulRequest](statefulrequest.md)
- [TargetedRequest](targetedrequest.md)
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

- [Classifying images for categorization and search](classifying-images-for-categorization-and-search.md)
  Analyze and label images using a Vision classification request.
- [struct ClassifyImageRequest](classifyimagerequest.md)
  A request to classify an image.
- [protocol ImageProcessingRequest](imageprocessingrequest.md)
  A type for image-analysis requests that focus on a specific part of an image.
- [class ImageRequestHandler](imagerequesthandler.md)
  An object that processes one or more image-analysis requests pertaining to a single image.
- [protocol VisionObservation](visionobservation.md)
  A type for objects produced by image-analysis requests.
- [struct DetectLensSmudgeRequest](detectlenssmudgerequest.md)
  A request that detects a smudge on a lens from an image or video frame capture.
- [struct SmudgeObservation](smudgeobservation.md)
  An observation that provides an overall score of the presence of a smudge in an image or video frame capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionrequest)*