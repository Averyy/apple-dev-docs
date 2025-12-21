# TrackObjectRequest

**Framework**: Vision  
**Kind**: class

An image-analysis request that tracks the movement of a previously identified object across multiple images or video frames.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final class TrackObjectRequest
```

#### Overview

Use this type of request to track the bounding boxes around objects previously identified in an image. Vision attempts to locate the same object from the input observation throughout the sequence. The request returns the resulting rectangle data in an instance of [`RectangleObservation`](rectangleobservation.md).

## Topics

### Creating a request
- [init(detectedObject: any BoundingBoxProviding & VisionObservation, TrackObjectRequest.Revision?, frameAnalysisSpacing: CMTime?)](trackobjectrequest/init(detectedobject:_:frameanalysisspacing:).md)
  Creates an object tracking request.
- [protocol BoundingBoxProviding](boundingboxproviding.md)
  A protocol for objects that have a bounding box.
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
- [struct DetectedObjectObservation](detectedobjectobservation.md)
  An observation that provides the position and extent of an image feature that an image-analysis request detects.
### Configuring a request
- [let inputObservation: any BoundingBoxProviding & VisionObservation](trackobjectrequest/inputobservation.md)
  The object to track.
### Getting the revision
- [let revision: TrackObjectRequest.Revision](trackobjectrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [TrackObjectRequest.Revision]](trackobjectrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [TrackObjectRequest.Revision](trackobjectrequest/revision-swift.enum.md)
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

- [class DetectTrajectoriesRequest](detecttrajectoriesrequest.md)
  A request that detects the trajectories of shapes moving along a parabolic path.
- [class TrackOpticalFlowRequest](trackopticalflowrequest.md)
  A request that determines the direction change of vectors for each pixel from a previous to current image.
- [class TrackRectangleRequest](trackrectanglerequest.md)
  An image-analysis request that tracks movement of a previously identified rectangular object across multiple images or video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/trackobjectrequest)*