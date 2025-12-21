# boundingQuad

**Framework**: Vision  
**Kind**: property

The bounding quadrilateral of the region.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var boundingQuad: RectangleObservation { get }
```

## See Also

- [var aspectRatio: Float](contoursobservation/contour/aspectratio.md)
  The aspect ratio of the contour, which is the image’s width divided by its height.
- [var boundingBox: NormalizedRect](contoursobservation/contour/boundingbox.md)
  The bounding box of the region.
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
- [var points: [NormalizedPoint]](contoursobservation/contour/points.md)
  The points of the region as an array of `NormalizedPoint`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/contoursobservation/contour/boundingquad)*