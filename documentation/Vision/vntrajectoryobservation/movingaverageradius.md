# movingAverageRadius

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The moving average radius of the object the request is tracking.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var movingAverageRadius: CGFloat { get }
```

```objc
@property (nonatomic, assign, readonly) CGFloat movingAverageRadius;
```

## See Also

### Evaluating an Observation
- [var detectedPoints: [VNPoint]](./detectedpoints.md)
  The centroid points of the detected contour along the trajectory.
- [var projectedPoints: [VNPoint]](./projectedpoints.md)
  The centroids of the calculated trajectory from the detected points.
- [var equationCoefficients: simd_float3](./equationcoefficients.md)
  The coefficients of the parabolic equation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrajectoryobservation/movingaverageradius)*