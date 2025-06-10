# TrajectoryObservation

**Framework**: Vision  
**Kind**: struct

An observation that describes a detected trajectory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
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

## See Also

- [func perform(on: URL, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-80bya.md)
  Performs the request on an image URL and produces observations.
- [func perform(on: Data, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3f3f1.md)
  Performs the request on image data and produces observations.
- [func perform(on: CGImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-qxxx.md)
  Performs the request on a Core Graphics image and produces observations.
- [func perform(on: CVPixelBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-xspx.md)
  Performs the request on a pixel buffer and produces observations.
- [func perform(on: CMSampleBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3hddl.md)
  Performs the request on a Core Media buffer and produces observations.
- [func perform(on: CIImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-85ex1.md)
  Performs the request on a Core Image image and produces observations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/trajectoryobservation)*