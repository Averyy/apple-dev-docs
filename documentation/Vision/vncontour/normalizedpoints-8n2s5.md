# normalizedPoints

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The contour’s array of points in normalized coordinates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
@nonobjc
var normalizedPoints: [simd_float2] { get }
```

#### Discussion

This property value provides the address of the buffer that contain the array of [`CGPoint`](../../CoreFoundation/cgpoint.md) values.

## See Also

### Inspecting the Contour
- [var aspectRatio: Float](./aspectratio.md)
  The aspect ratio of the contour.
- [var indexPath: IndexPath](./indexpath.md)
  The contour object’s index path.
- [var normalizedPath: CGPath](./normalizedpath.md)
  The contour object as a path in normalized coordinates.
- [var pointCount: Int](./pointcount.md)
  The contour’s number of points.
- [func polygonApproximation(epsilon: Float) throws -> VNContour](./polygonapproximation%28epsilon%29.md)
  Simplifies the contour to a polygon using a Ramer-Douglas-Peucker algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontour/normalizedpoints-8n2s5)*