# equationCoefficients

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The coefficients of the parabolic equation.

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
let equationCoefficients: simd_float3
```

## Discussion

This equation describes the parabola on which the detected contour is traveling. The equation and the projected points get refined over time.

## See Also

### Inspecting an observation
- [let detectedPoints: [NormalizedPoint]](./detectedpoints.md)
  The centroid points of the detected contour along the trajectory.
- [let projectedPoints: [NormalizedPoint]](./projectedpoints.md)
  The centroids of the calculated trajectory from the detected points.
- [let movingAverageRadius: CGFloat](./movingaverageradius.md)
  The moving average radius of the object the request is tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/trajectoryobservation/equationcoefficients)*