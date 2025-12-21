# VisionResult

**Framework**: Vision  
**Kind**: enum

The result the framework produces by performing a request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum VisionResult
```

#### Overview

Each result contains the original [`VisionRequest`](visionrequest.md), along with any observations produced.

## Topics

### Getting the still-image result
- [case classifyImage(ClassifyImageRequest, [ClassificationObservation])](visionresult/classifyimage(_:_:).md)
  A result from performing a classify image request.
### Getting the image sequence result
- [case generatePersonInstanceMask(GeneratePersonInstanceMaskRequest, InstanceMaskObservation?)](visionresult/generatepersoninstancemask(_:_:).md)
  A result from performing a generate person instance mask request.
- [case generatePersonSegmentation(GeneratePersonSegmentationRequest, PixelBufferObservation)](visionresult/generatepersonsegmentation(_:_:).md)
  A result from performing a generate person segmentation request.
- [case detectDocumentSegmentation(DetectDocumentSegmentationRequest, DetectedDocumentObservation?)](visionresult/detectdocumentsegmentation(_:_:).md)
  A result from performing a detect document segmentation request.
- [case recognizeDocuments(RecognizeDocumentsRequest, [DocumentObservation])](visionresult/recognizedocuments(_:_:).md)
### Getting the image aesthetics and lens smudge result
- [case calculateImageAestheticsScores(CalculateImageAestheticsScoresRequest, ImageAestheticsScoresObservation)](visionresult/calculateimageaestheticsscores(_:_:).md)
  A result from performing a calculate image aesthetics scores request.
- [case detectLensSmudge(DetectLensSmudgeRequest, SmudgeObservation)](visionresult/detectlenssmudge(_:_:).md)
### Getting the saliency result
- [case generateObjectnessBasedSaliencyImage(GenerateObjectnessBasedSaliencyImageRequest, SaliencyImageObservation)](visionresult/generateobjectnessbasedsaliencyimage(_:_:).md)
  A result from performing a generate objectness based saliency image request.
- [case generateAttentionBasedSaliencyImage(GenerateAttentionBasedSaliencyImageRequest, SaliencyImageObservation)](visionresult/generateattentionbasedsaliencyimage(_:_:).md)
  A result from performing a generate attention based saliency image request.
### Getting the object-tracking result
- [case trackRectangle(TrackRectangleRequest, RectangleObservation?)](visionresult/trackrectangle(_:_:).md)
  A result from performing a track rectangle request.
- [case trackObject(TrackObjectRequest, DetectedObjectObservation?)](visionresult/trackobject(_:_:).md)
  A result from performing a track object request.
### Getting the face and body detection result
- [case detectFaceCaptureQuality(DetectFaceCaptureQualityRequest, [FaceObservation])](visionresult/detectfacecapturequality(_:_:).md)
  A result from performing a detect face capture quality request.
- [case detectFaceLandmarks(DetectFaceLandmarksRequest, [FaceObservation])](visionresult/detectfacelandmarks(_:_:).md)
  A result from performing a detect face landmarks request.
- [case detectFaceRectangles(DetectFaceRectanglesRequest, [FaceObservation])](visionresult/detectfacerectangles(_:_:).md)
  A result from performing a detect face rectangles request.
- [case detectHumanRectangles(DetectHumanRectanglesRequest, [HumanObservation])](visionresult/detecthumanrectangles(_:_:).md)
  A result from performing a detect human rectangles request.
### Getting the body and hand pose detection result
- [case detectHumanBodyPose(DetectHumanBodyPoseRequest, [HumanBodyPoseObservation])](visionresult/detecthumanbodypose(_:_:).md)
  A result from performing a detect human body pose request.
- [case detectHumanHandPose(DetectHumanHandPoseRequest, [HumanHandPoseObservation])](visionresult/detecthumanhandpose(_:_:).md)
  A result from performing a detect human hand pose request.
- [case detectHumanBodyPose3D(DetectHumanBodyPose3DRequest, [HumanBodyPose3DObservation])](visionresult/detecthumanbodypose3d(_:_:).md)
  A result from performing a 3D detect human body pose request.
### Getting the animal detection result
- [case recognizeAnimals(RecognizeAnimalsRequest, [RecognizedObjectObservation])](visionresult/recognizeanimals(_:_:).md)
  A result from performing a recognize animals request.
- [case detectAnimalBodyPose(DetectAnimalBodyPoseRequest, [AnimalBodyPoseObservation])](visionresult/detectanimalbodypose(_:_:).md)
  A result from performing a detect animal body pose request.
### Getting the text result
- [case detectTextRectangles(DetectTextRectanglesRequest, [TextObservation])](visionresult/detecttextrectangles(_:_:).md)
  A result from performing a detect text rectangles request.
- [case recognizeText(RecognizeTextRequest, [RecognizedTextObservation])](visionresult/recognizetext(_:_:).md)
  A result from performing a recognize text request.
### Getting the image alignment, feature print, and background removal result
- [case trackTranslationalImageRegistration(TrackTranslationalImageRegistrationRequest, ImageTranslationAlignmentObservation)](visionresult/tracktranslationalimageregistration(_:_:).md)
  A result from performing a track translational image request.
- [case trackHomographicImageRegistration(TrackHomographicImageRegistrationRequest, ImageHomographicAlignmentObservation)](visionresult/trackhomographicimageregistration(_:_:).md)
  A result from performing a track homographic image request.
- [case generateForegroundInstanceMask(GenerateForegroundInstanceMaskRequest, InstanceMaskObservation?)](visionresult/generateforegroundinstancemask(_:_:).md)
  A result from performing a generate foreground instance mask request.
- [case generateImageFeaturePrint(GenerateImageFeaturePrintRequest, FeaturePrintObservation)](visionresult/generateimagefeatureprint(_:_:).md)
  A result from performing a generate image feature print request.
### Getting the trajectory, contour, and horizon detection result
- [case detectTrajectories(DetectTrajectoriesRequest, [TrajectoryObservation])](visionresult/detecttrajectories(_:_:).md)
  A result from performing a detect trajectories request.
- [case detectContours(DetectContoursRequest, ContoursObservation)](visionresult/detectcontours(_:_:).md)
  A result from performing a detect contours request.
- [case detectHorizon(DetectHorizonRequest, HorizonObservation?)](visionresult/detecthorizon(_:_:).md)
  A result from performing a detect horizon request.
### Getting the optical flow, rectangle and barcode detection result
- [case trackOpticalFlow(TrackOpticalFlowRequest, OpticalFlowObservation?)](visionresult/trackopticalflow(_:_:).md)
  A result from performing a track optical flow request.
- [case detectRectangles(DetectRectanglesRequest, [RectangleObservation])](visionresult/detectrectangles(_:_:).md)
  A result from performing a detect rectangles request.
- [case detectBarcodes(DetectBarcodesRequest, [BarcodeObservation])](visionresult/detectbarcodes(_:_:).md)
  A result from performing a detect barcodes request.
### Getting the machine learning image-analysis result
- [case coreML(CoreMLRequest, [any VisionObservation])](visionresult/coreml(_:_:).md)
  A result from performing a Core ML request.
### Getting the error result
- [case error(any VisionRequest, any Error)](visionresult/error(_:_:).md)
  A result from encountering a framework error.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [associatedtype Result](visionrequest/result.md)
  An associated type that represents the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionresult)*