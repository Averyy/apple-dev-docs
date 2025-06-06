# VNObservation

**Framework**: Vision  
**Kind**: class

The abstract superclass for analysis results.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNObservation
```

#### Overview

Observations resulting from Vision image analysis requests inherit from this abstract base class. Don’t use this abstract superclass directly.

## Topics

### Tracking Observations
- [var uuid: UUID](vnobservation/uuid.md)
  A unique identifier assigned to the Vision observation.
### Evaluating Observations
- [var timeRange: CMTimeRange](vnobservation/timerange.md)
  The time range of the reported observation.
- [var confidence: VNConfidence](vnobservation/confidence.md)
  The level of confidence in the observation’s accuracy.
- [typealias VNConfidence](vnconfidence.md)
  A type alias for the confidence value of an observation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VNClassificationObservation](vnclassificationobservation.md)
- [VNContoursObservation](vncontoursobservation.md)
- [VNCoreMLFeatureValueObservation](vncoremlfeaturevalueobservation.md)
- [VNDetectedObjectObservation](vndetectedobjectobservation.md)
- [VNFeaturePrintObservation](vnfeatureprintobservation.md)
- [VNHorizonObservation](vnhorizonobservation.md)
- [VNImageAestheticsScoresObservation](vnimageaestheticsscoresobservation.md)
- [VNImageAlignmentObservation](vnimagealignmentobservation.md)
- [VNInstanceMaskObservation](vninstancemaskobservation.md)
- [VNPixelBufferObservation](vnpixelbufferobservation.md)
- [VNRecognizedPoints3DObservation](vnrecognizedpoints3dobservation.md)
- [VNRecognizedPointsObservation](vnrecognizedpointsobservation.md)
- [VNTrajectoryObservation](vntrajectoryobservation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [Detecting Objects in Still Images](detecting-objects-in-still-images.md)
  Locate and demarcate rectangles, faces, barcodes, and text in images using the Vision framework.
- [Classifying images for categorization and search](classifying-images-for-categorization-and-search.md)
  Analyze and label images using a Vision classification request.
- [Analyzing Image Similarity with Feature Print](analyzing-image-similarity-with-feature-print.md)
  Generate a feature print to compute distance between images.
- [class VNRequest](vnrequest.md)
  The abstract superclass for analysis requests.
- [class VNImageBasedRequest](vnimagebasedrequest.md)
  The abstract superclass for image-analysis requests that focus on a specific part of an image.
- [class VNClassifyImageRequest](vnclassifyimagerequest.md)
  A request to classify an image.
- [class VNGenerateImageFeaturePrintRequest](vngenerateimagefeatureprintrequest.md)
  An image-based request to generate feature prints from an image.
- [class VNFeaturePrintObservation](vnfeatureprintobservation.md)
  An observation that provides the recognized feature print.
- [class VNImageRequestHandler](vnimagerequesthandler.md)
  An object that processes one or more image-analysis request pertaining to a single image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnobservation)*