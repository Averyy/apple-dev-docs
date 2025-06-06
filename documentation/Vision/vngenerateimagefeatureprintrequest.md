# VNGenerateImageFeaturePrintRequest

**Framework**: Vision  
**Kind**: class

An image-based request to generate feature prints from an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class VNGenerateImageFeaturePrintRequest
```

#### Overview

This request returns the feature print data it generates as an array of [`VNFeaturePrintObservation`](vnfeatureprintobservation.md) objects.

## Topics

### Scaling and Cropping Images
- [var imageCropAndScaleOption: VNImageCropAndScaleOption](vngenerateimagefeatureprintrequest/imagecropandscaleoption.md)
  An optional setting that tells the algorithm how to scale an input image before generating the feature print.
- [enum VNImageCropAndScaleOption](vnimagecropandscaleoption.md)
  Options that define how Vision crops and scales an input-image.
### Accessing the Results
- [var results: [VNFeaturePrintObservation]?](vngenerateimagefeatureprintrequest/results.md)
  The results of the feature print request.
- [class VNFeaturePrintObservation](vnfeatureprintobservation.md)
  An observation that provides the recognized feature print.
### Identifying Request Revisions
- [let VNGenerateImageFeaturePrintRequestRevision1: Int](vngenerateimagefeatureprintrequestrevision1.md)
  A constant for specifying the first revision of the feature-print request.

## Relationships

### Inherits From
- [VNImageBasedRequest](vnimagebasedrequest.md)
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
- [class VNImageBasedRequest](vnimagebasedrequest.md)
  The abstract superclass for image-analysis requests that focus on a specific part of an image.
- [class VNClassifyImageRequest](vnclassifyimagerequest.md)
  A request to classify an image.
- [class VNFeaturePrintObservation](vnfeatureprintobservation.md)
  An observation that provides the recognized feature print.
- [class VNImageRequestHandler](vnimagerequesthandler.md)
  An object that processes one or more image-analysis request pertaining to a single image.
- [class VNObservation](vnobservation.md)
  The abstract superclass for analysis results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngenerateimagefeatureprintrequest)*