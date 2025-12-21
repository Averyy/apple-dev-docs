# NormalizedPoint

**Framework**: Vision  
**Kind**: struct

A point in a 2D coordinate system.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct NormalizedPoint
```

## Topics

### Creating a normalized point
- [init(x: CGFloat, y: CGFloat)](normalizedpoint/init(x:y:).md)
  Creates a point object with the specified coordinates.
- [init(normalizedPoint: CGPoint)](normalizedpoint/init(normalizedpoint:).md)
  Creates a point object from the specified Core Graphics point.
- [init(imagePoint: CGPoint, in: CGSize)](normalizedpoint/init(imagepoint:in:).md)
  Creates a normalized point from a point in an image coordinate space.
- [init(imagePoint: CGPoint, in: CGSize, normalizedTo: NormalizedRect)](normalizedpoint/init(imagepoint:in:normalizedto:).md)
  Creates a point normalized to a region of interest within an image.
- [static var zero: NormalizedPoint](normalizedpoint/zero.md)
  A point object that represents the origin.
### Inspecting a normalized point
- [let cgPoint: CGPoint](normalizedpoint/cgpoint.md)
  The Core Graphics point for this point.
- [var x: CGFloat](normalizedpoint/x.md)
  The x-coordinate.
- [var y: CGFloat](normalizedpoint/y.md)
  The y-coordinate.
### Converting points
- [func toImageCoordinates(from: NormalizedRect, imageSize: CGSize, origin: CoordinateOrigin) -> CGPoint](normalizedpoint/toimagecoordinates(from:imagesize:origin:).md)
  Converts a point normalized to a region within an image into full image coordinates.
- [func toImageCoordinates(CGSize, origin: CoordinateOrigin) -> CGPoint](normalizedpoint/toimagecoordinates(_:origin:).md)
  Converts a point in normalized coordinates into image coordinates.
### Flipping a normalized point
- [func verticallyFlipped() -> NormalizedPoint](normalizedpoint/verticallyflipped.md)
  Returns a normalized point with the origin flipped between the top and bottom of the image.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct NormalizedRect](normalizedrect.md)
  The location and dimensions of a rectangle.
- [typealias NormalizedRegion](normalizedregion.md)
  A polygon composed of normalized points.
- [struct NormalizedCircle](normalizedcircle.md)
  The center point and radius of a 2D circle.
- [protocol BoundingBoxProviding](boundingboxproviding.md)
  A protocol for objects that have a bounding box.
- [protocol BoundingRegionProviding](boundingregionproviding.md)
  A protocol for objects that have a defined boundary in an image.
- [protocol QuadrilateralProviding](quadrilateralproviding.md)
  A protocol for objects that have a bounding quadrilateral.
- [enum CoordinateOrigin](coordinateorigin.md)
  The origin of a coordinate system relative to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedpoint)*