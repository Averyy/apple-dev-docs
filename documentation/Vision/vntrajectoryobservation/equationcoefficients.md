# equationCoefficients

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) simd_float3 equationCoefficients;
```

#### Discussion

This equation describes the parabola on which the detected contour is traveling. The equation and the projected points get refined over time.

## See Also

### Evaluating an Observation
- [var detectedPoints: [VNPoint]](./detectedpoints.md)
  The centroid points of the detected contour along the trajectory.
- [var projectedPoints: [VNPoint]](./projectedpoints.md)
  The centroids of the calculated trajectory from the detected points.
- [var movingAverageRadius: CGFloat](./movingaverageradius.md)
  The moving average radius of the object the request is tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrajectoryobservation/equationcoefficients)*