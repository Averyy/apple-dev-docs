# CoordinateOrigin

**Framework**: Vision  
**Kind**: enum

The origin of a coordinate system relative to an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum CoordinateOrigin
```

## Topics

### Getting the origins
- [CoordinateOrigin.upperLeft](coordinateorigin/upperleft.md)
  The origin at the upper-left corner of the image.
- [CoordinateOrigin.lowerLeft](coordinateorigin/lowerleft.md)
  The origin at the lower-left corner of the image.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct NormalizedPoint](normalizedpoint.md)
  A point in a 2D coordinate system.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/coordinateorigin)*