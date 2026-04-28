# detectedPoints

**Framework**: Vision  
**Kind**: property

The centroid points of the detected contour along the trajectory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let detectedPoints: [NormalizedPoint]
```

#### Discussion

The detected points may differ slightly from the ideal trajectory because they fall within the allowed tolerance. The system limits the maximum number of points based on the maximum trajectory length set in the request.

## See Also

- [let projectedPoints: [NormalizedPoint]](trajectoryobservation/projectedpoints.md)
  The centroids of the calculated trajectory from the detected points.
- [let equationCoefficients: simd_float3](trajectoryobservation/equationcoefficients.md)
  The coefficients of the parabolic equation.
- [let movingAverageRadius: CGFloat](trajectoryobservation/movingaverageradius.md)
  The moving average radius of the object the request is tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/trajectoryobservation/detectedpoints)*