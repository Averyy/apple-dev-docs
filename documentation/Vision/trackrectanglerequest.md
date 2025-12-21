# TrackRectangleRequest

**Framework**: Vision  
**Kind**: class

An image-analysis request that tracks movement of a previously identified rectangular object across multiple images or video frames.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final class TrackRectangleRequest
```

#### Overview

Use this type of request to track the bounding boxes of rectangles throughout a sequence of images. Vision returns locations for rectangles found in all orientations and sizes. The request returns the resulting rectangle data in an instance of [`RectangleObservation`](rectangleobservation.md).

## Topics

### Creating a request
- [init(detectedRectangle: any QuadrilateralProviding & VisionObservation, TrackRectangleRequest.Revision?, frameAnalysisSpacing: CMTime?)](trackrectanglerequest/init(detectedrectangle:_:frameanalysisspacing:).md)
  Creates a rectangle tracking request.
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
- [struct RectangleObservation](rectangleobservation.md)
  An object that represents the four vertices of a detected rectangle.
### Configuring a request
- [let inputObservation: any QuadrilateralProviding & VisionObservation](trackrectanglerequest/inputobservation.md)
  The object to track.
- [protocol QuadrilateralProviding](quadrilateralproviding.md)
  A protocol for objects that have a bounding quadrilateral.
- [var trackingLevel: TrackRectangleRequest.TrackingLevel](trackrectanglerequest/trackinglevel-swift.property.md)
  The tracking quality preference.
- [TrackRectangleRequest.TrackingLevel](trackrectanglerequest/trackinglevel-swift.enum.md)
### Getting the revision
- [let revision: TrackRectangleRequest.Revision](trackrectanglerequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [TrackRectangleRequest.Revision]](trackrectanglerequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [TrackRectangleRequest.Revision](trackrectanglerequest/revision-swift.enum.md)
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
- [class TrackObjectRequest](trackobjectrequest.md)
  An image-analysis request that tracks the movement of a previously identified object across multiple images or video frames.
- [class TrackOpticalFlowRequest](trackopticalflowrequest.md)
  A request that determines the direction change of vectors for each pixel from a previous to current image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/trackrectanglerequest)*