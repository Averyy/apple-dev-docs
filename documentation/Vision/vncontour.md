# VNContour

**Framework**: Vision  
**Kind**: class

A class that represents a detected contour in an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNContour
```

## Topics

### Inspecting the Contour
- [var aspectRatio: Float](vncontour/aspectratio.md)
  The aspect ratio of the contour.
- [var indexPath: IndexPath](vncontour/indexpath.md)
  The contour object’s index path.
- [var normalizedPath: CGPath](vncontour/normalizedpath.md)
  The contour object as a path in normalized coordinates.
- [var pointCount: Int](vncontour/pointcount.md)
  The contour’s number of points.
- [var normalizedPoints: [simd_float2]](vncontour/normalizedpoints-8n2s5.md)
  The contour’s array of points in normalized coordinates.
- [func polygonApproximation(epsilon: Float) throws -> VNContour](vncontour/polygonapproximation(epsilon:).md)
  Simplifies the contour to a polygon using a Ramer-Douglas-Peucker algorithm.
### Accessing Child Contours
- [var childContourCount: Int](vncontour/childcontourcount.md)
  The total number of detected child contours.
- [var childContours: [VNContour]](vncontour/childcontours.md)
  An array of contours that this contour encloses.
- [func childContour(at: Int) throws -> VNContour](vncontour/childcontour(at:).md)
  Retrieves the child contour object at the specified index.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [var contourCount: Int](vncontoursobservation/contourcount.md)
  The total number of detected contours.
- [var normalizedPath: CGPath](vncontoursobservation/normalizedpath.md)
  The detected contours as a path object in normalized coordinates.
- [var topLevelContours: [VNContour]](vncontoursobservation/toplevelcontours.md)
  An array of contours that don’t have another contour enclosing them.
- [var topLevelContourCount: Int](vncontoursobservation/toplevelcontourcount.md)
  The total number of detected top-level contours.
- [func contour(at: Int) throws -> VNContour](vncontoursobservation/contour(at:)-9on0y.md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.
- [func contour(at: IndexPath) throws -> VNContour](vncontoursobservation/contour(at:)-52odo.md)
  Retrieves the contour object at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontour)*