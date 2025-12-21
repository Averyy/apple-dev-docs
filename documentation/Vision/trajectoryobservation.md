# TrajectoryObservation

**Framework**: Vision  
**Kind**: struct

An observation that describes a detected trajectory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct TrajectoryObservation
```

## Topics

### Creating an observation
- [init(VNTrajectoryObservation)](trajectoryobservation/init(_:).md)
  Creates a trajectory observation.
### Inspecting an observation
- [let detectedPoints: [NormalizedPoint]](trajectoryobservation/detectedpoints.md)
  The centroid points of the detected contour along the trajectory.
- [let projectedPoints: [NormalizedPoint]](trajectoryobservation/projectedpoints.md)
  The centroids of the calculated trajectory from the detected points.
- [let equationCoefficients: simd_float3](trajectoryobservation/equationcoefficients.md)
  The coefficients of the parabolic equation.
- [let movingAverageRadius: CGFloat](trajectoryobservation/movingaverageradius.md)
  The moving average radius of the object the request is tracking.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/trajectoryobservation)*