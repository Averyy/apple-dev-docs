# CalculateImageAestheticsScoresRequest

**Framework**: Vision  
**Kind**: struct

A request that analyzes an image for aesthetically pleasing attributes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct CalculateImageAestheticsScoresRequest
```

#### Overview

The request returns the resulting aesthetics score in an instance of [`ImageAestheticsScoresObservation`](imageaestheticsscoresobservation.md).

## Topics

### Creating a request
- [init(CalculateImageAestheticsScoresRequest.Revision?)](calculateimageaestheticsscoresrequest/init(_:).md)
  Creates an image aesthetics request.
### Getting the revision
- [let revision: CalculateImageAestheticsScoresRequest.Revision](calculateimageaestheticsscoresrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [CalculateImageAestheticsScoresRequest.Revision]](calculateimageaestheticsscoresrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [CalculateImageAestheticsScoresRequest.Revision](calculateimageaestheticsscoresrequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.
### Inspecting a request
- [var cropAndScaleAction: ImageCropAndScaleAction](calculateimageaestheticsscoresrequest/cropandscaleaction.md)
  An optional setting that tells the algorithm how to scale an input image before generating the result.
- [enum ImageCropAndScaleAction](imagecropandscaleaction.md)
  A scale to apply to an input image before performing a request.
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
- [struct ImageAestheticsScoresObservation](imageaestheticsscoresobservation.md)
  An observation that provides an overall score of aesthetic attributes for an image.

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

- [Generating high-quality thumbnails from videos](generating-thumbnails-from-videos.md)
  Identify the most visually pleasing frames in a video by using the image-aesthetics scores request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/calculateimageaestheticsscoresrequest)*