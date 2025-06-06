# VNClassifyImageRequest

**Framework**: Vision  
**Kind**: class

A request to classify an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class VNClassifyImageRequest
```

#### Overview

This type of request produces a collection of [`VNClassificationObservation`](vnclassificationobservation.md) objects that describe an image. Access the classifications through [`knownClassifications(forRevision:)`](vnclassifyimagerequest/knownclassifications(forrevision:).md).

## Topics

### Accessing Results
- [func supportedIdentifiers() throws -> [String]](vnclassifyimagerequest/supportedidentifiers.md)
  Returns the classification identifiers that the request supports in its current configuration.
- [var results: [VNClassificationObservation]?](vnclassifyimagerequest/results.md)
  The results of the image classification request.
- [class VNClassificationObservation](vnclassificationobservation.md)
  An object that represents classification information that an image-analysis request produces.
- [class func knownClassifications(forRevision: Int) throws -> [VNClassificationObservation]](vnclassifyimagerequest/knownclassifications(forrevision:).md)
  Requests the collection of classifications that the Vision framework recognizes.
### Specifying Algorithm Revision
- [let VNClassifyImageRequestRevision1: Int](vnclassifyimagerequestrevision1.md)
  A constant for specifying the first revision of the image-classification request.

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
- [class VNGenerateImageFeaturePrintRequest](vngenerateimagefeatureprintrequest.md)
  An image-based request to generate feature prints from an image.
- [class VNFeaturePrintObservation](vnfeatureprintobservation.md)
  An observation that provides the recognized feature print.
- [class VNImageRequestHandler](vnimagerequesthandler.md)
  An object that processes one or more image-analysis request pertaining to a single image.
- [class VNObservation](vnobservation.md)
  The abstract superclass for analysis results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnclassifyimagerequest)*