# VNFaceLandmarks2D

**Framework**: Vision  
**Kind**: class

A collection of facial features that a request detects.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNFaceLandmarks2D
```

#### Overview

This class represents the set of all detectable 2D face landmarks and regions, exposed as properties. The coordinates of the face landmarks are normalized to the dimensions of the face observation’s [`boundingBox`](vndetectedobjectobservation/boundingbox.md), with the origin at the bounding box’s lower-left corner. Use the [`VNImagePointForFaceLandmarkPoint(_:_:_:_:)`](vnimagepointforfacelandmarkpoint(_:_:_:_:).md) function to convert normalized face landmark points into absolute points within the image’s coordinate system.

## Topics

### Face Landmark Points
- [var allPoints: VNFaceLandmarkRegion2D?](vnfacelandmarks2d/allpoints.md)
  The region containing all face landmark points.
- [var faceContour: VNFaceLandmarkRegion2D?](vnfacelandmarks2d/facecontour.md)
  The region containing points that trace the face contour from the left cheek, over the chin, to the right cheek.
- [var leftEye: VNFaceLandmarkRegion2D?](vnfacelandmarks2d/lefteye.md)
  The region containing points that outline the left eye.
- [var rightEye: VNFaceLandmarkRegion2D?](vnfacelandmarks2d/righteye.md)
  The region containing points that outline the right eye.
- [var leftEyebrow: VNFaceLandmarkRegion2D?](vnfacelandmarks2d/lefteyebrow.md)
  The region containing points that trace the left eyebrow.
- [var rightEyebrow: VNFaceLandmarkRegion2D?](vnfacelandmarks2d/righteyebrow.md)
  The region containing points that trace the right eyebrow.
- [var nose: VNFaceLandmarkRegion2D?](vnfacelandmarks2d/nose.md)
  The region containing points that outline the nose.
- [var noseCrest: VNFaceLandmarkRegion2D?](vnfacelandmarks2d/nosecrest.md)
  The region containing points that trace the center crest of the nose.
- [var medianLine: VNFaceLandmarkRegion2D?](vnfacelandmarks2d/medianline.md)
  The region containing points that trace a vertical line down the center of the face.
- [var outerLips: VNFaceLandmarkRegion2D?](vnfacelandmarks2d/outerlips.md)
  The region containing points that outline the outside of the lips.
- [var innerLips: VNFaceLandmarkRegion2D?](vnfacelandmarks2d/innerlips.md)
  The region containing points that outline the space between the lips.
- [var leftPupil: VNFaceLandmarkRegion2D?](vnfacelandmarks2d/leftpupil.md)
  The region containing the point where the left pupil is located.
- [var rightPupil: VNFaceLandmarkRegion2D?](vnfacelandmarks2d/rightpupil.md)
  The region containing the point where the right pupil is located.

## Relationships

### Inherits From
- [VNFaceLandmarks](vnfacelandmarks.md)
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
- [class VNFaceLandmarkRegion2D](vnfacelandmarkregion2d.md)
  2D geometry information for a specific facial feature.
- [class VNFaceLandmarks](vnfacelandmarks.md)
  The abstract superclass for containers of face landmark information.
- [class VNFaceLandmarkRegion](vnfacelandmarkregion.md)
  The abstract superclass for information about a specific face landmark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfacelandmarks2d)*