# DetectRectanglesRequest

**Framework**: Vision  
**Kind**: struct

An image-analysis request that finds projected rectangular regions in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct DetectRectanglesRequest
```

#### Overview

A rectangle-detection request locates regions of an image with rectangular shape, like credit cards, business cards, documents, and signs. The request returns its observations in the form of [`RectangleObservation`](rectangleobservation.md) objects, and contains normalized coordinates of bounding boxes containing a rectangle.

Use this type of request to find the bounding boxes of rectangles in an image. Vision returns observations for rectangles found in all orientations and sizes, along with a confidence level to indicate how likely it is that the observation contains an actual rectangle.

To further configure or restrict the types of rectangles found, set properties on the request specifying a range of aspect ratios, sizes, and quadrature tolerance.

## Topics

### Creating a request
- [init(DetectRectanglesRequest.Revision?)](detectrectanglesrequest/init(_:).md)
  Creates a rectangle-detection request.
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
- [var maximumAspectRatio: Float](detectrectanglesrequest/maximumaspectratio.md)
  The largest aspect ratio the rectangle request detects.
- [var maximumObservations: Int](detectrectanglesrequest/maximumobservations.md)
  The maximum number of rectangles Vision returns.
- [var minimumAspectRatio: Float](detectrectanglesrequest/minimumaspectratio.md)
  The smallest aspect ratio the rectangle request detects.
- [var minimumConfidence: Float](detectrectanglesrequest/minimumconfidence.md)
  The minimum acceptable confidence level for detected rectangles.
- [var minimumSize: Float](detectrectanglesrequest/minimumsize.md)
  The minimum size of the rectangle to be detected, as a proportion of the smallest dimension.
- [var quadratureToleranceDegrees: Float](detectrectanglesrequest/quadraturetolerancedegrees.md)
  The maximum number of degrees a rectangle corner angle can deviate from 90°.
### Getting the revision
- [let revision: DetectRectanglesRequest.Revision](detectrectanglesrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectRectanglesRequest.Revision]](detectrectanglesrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [DetectRectanglesRequest.Revision](detectrectanglesrequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.

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

- [struct DetectContoursRequest](detectcontoursrequest.md)
  A request that detects the contours of the edges of an image.
- [struct DetectHorizonRequest](detecthorizonrequest.md)
  An image-analysis request that determines the horizon angle in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectrectanglesrequest)*