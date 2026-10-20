# polygonApproximation(epsilon:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Simplifies the contour to a polygon using a Ramer-Douglas-Peucker algorithm.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func polygonApproximation(epsilon: Float) throws -> VNContour
```

```objc
- (VNContour *) polygonApproximationWithEpsilon:(float) epsilon error:(NSError **) error;
```

#### Return Value

A simplified polygon contour from the points of the original contour.

## Parameters

- `epsilon`: This parameter defines the distance threshold the algorithm uses. It preserves points whose perpendicular distance to the line segment they are on is greater than `epsilon`, and removes all others.

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
- [var normalizedPoints: [simd_float2]](./normalizedpoints-8n2s5.md)
  The contour’s array of points in normalized coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontour/polygonapproximation(epsilon:))*