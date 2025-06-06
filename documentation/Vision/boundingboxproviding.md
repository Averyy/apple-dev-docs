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

- [init(detectedObject: any BoundingBoxProviding & VisionObservation, TrackObjectRequest.Revision?, frameAnalysisSpacing: CMTime?)](trackobjectrequest/init(detectedobject:_:frameanalysisspacing:).md)
  Creates an object tracking request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/boundingboxproviding)*