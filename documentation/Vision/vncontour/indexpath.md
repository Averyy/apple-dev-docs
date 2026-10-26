# indexPath

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The contour object’s index path.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var indexPath: IndexPath { get }
```

```objc
@property (readonly) NSIndexPath * indexPath;
```

## See Also

### Inspecting the Contour
- [var aspectRatio: Float](./aspectratio.md)
  The aspect ratio of the contour.
- [var normalizedPath: CGPath](./normalizedpath.md)
  The contour object as a path in normalized coordinates.
- [var pointCount: Int](./pointcount.md)
  The contour’s number of points.
- [var normalizedPoints: [simd_float2]](./normalizedpoints-8n2s5.md)
  The contour’s array of points in normalized coordinates.
- [func polygonApproximation(epsilon: Float) throws -> VNContour](./polygonapproximation%28epsilon%29.md)
  Simplifies the contour to a polygon using a Ramer-Douglas-Peucker algorithm.
- [normalizedPoints](./normalizedpoints-2orqj.md)
  The contour’s array of points in normalized coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontour/indexpath)*