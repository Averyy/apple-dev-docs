# projectedPoints

**Framework**: Vision  
**Kind**: property

The centroids of the calculated trajectory from the detected points.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var projectedPoints: [VNPoint] { get }
```

#### Discussion

The projected points define the ideal trajectory described by the parabolic equation. The equation’s coefficients and the projected points of the detected trajectory get refined over time. The system limits the maximum number of cached points to the maximum points needed to describe the trajectory together with the parabolic equation.

## See Also

- [var detectedPoints: [VNPoint]](vntrajectoryobservation/detectedpoints.md)
  The centroid points of the detected contour along the trajectory.
- [var equationCoefficients: simd_float3](vntrajectoryobservation/equationcoefficients.md)
  The coefficients of the parabolic equation.
- [var movingAverageRadius: CGFloat](vntrajectoryobservation/movingaverageradius.md)
  The moving average radius of the object the request is tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrajectoryobservation/projectedpoints)*