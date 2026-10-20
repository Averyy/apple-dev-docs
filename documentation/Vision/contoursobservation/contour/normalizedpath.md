# normalizedPath

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The contour object as a path in normalized coordinates.

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
var normalizedPath: CGPath { get }
```

## See Also

### Inspecting a contour
- [var aspectRatio: Float](./aspectratio.md)
  The aspect ratio of the contour, which is the image’s width divided by its height.
- [var boundingBox: NormalizedRect](./boundingbox.md)
  The bounding box of the region.
- [var boundingQuad: RectangleObservation](./boundingquad.md)
  The bounding quadrilateral of the region.
- [var childContours: [ContoursObservation.Contour]](./childcontours.md)
  An array of contours that this contour encloses.
- [var indexPath: IndexPath](./indexpath.md)
  The contour object’s index path.
- [var normalizedPoints: [simd_float2]](./normalizedpoints.md)
  The contour’s array of points in normalized coordinates.
- [var pointCount: Int](./pointcount.md)
  The contour’s number of points.
- [var points: [NormalizedPoint]](./points.md)
  The points of the region as an array of `NormalizedPoint`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/contoursobservation/contour/normalizedpath)*