# movingAverageRadius

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The moving average radius of the object the request is tracking.

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
let movingAverageRadius: CGFloat
```

## See Also

### Inspecting an observation
- [let detectedPoints: [NormalizedPoint]](./detectedpoints.md)
  The centroid points of the detected contour along the trajectory.
- [let projectedPoints: [NormalizedPoint]](./projectedpoints.md)
  The centroids of the calculated trajectory from the detected points.
- [let equationCoefficients: simd_float3](./equationcoefficients.md)
  The coefficients of the parabolic equation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/trajectoryobservation/movingaverageradius)*