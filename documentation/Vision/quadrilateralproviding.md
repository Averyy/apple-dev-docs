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

- [let inputObservation: any QuadrilateralProviding & VisionObservation](trackrectanglerequest/inputobservation.md)
  The object to track.
- [var trackingLevel: TrackRectangleRequest.TrackingLevel](trackrectanglerequest/trackinglevel-swift.property.md)
  The tracking quality preference.
- [TrackRectangleRequest.TrackingLevel](trackrectanglerequest/trackinglevel-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/quadrilateralproviding)*