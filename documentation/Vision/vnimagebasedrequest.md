# VNImageBasedRequest

**Framework**: Vision  
**Kind**: class

The abstract superclass for image-analysis requests that focus on a specific part of an image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNImageBasedRequest
```

#### Overview

Other Vision request handlers that operate on still images inherit from this abstract base class. Don’t use it directly.

## Topics

### Configuring a Request
- [var regionOfInterest: CGRect](vnimagebasedrequest/regionofinterest.md)
  The region of the image in which Vision will perform the request.

## Relationships

### Inherits From
- [VNRequest](vnrequest.md)
### Inherited By
- [VNCalculateImageAestheticsScoresRequest](vncalculateimageaestheticsscoresrequest.md)
- [VNClassifyImageRequest](vnclassifyimagerequest.md)
- [VNCoreMLRequest](vncoremlrequest.md)
- [VNDetectAnimalBodyPoseRequest](vndetectanimalbodyposerequest.md)
- [VNDetectBarcodesRequest](vndetectbarcodesrequest.md)
- [VNDetectContoursRequest](vndetectcontoursrequest.md)
- [VNDetectDocumentSegmentationRequest](vndetectdocumentsegmentationrequest.md)
- [VNDetectFaceCaptureQualityRequest](vndetectfacecapturequalityrequest.md)
- [VNDetectFaceLandmarksRequest](vndetectfacelandmarksrequest.md)
- [VNDetectFaceRectanglesRequest](vndetectfacerectanglesrequest.md)
- [VNDetectHorizonRequest](vndetecthorizonrequest.md)
- [VNDetectHumanBodyPoseRequest](vndetecthumanbodyposerequest.md)
- [VNDetectHumanHandPoseRequest](vndetecthumanhandposerequest.md)
- [VNDetectHumanRectanglesRequest](vndetecthumanrectanglesrequest.md)
- [VNDetectRectanglesRequest](vndetectrectanglesrequest.md)
- [VNDetectTextRectanglesRequest](vndetecttextrectanglesrequest.md)
- [VNGenerateAttentionBasedSaliencyImageRequest](vngenerateattentionbasedsaliencyimagerequest.md)
- [VNGenerateForegroundInstanceMaskRequest](vngenerateforegroundinstancemaskrequest.md)
- [VNGenerateImageFeaturePrintRequest](vngenerateimagefeatureprintrequest.md)
- [VNGenerateObjectnessBasedSaliencyImageRequest](vngenerateobjectnessbasedsaliencyimagerequest.md)
- [VNGeneratePersonInstanceMaskRequest](vngeneratepersoninstancemaskrequest.md)
- [VNRecognizeAnimalsRequest](vnrecognizeanimalsrequest.md)
- [VNRecognizeTextRequest](vnrecognizetextrequest.md)
- [VNStatefulRequest](vnstatefulrequest.md)
- [VNTargetedImageRequest](vntargetedimagerequest.md)
- [VNTrackingRequest](vntrackingrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Detecting Objects in Still Images](detecting-objects-in-still-images.md)
  Locate and demarcate rectangles, faces, barcodes, and text in images using the Vision framework.
- [Classifying images for categorization and search](classifying-images-for-categorization-and-search.md)
  Analyze and label images using a Vision classification request.
- [Analyzing Image Similarity with Feature Print](analyzing-image-similarity-with-feature-print.md)
  Generate a feature print to compute distance between images.
- [class VNRequest](vnrequest.md)
  The abstract superclass for analysis requests.
- [class VNClassifyImageRequest](vnclassifyimagerequest.md)
  A request to classify an image.
- [class VNGenerateImageFeaturePrintRequest](vngenerateimagefeatureprintrequest.md)
  An image-based request to generate feature prints from an image.
- [class VNFeaturePrintObservation](vnfeatureprintobservation.md)
  An observation that provides the recognized feature print.
- [class VNImageRequestHandler](vnimagerequesthandler.md)
  An object that processes one or more image-analysis request pertaining to a single image.
- [class VNObservation](vnobservation.md)
  The abstract superclass for analysis results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimagebasedrequest)*