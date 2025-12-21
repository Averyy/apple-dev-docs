# DetectHorizonRequest

**Framework**: Vision  
**Kind**: struct

An image-analysis request that determines the horizon angle in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct DetectHorizonRequest
```

#### Overview

This request generates a [`HorizonObservation`](horizonobservation.md) object that describes the horizon the request detects.

## Topics

### Creating a request
- [init(DetectHorizonRequest.Revision?)](detecthorizonrequest/init(_:).md)
  Creates a horizon-detection request.
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
- [struct HorizonObservation](horizonobservation.md)
  The horizon angle information that an image-analysis request detects.
### Getting the revision
- [let revision: DetectHorizonRequest.Revision](detecthorizonrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectHorizonRequest.Revision]](detecthorizonrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [DetectHorizonRequest.Revision](detecthorizonrequest/revision-swift.enum.md)
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
- [struct DetectRectanglesRequest](detectrectanglesrequest.md)
  An image-analysis request that finds projected rectangular regions in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecthorizonrequest)*