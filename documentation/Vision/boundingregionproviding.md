# BoundingRegionProviding

**Framework**: Vision  
**Kind**: protocol

A protocol for objects that have a defined boundary in an image.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol BoundingRegionProviding
```

## Topics

### Getting the bounding region
- [var boundingRegion: NormalizedRegion](boundingregionproviding/boundingregion.md)
  A polygon that defines the boundary of an area in the image.

## Relationships

### Conforming Types
- [DocumentObservation.Container](documentobservation/container.md)
- [DocumentObservation.Container.DataDetectorMatch](documentobservation/container/datadetectormatch.md)
- [DocumentObservation.Container.List](documentobservation/container/list.md)
- [DocumentObservation.Container.Table](documentobservation/container/table.md)
- [DocumentObservation.Container.Text](documentobservation/container/text-swift.struct.md)

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
- [protocol QuadrilateralProviding](quadrilateralproviding.md)
  A protocol for objects that have a bounding quadrilateral.
- [enum CoordinateOrigin](coordinateorigin.md)
  The origin of a coordinate system relative to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/boundingregionproviding)*