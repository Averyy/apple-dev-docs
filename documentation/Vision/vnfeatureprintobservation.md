# VNFeaturePrintObservation

**Framework**: Vision  
**Kind**: class

An observation that provides the recognized feature print.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class VNFeaturePrintObservation
```

## Topics

### Fetching Feature Print Data
- [var data: Data](vnfeatureprintobservation/data.md)
  The feature print data.
- [var elementCount: Int](vnfeatureprintobservation/elementcount.md)
  The total number of elements in the data.
### Determining Types of Feature Prints
- [var elementType: VNElementType](vnfeatureprintobservation/elementtype.md)
  The type of each element in the data.
- [enum VNElementType](vnelementtype.md)
  An enumeration of the type of element in feature print data.
- [func VNElementTypeSize(VNElementType) -> Int](vnelementtypesize(_:).md)
  Returns the size of a feature print element.
### Computing Distance Between Features
- [func computeDistance(UnsafeMutablePointer<Float>, to: VNFeaturePrintObservation) throws](vnfeatureprintobservation/computedistance(_:to:).md)
  Computes the distance between two feature print observations.

## Relationships

### Inherits From
- [VNObservation](vnobservation.md)
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
- [class VNImageRequestHandler](vnimagerequesthandler.md)
  An object that processes one or more image-analysis request pertaining to a single image.
- [class VNObservation](vnobservation.md)
  The abstract superclass for analysis results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfeatureprintobservation)*