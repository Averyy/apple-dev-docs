# RequestDescriptor

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

A type that describes the request and revision combination.

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
enum RequestDescriptor
```

## Topics

### Getting the still-image descriptor
- [case classifyImageRequest(ClassifyImageRequest.Revision)](./requestdescriptor/classifyimagerequest%28_%29.md)
  A descriptor that describes a classify image request.
- [case detectLensSmudgeRequest(DetectLensSmudgeRequest.Revision)](./requestdescriptor/detectlenssmudgerequest%28_%29.md)
  A descriptor that describes a detect lens smudge request.
### Getting the image sequence descriptor
- [case detectDocumentSegmentationRequest(DetectDocumentSegmentationRequest.Revision)](./requestdescriptor/detectdocumentsegmentationrequest%28_%29.md)
  A descriptor that describes a detect document segmentation request.
- [case recognizeDocumentsRequest(RecognizeDocumentsRequest.Revision)](./requestdescriptor/recognizedocumentsrequest%28_%29.md)
- [case generatePersonInstanceMaskRequest(GeneratePersonInstanceMaskRequest.Revision)](./requestdescriptor/generatepersoninstancemaskrequest%28_%29.md)
  A descriptor that describes a generate person instance mask request.
- [case generatePersonSegmentationRequest(GeneratePersonSegmentationRequest.Revision)](./requestdescriptor/generatepersonsegmentationrequest%28_%29.md)
  A descriptor that describes a generate person segmentation request.
### Getting the iterative and selected object descriptor
- [case generateIterativeSegmentationRequest(GenerateIterativeSegmentationRequest.Revision)](./requestdescriptor/generateiterativesegmentationrequest%28_%29.md)
### Getting the image aesthetics descriptor
- [case calculateImageAestheticsScoresRequest(CalculateImageAestheticsScoresRequest.Revision)](./requestdescriptor/calculateimageaestheticsscoresrequest%28_%29.md)
  A descriptor that describes a calculate image aesthetics scores request.
### Getting the saliency descriptor
- [case generateAttentionBasedSaliencyImageRequest(GenerateAttentionBasedSaliencyImageRequest.Revision)](./requestdescriptor/generateattentionbasedsaliencyimagerequest%28_%29.md)
  A descriptor that describes a generate attention based saliency image request.
- [case generateObjectnessBasedSaliencyImageRequest(GenerateObjectnessBasedSaliencyImageRequest.Revision)](./requestdescriptor/generateobjectnessbasedsaliencyimagerequest%28_%29.md)
  A descriptor that describes a generate objectness based saliency image request.
### Getting the object-tracking descriptor
- [case trackObjectRequest(TrackObjectRequest.Revision)](./requestdescriptor/trackobjectrequest%28_%29.md)
  A descriptor that describes a track object request.
- [case trackRectangleRequest(TrackRectangleRequest.Revision)](./requestdescriptor/trackrectanglerequest%28_%29.md)
  A descriptor that describes a track rectangles request.
### Getting the face and body detection descriptor
- [case detectFaceCaptureQualityRequest(DetectFaceCaptureQualityRequest.Revision)](./requestdescriptor/detectfacecapturequalityrequest%28_%29.md)
  A descriptor that describes a detect face capture quality request.
- [case detectFaceLandmarksRequest(DetectFaceLandmarksRequest.Revision)](./requestdescriptor/detectfacelandmarksrequest%28_%29.md)
  A descriptor that describes a detect face landmarks request.
- [case detectFaceRectanglesRequest(DetectFaceRectanglesRequest.Revision)](./requestdescriptor/detectfacerectanglesrequest%28_%29.md)
  A descriptor that describes a detect face rectangles request.
- [case detectHumanRectanglesRequest(DetectHumanRectanglesRequest.Revision)](./requestdescriptor/detecthumanrectanglesrequest%28_%29.md)
  A descriptor that describes a detect human rectangles request.
### Getting the body and hand pose detection descriptor
- [case detectHumanBodyPoseRequest(DetectHumanBodyPoseRequest.Revision)](./requestdescriptor/detecthumanbodyposerequest%28_%29.md)
  A descriptor that describes a detect human body pose request.
- [case detectHumanHandPoseRequest(DetectHumanHandPoseRequest.Revision)](./requestdescriptor/detecthumanhandposerequest%28_%29.md)
  A descriptor that describes a detect human hand pose request.
- [case detectHumanBodyPose3DRequest(DetectHumanBodyPose3DRequest.Revision)](./requestdescriptor/detecthumanbodypose3drequest%28_%29.md)
  A descriptor that describes a 3D detect human body pose request.
### Getting the animal detection descriptor
- [case detectAnimalBodyPoseRequest(DetectAnimalBodyPoseRequest.Revision)](./requestdescriptor/detectanimalbodyposerequest%28_%29.md)
  A descriptor that describes a detect animal body pose request.
- [case recognizeAnimalsRequest(RecognizeAnimalsRequest.Revision)](./requestdescriptor/recognizeanimalsrequest%28_%29.md)
  A descriptor that describes a recognize animals request.
### Getting the text descriptor
- [case detectTextRectanglesRequest(DetectTextRectanglesRequest.Revision)](./requestdescriptor/detecttextrectanglesrequest%28_%29.md)
  A descriptor that describes a detect text rectangles request.
- [case recognizeTextRequest(RecognizeTextRequest.Revision)](./requestdescriptor/recognizetextrequest%28_%29.md)
  A descriptor that describes a recognize text request.
### Getting the image alignment, feature print, and background removal descriptor
- [case trackTranslationalImageRegistrationRequest(TrackTranslationalImageRegistrationRequest.Revision)](./requestdescriptor/tracktranslationalimageregistrationrequest%28_%29.md)
  A descriptor that describes a track translational image request.
- [case trackHomographicImageRegistrationRequest(TrackHomographicImageRegistrationRequest.Revision)](./requestdescriptor/trackhomographicimageregistrationrequest%28_%29.md)
  A descriptor that describes a track homographic image request.
- [case generateForegroundInstanceMaskRequest(GenerateForegroundInstanceMaskRequest.Revision)](./requestdescriptor/generateforegroundinstancemaskrequest%28_%29.md)
  A descriptor that describes a generate foreground instance mask request.
- [case generateImageFeaturePrintRequest(GenerateImageFeaturePrintRequest.Revision)](./requestdescriptor/generateimagefeatureprintrequest%28_%29.md)
  A descriptor that describes a generate image feature print request.
### Getting the trajectory, contour, and horizon detection descriptor
- [case detectTrajectoriesRequest(DetectTrajectoriesRequest.Revision)](./requestdescriptor/detecttrajectoriesrequest%28_%29.md)
  A descriptor that describes a detect trajectories request.
- [case detectContoursRequest(DetectContoursRequest.Revision)](./requestdescriptor/detectcontoursrequest%28_%29.md)
  A descriptor that describes a detect contours request.
- [case detectHorizonRequest(DetectHorizonRequest.Revision)](./requestdescriptor/detecthorizonrequest%28_%29.md)
  A descriptor that describes a detect horizon request.
### Getting the optical flow, rectangle and barcode detection descriptor
- [case trackOpticalFlowRequest(TrackOpticalFlowRequest.Revision)](./requestdescriptor/trackopticalflowrequest%28_%29.md)
  A descriptor that describes a track optical flow request.
- [case detectRectanglesRequest(DetectRectanglesRequest.Revision)](./requestdescriptor/detectrectanglesrequest%28_%29.md)
  A descriptor that describes a detect rectangles request.
- [case detectBarcodesRequest(DetectBarcodesRequest.Revision)](./requestdescriptor/detectbarcodesrequest%28_%29.md)
  A descriptor that describes a detect barcodes request.
### Getting the machine learning image-analysis descriptor
- [case coreMLRequest(CoreMLRequest.Revision)](./requestdescriptor/coremlrequest%28_%29.md)
  A descriptor that describes a Core ML request.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting an observation
- [var uuid: UUID](./visionobservation/uuid.md)
  A unique alphanumeric value that the framework assigns the observation.
- [var confidence: Float](./visionobservation/confidence.md)
  The level of confidence in the observation’s accuracy.
- [var description: String](./visionobservation/description.md)
  A textual representation of this instance.
- [var originatingRequestDescriptor: RequestDescriptor?](./visionobservation/originatingrequestdescriptor.md)
  The descriptor of the request that produces the observation.
- [var timeRange: CMTimeRange?](./visionobservation/timerange.md)
  The time range of the reported observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/requestdescriptor)*