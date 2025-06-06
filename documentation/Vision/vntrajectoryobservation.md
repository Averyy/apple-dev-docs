# VNTrajectoryObservation

**Framework**: Vision  
**Kind**: class

An observation that describes a detected trajectory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNTrajectoryObservation
```

## Mentions

- [Identifying Trajectories in Video](identifying-trajectories-in-video.md)

## Topics

### Evaluating an Observation
- [var detectedPoints: [VNPoint]](vntrajectoryobservation/detectedpoints.md)
  The centroid points of the detected contour along the trajectory.
- [var projectedPoints: [VNPoint]](vntrajectoryobservation/projectedpoints.md)
  The centroids of the calculated trajectory from the detected points.
- [var equationCoefficients: simd_float3](vntrajectoryobservation/equationcoefficients.md)
  The coefficients of the parabolic equation.
- [var movingAverageRadius: CGFloat](vntrajectoryobservation/movingaverageradius.md)
  The moving average radius of the object the request is tracking.

## Relationships

### Inherits From
- [VNObservation](vnobservation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [var results: [VNTrajectoryObservation]?](vndetecttrajectoriesrequest/results.md)
  The array of detected trajectory observations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrajectoryobservation)*