# VNRequestRevisionProviding

**Framework**: Vision  
**Kind**: protocol

A protocol for specifying the revision number of Vision algorithms.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
protocol VNRequestRevisionProviding
```

#### Overview

Subclasses of [`VNRequest`](vnrequest.md) should adopt this protocol to specify which revision of an algorithm the Vision framework uses to generate requests.

## Topics

### Specifying Revision Number
- [var requestRevision: Int](vnrequestrevisionproviding/requestrevision.md)
  The revision of the [`VNRequest`](vnrequest.md) subclass used to generate the implementing object.
### Determining Revision Type
- [let VNRequestRevisionUnspecified: Int](vnrequestrevisionunspecified.md)
  A constant for specifying an unspecified request revision.
- [let VNDetectRectanglesRequestRevision1: Int](vndetectrectanglesrequestrevision1.md)
  A constant for specifying revision 1 of the rectangle detection request.
- [let VNTrackRectangleRequestRevision1: Int](vntrackrectanglerequestrevision1.md)
  A constant for specifying revision 1 of the rectangling tracking request.
- [let VNTrackObjectRequestRevision1: Int](vntrackobjectrequestrevision1.md)
  A constant for specifying revision 1 of the object tracking request.
- [let VNDetectFaceRectanglesRequestRevision2: Int](vndetectfacerectanglesrequestrevision2.md)
  A constant for specifying revision 2 of the face rectangles detection request.
- [let VNDetectFaceRectanglesRequestRevision1: Int](vndetectfacerectanglesrequestrevision1.md)
  A constant for specifying revision 1 of the face rectangles detection request.
- [let VNDetectFaceLandmarksRequestRevision3: Int](vndetectfacelandmarksrequestrevision3.md)
  A constant for specifying revision 3 of the face landmarks detection request.
- [let VNDetectFaceLandmarksRequestRevision2: Int](vndetectfacelandmarksrequestrevision2.md)
  A constant for specifying revision 2 of the face landmarks detection request.
- [let VNDetectFaceLandmarksRequestRevision1: Int](vndetectfacelandmarksrequestrevision1.md)
  A constant for specifying revision 1 of the face landmarks detection request.
- [let VNRecognizeTextRequestRevision1: Int](vnrecognizetextrequestrevision1.md)
  A constant for specifying revision 1 of the text recognition request.
- [let VNDetectTextRectanglesRequestRevision1: Int](vndetecttextrectanglesrequestrevision1.md)
  A constant for specifying revision 1 of the text rectangles detection request.
- [let VNDetectBarcodesRequestRevision1: Int](vndetectbarcodesrequestrevision1.md)
  A constant for specifying revision 1 of the barcode detection request.
- [let VNDetectHorizonRequestRevision1: Int](vndetecthorizonrequestrevision1.md)
  A constant for specifying revision 1 of the horizon detection request.
- [let VNTranslationalImageRegistrationRequestRevision1: Int](vntranslationalimageregistrationrequestrevision1.md)
  A constant for specifying revision 1 of the translational image registration request.
- [let VNHomographicImageRegistrationRequestRevision1: Int](vnhomographicimageregistrationrequestrevision1.md)
  A constant for specifying revision 1 of the homographic image registration request.
- [let VNCoreMLRequestRevision1: Int](vncoremlrequestrevision1.md)
  A constant for specifying revision 1 of a Core ML request.
- [let VNGenerateAttentionBasedSaliencyImageRequestRevision1: Int](vngenerateattentionbasedsaliencyimagerequestrevision1.md)
  A constant for specifying revision 1 of the image saliency request.
- [let VNGenerateObjectnessBasedSaliencyImageRequestRevision1: Int](vngenerateobjectnessbasedsaliencyimagerequestrevision1.md)
  A constant for specifying revision 1 of the image saliency request.
- [let VNClassifyImageRequestRevision1: Int](vnclassifyimagerequestrevision1.md)
  A constant for specifying the first revision of the image-classification request.
- [let VNGenerateImageFeaturePrintRequestRevision1: Int](vngenerateimagefeatureprintrequestrevision1.md)
  A constant for specifying the first revision of the feature-print request.
- [let VNDetectFaceCaptureQualityRequestRevision1: Int](vndetectfacecapturequalityrequestrevision1.md)
  A constant for specifying revision 1 of the face capture detection request.
- [let VNDetectHumanRectanglesRequestRevision1: Int](vndetecthumanrectanglesrequestrevision1.md)
  A constant for specifying revision 1 of the human rectangles detection request.

## Relationships

### Conforming Types
- [VNAnimalBodyPoseObservation](vnanimalbodyposeobservation.md)
- [VNBarcodeObservation](vnbarcodeobservation.md)
- [VNClassificationObservation](vnclassificationobservation.md)
- [VNContour](vncontour.md)
- [VNContoursObservation](vncontoursobservation.md)
- [VNCoreMLFeatureValueObservation](vncoremlfeaturevalueobservation.md)
- [VNDetectedObjectObservation](vndetectedobjectobservation.md)
- [VNFaceLandmarkRegion](vnfacelandmarkregion.md)
- [VNFaceLandmarkRegion2D](vnfacelandmarkregion2d.md)
- [VNFaceLandmarks](vnfacelandmarks.md)
- [VNFaceLandmarks2D](vnfacelandmarks2d.md)
- [VNFaceObservation](vnfaceobservation.md)
- [VNFeaturePrintObservation](vnfeatureprintobservation.md)
- [VNHorizonObservation](vnhorizonobservation.md)
- [VNHumanBodyPose3DObservation](vnhumanbodypose3dobservation.md)
- [VNHumanBodyPoseObservation](vnhumanbodyposeobservation.md)
- [VNHumanHandPoseObservation](vnhumanhandposeobservation.md)
- [VNHumanObservation](vnhumanobservation.md)
- [VNImageAestheticsScoresObservation](vnimageaestheticsscoresobservation.md)
- [VNImageAlignmentObservation](vnimagealignmentobservation.md)
- [VNImageHomographicAlignmentObservation](vnimagehomographicalignmentobservation.md)
- [VNImageTranslationAlignmentObservation](vnimagetranslationalignmentobservation.md)
- [VNInstanceMaskObservation](vninstancemaskobservation.md)
- [VNObservation](vnobservation.md)
- [VNPixelBufferObservation](vnpixelbufferobservation.md)
- [VNRecognizedObjectObservation](vnrecognizedobjectobservation.md)
- [VNRecognizedPoints3DObservation](vnrecognizedpoints3dobservation.md)
- [VNRecognizedPointsObservation](vnrecognizedpointsobservation.md)
- [VNRecognizedText](vnrecognizedtext.md)
- [VNRecognizedTextObservation](vnrecognizedtextobservation.md)
- [VNRectangleObservation](vnrectangleobservation.md)
- [VNSaliencyImageObservation](vnsaliencyimageobservation.md)
- [VNTextObservation](vntextobservation.md)
- [VNTrajectoryObservation](vntrajectoryobservation.md)

## See Also

- [class var currentRevision: Int](vnrequest/currentrevision.md)
  The current revison supported by the request.
- [class var defaultRevision: Int](vnrequest/defaultrevision.md)
  The revision of the latest request for the particular SDK linked with the client application.
- [class var supportedRevisions: IndexSet](vnrequest/supportedrevisions.md)
  The collection of currently-supported algorithm versions for the class of request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequestrevisionproviding)*