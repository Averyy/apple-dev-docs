# NormalizedCircle

**Framework**: Vision  
**Kind**: struct

The center point and radius of a 2D circle.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct NormalizedCircle
```

## Topics

### Creating a normalized circle
- [init(center: NormalizedPoint, radius: CGFloat)](normalizedcircle/init(center:radius:).md)
  Creates a circle with the specified center and radius.
- [static var zero: NormalizedCircle](normalizedcircle/zero.md)
  A circle object centered at the origin, with a radius of zero.
### Inspecting a normalized circle
- [let center: NormalizedPoint](normalizedcircle/center.md)
  The circle’s center point.
- [let radius: CGFloat](normalizedcircle/radius.md)
  The circle’s radius.
### Determining whether the circle contains a point
- [func contains(NormalizedPoint) -> Bool](normalizedcircle/contains(_:).md)
  Returns a Boolean value that indicates whether this circle, including its boundary, contains the specified point.
- [func contains(NormalizedPoint, inCircumferentialRingOfWidth: CGFloat) -> Bool](normalizedcircle/contains(_:incircumferentialringofwidth:).md)
  Returns a Boolean value that indicates whether a ring around this circle’s circumference contains the specified point.
### Getting the bounding circle
- [static func boundingCircle(for: [NormalizedPoint]) -> NormalizedCircle](normalizedcircle/boundingcircle(for:).md)
  Creates the smallest circle that encloses the points you specify.

## See Also

- [struct NormalizedPoint](normalizedpoint.md)
  A point in a 2D coordinate system.
- [struct NormalizedRect](normalizedrect.md)
  The location and dimensions of a rectangle.
- [typealias NormalizedRegion](normalizedregion.md)
  A polygon composed of normalized points.
- [protocol BoundingBoxProviding](boundingboxproviding.md)
  A protocol for objects that have a bounding box.
- [protocol BoundingRegionProviding](boundingregionproviding.md)
  A protocol for objects that have a defined boundary in an image.
- [protocol QuadrilateralProviding](quadrilateralproviding.md)
  A protocol for objects that have a bounding quadrilateral.
- [enum CoordinateOrigin](coordinateorigin.md)
  The origin of a coordinate system relative to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedcircle)*