# QuadrilateralProviding

**Framework**: Vision  
**Kind**: protocol

A protocol for objects that have a bounding quadrilateral.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
protocol QuadrilateralProviding : BoundingBoxProviding
```

## Topics

### Getting the normalized points
- [var bottomLeft: NormalizedPoint](quadrilateralproviding/bottomleft.md)
  The coordinates of the lower-left corner of the quadrilateral.
- [var bottomRight: NormalizedPoint](quadrilateralproviding/bottomright.md)
  The coordinates of the lower-right corner of quadrilateral.
- [var topLeft: NormalizedPoint](quadrilateralproviding/topleft.md)
  The coordinates of the upper-left corner of the quadrilateral.
- [var topRight: NormalizedPoint](quadrilateralproviding/topright.md)
  The coordinates of the upper-right corner of the quadrilateral.

## Relationships

### Inherits From
- [BoundingBoxProviding](boundingboxproviding.md)
### Conforming Types
- [BarcodeObservation](barcodeobservation.md)
- [DetectedDocumentObservation](detecteddocumentobservation.md)
- [RecognizedTextObservation](recognizedtextobservation.md)
- [RectangleObservation](rectangleobservation.md)
- [TextObservation](textobservation.md)

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
- [enum CoordinateOrigin](coordinateorigin.md)
  The origin of a coordinate system relative to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/quadrilateralproviding)*