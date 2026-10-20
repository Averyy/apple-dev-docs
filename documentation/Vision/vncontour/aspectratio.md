# aspectRatio

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The aspect ratio of the contour.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var aspectRatio: Float { get }
```

```objc
@property (readonly) float aspectRatio;
```

#### Discussion

The aspect ratio is the original image’s width divided by its height.

## See Also

### Inspecting the Contour
- [var indexPath: IndexPath](./indexpath.md)
  The contour object’s index path.
- [var normalizedPath: CGPath](./normalizedpath.md)
  The contour object as a path in normalized coordinates.
- [var pointCount: Int](./pointcount.md)
  The contour’s number of points.
- [var normalizedPoints: [simd_float2]](./normalizedpoints-8n2s5.md)
  The contour’s array of points in normalized coordinates.
- [func polygonApproximation(epsilon: Float) throws -> VNContour](./polygonapproximation%28epsilon%29.md)
  Simplifies the contour to a polygon using a Ramer-Douglas-Peucker algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontour/aspectratio)*