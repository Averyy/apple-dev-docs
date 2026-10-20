# VisionResult

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

The result the framework produces by performing a request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
enum VisionResult
```

#### Overview

Each result contains the original [`VisionRequest`](./visionrequest.md), along with any observations produced.

## Topics

### Getting the still-image result
- [case classifyImage(ClassifyImageRequest, [ClassificationObservation])](./visionresult/classifyimage%28_,_%29.md)
  A result from performing a classify image request.
### Getting the image sequence result
- [case generatePersonInstanceMask(GeneratePersonInstanceMaskRequest, InstanceMaskObservation?)](./visionresult/generatepersoninstancemask%28_,_%29.md)
  A result from performing a generate person instance mask request.
- [case generatePersonSegmentation(GeneratePersonSegmentationRequest, PixelBufferObservation)](./visionresult/generatepersonsegmentation%28_,_%29.md)
  A result from performing a generate person segmentation request.
- [case detectDocumentSegmentation(DetectDocumentSegmentationRequest, DetectedDocumentObservation?)](./visionresult/detectdocumentsegmentation%28_,_%29.md)
  A result from performing a detect document segmentation request.
- [case generateIterativeSegmentation(GenerateIterativeSegmentationRequest, PixelBufferObservation?)](./visionresult/generateiterativesegmentation%28_,_%29.md)
- [case recognizeDocuments(RecognizeDocumentsRequest, [DocumentObservation])](./visionresult/recognizedocuments%28_,_%29.md)
### Getting the iterative and selected object result
- [case generateIterativeSegmentation(GenerateIterativeSegmentationRequest, PixelBufferObservation?)](./visionresult/generateiterativesegmentation%28_,_%29.md)
### Getting the image aesthetics and lens smudge result
- [case calculateImageAestheticsScores(CalculateImageAestheticsScoresRequest, ImageAestheticsScoresObservation)](./visionresult/calculateimageaestheticsscores%28_,_%29.md)
  A result from performing a calculate image aesthetics scores request.
- [case detectLensSmudge(DetectLensSmudgeRequest, SmudgeObservation)](./visionresult/detectlenssmudge%28_,_%29.md)
### Getting the saliency result
- [case generateObjectnessBasedSaliencyImage(GenerateObjectnessBasedSaliencyImageRequest, SaliencyImageObservation)](./visionresult/generateobjectnessbasedsaliencyimage%28_,_%29.md)
  A result from performing a generate objectness based saliency image request.
- [case generateAttentionBasedSaliencyImage(GenerateAttentionBasedSaliencyImageRequest, SaliencyImageObservation)](./visionresult/generateattentionbasedsaliencyimage%28_,_%29.md)
  A result from performing a generate attention based saliency image request.
### Getting the object-tracking result
- [case trackRectangle(TrackRectangleRequest, RectangleObservation?)](./visionresult/trackrectangle%28_,_%29.md)
  A result from performing a track rectangle request.
- [case trackObject(TrackObjectRequest, DetectedObjectObservation?)](./visionresult/trackobject%28_,_%29.md)
  A result from performing a track object request.
### Getting the face and body detection result
- [case detectFaceCaptureQuality(DetectFaceCaptureQualityRequest, [FaceObservation])](./visionresult/detectfacecapturequality%28_,_%29.md)
  A result from performing a detect face capture quality request.
- [case detectFaceLandmarks(DetectFaceLandmarksRequest, [FaceObservation])](./visionresult/detectfacelandmarks%28_,_%29.md)
  A result from performing a detect face landmarks request.
- [case detectFaceRectangles(DetectFaceRectanglesRequest, [FaceObservation])](./visionresult/detectfacerectangles%28_,_%29.md)
  A result from performing a detect face rectangles request.
- [case detectHumanRectangles(DetectHumanRectanglesRequest, [HumanObservation])](./visionresult/detecthumanrectangles%28_,_%29.md)
  A result from performing a detect human rectangles request.
### Getting the body and hand pose detection result
- [case detectHumanBodyPose(DetectHumanBodyPoseRequest, [HumanBodyPoseObservation])](./visionresult/detecthumanbodypose%28_,_%29.md)
  A result from performing a detect human body pose request.
- [case detectHumanHandPose(DetectHumanHandPoseRequest, [HumanHandPoseObservation])](./visionresult/detecthumanhandpose%28_,_%29.md)
  A result from performing a detect human hand pose request.
- [case detectHumanBodyPose3D(DetectHumanBodyPose3DRequest, [HumanBodyPose3DObservation])](./visionresult/detecthumanbodypose3d%28_,_%29.md)
  A result from performing a 3D detect human body pose request.
### Getting the animal detection result
- [case recognizeAnimals(RecognizeAnimalsRequest, [RecognizedObjectObservation])](./visionresult/recognizeanimals%28_,_%29.md)
  A result from performing a recognize animals request.
- [case detectAnimalBodyPose(DetectAnimalBodyPoseRequest, [AnimalBodyPoseObservation])](./visionresult/detectanimalbodypose%28_,_%29.md)
  A result from performing a detect animal body pose request.
### Getting the text result
- [case detectTextRectangles(DetectTextRectanglesRequest, [TextObservation])](./visionresult/detecttextrectangles%28_,_%29.md)
  A result from performing a detect text rectangles request.
- [case recognizeText(RecognizeTextRequest, [RecognizedTextObservation])](./visionresult/recognizetext%28_,_%29.md)
  A result from performing a recognize text request.
### Getting the image alignment, feature print, and background removal result
- [case trackTranslationalImageRegistration(TrackTranslationalImageRegistrationRequest, ImageTranslationAlignmentObservation)](./visionresult/tracktranslationalimageregistration%28_,_%29.md)
  A result from performing a track translational image request.
- [case trackHomographicImageRegistration(TrackHomographicImageRegistrationRequest, ImageHomographicAlignmentObservation)](./visionresult/trackhomographicimageregistration%28_,_%29.md)
  A result from performing a track homographic image request.
- [case generateForegroundInstanceMask(GenerateForegroundInstanceMaskRequest, InstanceMaskObservation?)](./visionresult/generateforegroundinstancemask%28_,_%29.md)
  A result from performing a generate foreground instance mask request.
- [case generateImageFeaturePrint(GenerateImageFeaturePrintRequest, FeaturePrintObservation)](./visionresult/generateimagefeatureprint%28_,_%29.md)
  A result from performing a generate image feature print request.
### Getting the trajectory, contour, and horizon detection result
- [case detectTrajectories(DetectTrajectoriesRequest, [TrajectoryObservation])](./visionresult/detecttrajectories%28_,_%29.md)
  A result from performing a detect trajectories request.
- [case detectContours(DetectContoursRequest, ContoursObservation)](./visionresult/detectcontours%28_,_%29.md)
  A result from performing a detect contours request.
- [case detectHorizon(DetectHorizonRequest, HorizonObservation?)](./visionresult/detecthorizon%28_,_%29.md)
  A result from performing a detect horizon request.
### Getting the optical flow, rectangle and barcode detection result
- [case trackOpticalFlow(TrackOpticalFlowRequest, OpticalFlowObservation?)](./visionresult/trackopticalflow%28_,_%29.md)
  A result from performing a track optical flow request.
- [case detectRectangles(DetectRectanglesRequest, [RectangleObservation])](./visionresult/detectrectangles%28_,_%29.md)
  A result from performing a detect rectangles request.
- [case detectBarcodes(DetectBarcodesRequest, [BarcodeObservation])](./visionresult/detectbarcodes%28_,_%29.md)
  A result from performing a detect barcodes request.
### Getting the machine learning image-analysis result
- [case coreML(CoreMLRequest, [any VisionObservation])](./visionresult/coreml%28_,_%29.md)
  A result from performing a Core ML request.
### Getting the error result
- [case error(any VisionRequest, any Error)](./visionresult/error%28_,_%29.md)
  A result from encountering a framework error.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Performing the request
- [associatedtype Result](./visionrequest/result.md)
  An associated type that represents the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionresult)*