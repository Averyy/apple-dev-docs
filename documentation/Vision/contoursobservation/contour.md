# ContoursObservation.Contour

**Framework**: Vision  
**Kind**: struct

An object that represents a detected contour in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct Contour
```

## Topics

### Inspecting a contour
- [var aspectRatio: Float](contoursobservation/contour/aspectratio.md)
  The aspect ratio of the contour, which is the image’s width divided by its height.
- [var childContours: [ContoursObservation.Contour]](contoursobservation/contour/childcontours.md)
  An array of contours that this contour encloses.
- [var indexPath: IndexPath](contoursobservation/contour/indexpath.md)
  The contour object’s index path.
- [var normalizedPath: CGPath](contoursobservation/contour/normalizedpath.md)
  The contour object as a path in normalized coordinates.
- [var normalizedPoints: [simd_float2]](contoursobservation/contour/normalizedpoints.md)
  The contour’s array of points in normalized coordinates.
- [var pointCount: Int](contoursobservation/contour/pointcount.md)
  The contour’s number of points.
### Calculating area and perimeter
- [func calculateArea(useOrientedArea: Bool) -> Double](contoursobservation/contour/calculatearea(useorientedarea:).md)
- [func calculatePerimeter() -> Double](contoursobservation/contour/calculateperimeter.md)
### Getting the bounding circle
- [func boundingCircle() -> NormalizedCircle](contoursobservation/contour/boundingcircle.md)
### Getting the approximation
- [func polygonApproximation(epsilon: Float) throws -> ContoursObservation.Contour](contoursobservation/contour/polygonapproximation(epsilon:).md)
### Instance Properties
- [var boundingBox: NormalizedRect](contoursobservation/contour/boundingbox.md)
  The bounding box of the region.
- [var boundingQuad: RectangleObservation](contoursobservation/contour/boundingquad.md)
  The bounding quadrilateral of the region.
- [var points: [NormalizedPoint]](contoursobservation/contour/points.md)
  The points of the region as an array of `NormalizedPoint`.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func contourAtIndex(Int) -> ContoursObservation.Contour?](contoursobservation/contouratindex(_:).md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.
- [func countourAtIndexPath(IndexPath) -> ContoursObservation.Contour?](contoursobservation/countouratindexpath(_:).md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/contoursobservation/contour)*