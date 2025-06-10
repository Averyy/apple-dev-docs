# DetectHumanRectanglesRequest

**Framework**: Vision  
**Kind**: struct

A request that finds rectangular regions that contain people in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct DetectHumanRectanglesRequest
```

#### Overview

The request returns the resulting rectangle data in a collection of [`HumanObservation`](humanobservation.md) objects.

## Topics

### Creating a request
- [init(DetectHumanRectanglesRequest.Revision?)](detecthumanrectanglesrequest/init(_:).md)
  Creates a human detection request.
### Getting the revision
- [let revision: DetectHumanRectanglesRequest.Revision](detecthumanrectanglesrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectHumanRectanglesRequest.Revision]](detecthumanrectanglesrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [DetectHumanRectanglesRequest.Revision](detecthumanrectanglesrequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.
### Inspecting a request
- [var upperBodyOnly: Bool](detecthumanrectanglesrequest/upperbodyonly.md)
  A Boolean value that indicates whether the request requires only detecting a human upper body to produce a result.
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
- [struct HumanObservation](humanobservation.md)
  An object that represents a person that the request detects.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ImageProcessingRequest](imageprocessingrequest.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionRequest](visionrequest.md)

## See Also

- [Analyzing a selfie and visualizing its content](analyzing-a-selfie-and-visualizing-its-content.md)
  Calculate face-capture quality and visualize facial features for a collection of images using the Vision framework.
- [struct DetectFaceRectanglesRequest](detectfacerectanglesrequest.md)
  A request that finds faces within an image.
- [struct DetectFaceLandmarksRequest](detectfacelandmarksrequest.md)
  An image-analysis request that finds facial features like eyes and mouth in an image.
- [struct DetectFaceCaptureQualityRequest](detectfacecapturequalityrequest.md)
  A request that produces a floating-point number that represents the capture quality of a face in a photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecthumanrectanglesrequest)*