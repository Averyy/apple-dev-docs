# BoundingBoxProviding

**Framework**: Vision  
**Kind**: protocol

A protocol for objects that have a bounding box.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
protocol BoundingBoxProviding
```

## Topics

### Getting the bounding box
- [var boundingBox: NormalizedRect](boundingboxproviding/boundingbox.md)
  The bounding box of the object.

## Relationships

### Inherited By
- [QuadrilateralProviding](quadrilateralproviding.md)
### Conforming Types
- [BarcodeObservation](barcodeobservation.md)
- [DetectedDocumentObservation](detecteddocumentobservation.md)
- [DetectedObjectObservation](detectedobjectobservation.md)
- [FaceObservation](faceobservation.md)
- [HumanObservation](humanobservation.md)
- [RecognizedObjectObservation](recognizedobjectobservation.md)
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
- [protocol BoundingRegionProviding](boundingregionproviding.md)
  A protocol for objects that have a defined boundary in an image.
- [protocol QuadrilateralProviding](quadrilateralproviding.md)
  A protocol for objects that have a bounding quadrilateral.
- [enum CoordinateOrigin](coordinateorigin.md)
  The origin of a coordinate system relative to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/boundingboxproviding)*