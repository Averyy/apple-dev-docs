# normalizedPath

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The contour object as a path in normalized coordinates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var normalizedPath: CGPath { get }
```

```objc
@property (readonly) CGPathRef normalizedPath;
```

## See Also

### Inspecting the Contour
- [var aspectRatio: Float](./aspectratio.md)
  The aspect ratio of the contour.
- [var indexPath: IndexPath](./indexpath.md)
  The contour object’s index path.
- [var pointCount: Int](./pointcount.md)
  The contour’s number of points.
- [var normalizedPoints: [simd_float2]](./normalizedpoints-8n2s5.md)
  The contour’s array of points in normalized coordinates.
- [func polygonApproximation(epsilon: Float) throws -> VNContour](./polygonapproximation%28epsilon%29.md)
  Simplifies the contour to a polygon using a Ramer-Douglas-Peucker algorithm.
- [normalizedPoints](./normalizedpoints-2orqj.md)
  The contour’s array of points in normalized coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontour/normalizedpath)*