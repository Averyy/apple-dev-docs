# VNFaceLandmarkRegion2D

**Framework**: Vision  
**Kind**: class

2D geometry information for a specific facial feature.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNFaceLandmarkRegion2D
```

#### Overview

This class represents the set of all facial landmark regions in 2D, exposed as properties.

## Topics

### Describing Region Points
- [var pointsClassification: VNPointsClassification](vnfacelandmarkregion2d/pointsclassification.md)
  An enumeration that describes how to interpret the points the region provides.
- [enum VNPointsClassification](vnpointsclassification.md)
  The set of classifications that describe how to interpret the points the region provides.
### Specifying Region Properties
- [var normalizedPoints: [CGPoint]](vnfacelandmarkregion2d/normalizedpoints-7s7im.md)
  The array of normalized landmark points.
- [var precisionEstimatesPerPoint: [Float]?](vnfacelandmarkregion2d/precisionestimatesperpoint-5jl22.md)
  Requests an array of precision estimates for each landmark point.
### Computing Feature Points
- [func pointsInImage(imageSize: CGSize) -> [CGPoint]](vnfacelandmarkregion2d/pointsinimage(imagesize:).md)
  Returns an array containing landmark points in the coordinate space of the specified image size.

## Relationships

### Inherits From
- [VNFaceLandmarkRegion](vnfacelandmarkregion.md)
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

- [var landmarks: VNFaceLandmarks2D?](vnfaceobservation/landmarks.md)
  The facial features of the detected face.
- [class VNFaceLandmarks2D](vnfacelandmarks2d.md)
  A collection of facial features that a request detects.
- [class VNFaceLandmarks](vnfacelandmarks.md)
  The abstract superclass for containers of face landmark information.
- [class VNFaceLandmarkRegion](vnfacelandmarkregion.md)
  The abstract superclass for information about a specific face landmark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfacelandmarkregion2d)*