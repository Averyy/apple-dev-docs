# DetectTrajectoriesRequest

**Framework**: Vision  
**Kind**: class

A request that detects the trajectories of shapes moving along a parabolic path.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final class DetectTrajectoriesRequest
```

#### Overview

After the request detects a trajectory, it produces a collection of [`TrajectoryObservation`](trajectoryobservation.md) objects that contain the shape’s detected points and an equation describing the parabola.

## Topics

### Creating a request
- [init(trajectoryLength: Int, DetectTrajectoriesRequest.Revision?, frameAnalysisSpacing: CMTime?)](detecttrajectoriesrequest/init(trajectorylength:_:frameanalysisspacing:).md)
  Creates a trajectory-detection request.
### Performing a request
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
### Understanding the result
- [struct TrajectoryObservation](trajectoryobservation.md)
  An observation that describes a detected trajectory.
### Configuring a request
- [var objectMaximumNormalizedRadius: Float](detecttrajectoriesrequest/objectmaximumnormalizedradius.md)
  The maximum radius of the bounding circle of the object to track.
- [var objectMinimumNormalizedRadius: Float](detecttrajectoriesrequest/objectminimumnormalizedradius.md)
  The minimum radius of the bounding circle of the object to track.
- [var targetFrameTime: CMTime](detecttrajectoriesrequest/targetframetime.md)
  The requested target frame time for processing trajectory detection.
- [let trajectoryLength: Int](detecttrajectoriesrequest/trajectorylength.md)
  The number of points to detect before calculating a trajectory.
### Getting the revision
- [let revision: DetectTrajectoriesRequest.Revision](detecttrajectoriesrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectTrajectoriesRequest.Revision]](detecttrajectoriesrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [DetectTrajectoriesRequest.Revision](detecttrajectoriesrequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ImageProcessingRequest](imageprocessingrequest.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [StatefulRequest](statefulrequest.md)
- [VisionRequest](visionrequest.md)

## See Also

- [class TrackObjectRequest](trackobjectrequest.md)
  An image-analysis request that tracks the movement of a previously identified object across multiple images or video frames.
- [class TrackOpticalFlowRequest](trackopticalflowrequest.md)
  A request that determines the direction change of vectors for each pixel from a previous to current image.
- [class TrackRectangleRequest](trackrectanglerequest.md)
  An image-analysis request that tracks movement of a previously identified rectangular object across multiple images or video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecttrajectoriesrequest)*