# equationCoefficients

**Framework**: Vision  
**Kind**: property

The coefficients of the parabolic equation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var equationCoefficients: simd_float3 { get }
```

#### Discussion

This equation describes the parabola on which the detected contour is traveling. The equation and the projected points get refined over time.

## See Also

- [var detectedPoints: [VNPoint]](vntrajectoryobservation/detectedpoints.md)
  The centroid points of the detected contour along the trajectory.
- [var projectedPoints: [VNPoint]](vntrajectoryobservation/projectedpoints.md)
  The centroids of the calculated trajectory from the detected points.
- [var movingAverageRadius: CGFloat](vntrajectoryobservation/movingaverageradius.md)
  The moving average radius of the object the request is tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrajectoryobservation/equationcoefficients)*