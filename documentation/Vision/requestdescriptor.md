# RequestDescriptor

**Framework**: Vision  
**Kind**: enum

A type that describes the request and revision combination.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum RequestDescriptor
```

## Topics

### Getting the still-image descriptor
- [case classifyImageRequest(ClassifyImageRequest.Revision)](requestdescriptor/classifyimagerequest(_:).md)
  A descriptor that describes a classify image request.
### Getting the image sequence descriptor
- [case detectDocumentSegmentationRequest(DetectDocumentSegmentationRequest.Revision)](requestdescriptor/detectdocumentsegmentationrequest(_:).md)
  A descriptor that describes a detect document segmentation request.
- [case generatePersonInstanceMaskRequest(GeneratePersonInstanceMaskRequest.Revision)](requestdescriptor/generatepersoninstancemaskrequest(_:).md)
  A descriptor that describes a generate person instance mask request.
- [case generatePersonSegmentationRequest(GeneratePersonSegmentationRequest.Revision)](requestdescriptor/generatepersonsegmentationrequest(_:).md)
  A descriptor that describes a generate person segmentation request.
### Getting the image aesthetics descriptor
- [case calculateImageAestheticsScoresRequest(CalculateImageAestheticsScoresRequest.Revision)](requestdescriptor/calculateimageaestheticsscoresrequest(_:).md)
  A descriptor that describes a calculate image aesthetics scores request.
### Getting the saliency descriptor
- [case generateAttentionBasedSaliencyImageRequest(GenerateAttentionBasedSaliencyImageRequest.Revision)](requestdescriptor/generateattentionbasedsaliencyimagerequest(_:).md)
  A descriptor that describes a generate attention based saliency image request.
- [case generateObjectnessBasedSaliencyImageRequest(GenerateObjectnessBasedSaliencyImageRequest.Revision)](requestdescriptor/generateobjectnessbasedsaliencyimagerequest(_:).md)
  A descriptor that describes a generate objectness based saliency image request.
### Getting the object-tracking descriptor
- [case trackObjectRequest(TrackObjectRequest.Revision)](requestdescriptor/trackobjectrequest(_:).md)
  A descriptor that describes a track object request.
- [case trackRectangleRequest(TrackRectangleRequest.Revision)](requestdescriptor/trackrectanglerequest(_:).md)
  A descriptor that describes a track rectangles request.
### Getting the face and body detection descriptor
- [case detectFaceCaptureQualityRequest(DetectFaceCaptureQualityRequest.Revision)](requestdescriptor/detectfacecapturequalityrequest(_:).md)
  A descriptor that describes a detect face capture quality request.
- [case detectFaceLandmarksRequest(DetectFaceLandmarksRequest.Revision)](requestdescriptor/detectfacelandmarksrequest(_:).md)
  A descriptor that describes a detect face landmarks request.
- [case detectFaceRectanglesRequest(DetectFaceRectanglesRequest.Revision)](requestdescriptor/detectfacerectanglesrequest(_:).md)
  A descriptor that describes a detect face rectangles request.
- [case detectHumanRectanglesRequest(DetectHumanRectanglesRequest.Revision)](requestdescriptor/detecthumanrectanglesrequest(_:).md)
  A descriptor that describes a detect human rectangles request.
### Getting the body and hand pose detection descriptor
- [case detectHumanBodyPoseRequest(DetectHumanBodyPoseRequest.Revision)](requestdescriptor/detecthumanbodyposerequest(_:).md)
  A descriptor that describes a detect human body pose request.
- [case detectHumanHandPoseRequest(DetectHumanHandPoseRequest.Revision)](requestdescriptor/detecthumanhandposerequest(_:).md)
  A descriptor that describes a detect human hand pose request.
- [case detectHumanBodyPose3DRequest(DetectHumanBodyPose3DRequest.Revision)](requestdescriptor/detecthumanbodypose3drequest(_:).md)
  A descriptor that describes a 3D detect human body pose request.
### Getting the animal detection descriptor
- [case detectAnimalBodyPoseRequest(DetectAnimalBodyPoseRequest.Revision)](requestdescriptor/detectanimalbodyposerequest(_:).md)
  A descriptor that describes a detect animal body pose request.
- [case recognizeAnimalsRequest(RecognizeAnimalsRequest.Revision)](requestdescriptor/recognizeanimalsrequest(_:).md)
  A descriptor that describes a recognize animals request.
### Getting the text descriptor
- [case detectTextRectanglesRequest(DetectTextRectanglesRequest.Revision)](requestdescriptor/detecttextrectanglesrequest(_:).md)
  A descriptor that describes a detect text rectangles request.
- [case recognizeTextRequest(RecognizeTextRequest.Revision)](requestdescriptor/recognizetextrequest(_:).md)
  A descriptor that describes a recognize text request.
### Getting the image alignment, feature print, and background removal descriptor
- [case trackTranslationalImageRegistrationRequest(TrackTranslationalImageRegistrationRequest.Revision)](requestdescriptor/tracktranslationalimageregistrationrequest(_:).md)
  A descriptor that describes a track translational image request.
- [case trackHomographicImageRegistrationRequest(TrackHomographicImageRegistrationRequest.Revision)](requestdescriptor/trackhomographicimageregistrationrequest(_:).md)
  A descriptor that describes a track homographic image request.
- [case generateForegroundInstanceMaskRequest(GenerateForegroundInstanceMaskRequest.Revision)](requestdescriptor/generateforegroundinstancemaskrequest(_:).md)
  A descriptor that describes a generate foreground instance mask request.
- [case generateImageFeaturePrintRequest(GenerateImageFeaturePrintRequest.Revision)](requestdescriptor/generateimagefeatureprintrequest(_:).md)
  A descriptor that describes a generate image feature print request.
### Getting the trajectory, contour, and horizon detection descriptor
- [case detectTrajectoriesRequest(DetectTrajectoriesRequest.Revision)](requestdescriptor/detecttrajectoriesrequest(_:).md)
  A descriptor that describes a detect trajectories request.
- [case detectContoursRequest(DetectContoursRequest.Revision)](requestdescriptor/detectcontoursrequest(_:).md)
  A descriptor that describes a detect contours request.
- [case detectHorizonRequest(DetectHorizonRequest.Revision)](requestdescriptor/detecthorizonrequest(_:).md)
  A descriptor that describes a detect horizon request.
### Getting the optical flow, rectangle and barcode detection descriptor
- [case trackOpticalFlowRequest(TrackOpticalFlowRequest.Revision)](requestdescriptor/trackopticalflowrequest(_:).md)
  A descriptor that describes a track optical flow request.
- [case detectRectanglesRequest(DetectRectanglesRequest.Revision)](requestdescriptor/detectrectanglesrequest(_:).md)
  A descriptor that describes a detect rectangles request.
- [case detectBarcodesRequest(DetectBarcodesRequest.Revision)](requestdescriptor/detectbarcodesrequest(_:).md)
  A descriptor that describes a detect barcodes request.
### Getting the machine learning image-analysis descriptor
- [case coreMLRequest(CoreMLRequest.Revision)](requestdescriptor/coremlrequest(_:).md)
  A descriptor that describes a Core ML request.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var hasPrecisionRecallCurve: Bool](classificationobservation/hasprecisionrecallcurve.md)
  A Boolean value that indicates whether the observation contains precision and recall curves.
- [let identifier: String](classificationobservation/identifier.md)
  The classification label that identifies the type of observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/requestdescriptor)*