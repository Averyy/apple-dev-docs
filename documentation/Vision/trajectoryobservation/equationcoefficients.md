# equationCoefficients

**Framework**: Vision  
**Kind**: property

The coefficients of the parabolic equation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let equationCoefficients: simd_float3
```

#### Discussion

This equation describes the parabola on which the detected contour is traveling. The equation and the projected points get refined over time.

## See Also

- [let detectedPoints: [NormalizedPoint]](trajectoryobservation/detectedpoints.md)
  The centroid points of the detected contour along the trajectory.
- [let projectedPoints: [NormalizedPoint]](trajectoryobservation/projectedpoints.md)
  The centroids of the calculated trajectory from the detected points.
- [let movingAverageRadius: CGFloat](trajectoryobservation/movingaverageradius.md)
  The moving average radius of the object the request is tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/trajectoryobservation/equationcoefficients)*