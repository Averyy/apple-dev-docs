# DetectContoursRequest

**Framework**: Vision  
**Kind**: struct

A request that detects the contours of the edges of an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct DetectContoursRequest
```

#### Overview

This request generates a [`ContoursObservation`](contoursobservation.md) object that describes the contours in an image.

## Topics

### Creating a request
- [init(DetectContoursRequest.Revision?)](detectcontoursrequest/init(_:).md)
  Creates a contour-detection request.
### Getting the revision
- [let revision: DetectContoursRequest.Revision](detectcontoursrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectContoursRequest.Revision]](detectcontoursrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [DetectContoursRequest.Revision](detectcontoursrequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.
### Inspecting a request
- [var contrastAdjustment: Float](detectcontoursrequest/contrastadjustment.md)
  The amount by which to adjust the image contrast.
- [var contrastPivot: Float?](detectcontoursrequest/contrastpivot.md)
  The pixel value to use as a pivot for the contrast.
- [var detectsDarkOnLight: Bool](detectcontoursrequest/detectsdarkonlight.md)
  A Boolean value that indicates whether the request detects a dark object on a light background to aid in detection.
- [var maximumImageDimension: Int](detectcontoursrequest/maximumimagedimension.md)
  The maximum image dimension to use for contour detection.
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
- [struct ContoursObservation](contoursobservation.md)
  An object that represents the detected contours in an image.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ImageProcessingRequest](imageprocessingrequest.md)
- [Sendable](../Swift/Sendable.md)
- [VisionRequest](visionrequest.md)

## See Also

- [class DetectTrajectoriesRequest](detecttrajectoriesrequest.md)
  A request that detects the trajectories of shapes moving along a parabolic path.
- [struct DetectHorizonRequest](detecthorizonrequest.md)
  An image-analysis request that determines the horizon angle in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectcontoursrequest)*