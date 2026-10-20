# ContoursObservation.Contour

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An object that represents a detected contour in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
struct Contour
```

## Topics

### Inspecting a contour
- [var aspectRatio: Float](./contour/aspectratio.md)
  The aspect ratio of the contour, which is the image’s width divided by its height.
- [var boundingBox: NormalizedRect](./contour/boundingbox.md)
  The bounding box of the region.
- [var boundingQuad: RectangleObservation](./contour/boundingquad.md)
  The bounding quadrilateral of the region.
- [var childContours: [ContoursObservation.Contour]](./contour/childcontours.md)
  An array of contours that this contour encloses.
- [var indexPath: IndexPath](./contour/indexpath.md)
  The contour object’s index path.
- [var normalizedPath: CGPath](./contour/normalizedpath.md)
  The contour object as a path in normalized coordinates.
- [var normalizedPoints: [simd_float2]](./contour/normalizedpoints.md)
  The contour’s array of points in normalized coordinates.
- [var pointCount: Int](./contour/pointcount.md)
  The contour’s number of points.
- [var points: [NormalizedPoint]](./contour/points.md)
  The points of the region as an array of `NormalizedPoint`.
### Calculating area and perimeter
- [func calculateArea(useOrientedArea: Bool) -> Double](./contour/calculatearea%28useorientedarea%29.md)
- [func calculatePerimeter() -> Double](./contour/calculateperimeter%28%29.md)
### Getting the bounding circle
- [func boundingCircle() -> NormalizedCircle](./contour/boundingcircle%28%29.md)
### Getting the approximation
- [func polygonApproximation(epsilon: Float) throws -> ContoursObservation.Contour](./contour/polygonapproximation%28epsilon%29.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the contours
- [func contourAtIndex(Int) -> ContoursObservation.Contour?](./contouratindex%28_%29.md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.
- [func countourAtIndexPath(IndexPath) -> ContoursObservation.Contour?](./countouratindexpath%28_%29.md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/contoursobservation/contour)*