# GenerateObjectnessBasedSaliencyImageRequest

**Framework**: Vision  
**Kind**: struct

A request that generates a heat map that identifies the parts of an image most likely to represent objects.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct GenerateObjectnessBasedSaliencyImageRequest
```

#### Overview

The request returns the resulting heat map and object data in an instance of [`SaliencyImageObservation`](saliencyimageobservation.md).

## Topics

### Creating a request
- [init(GenerateObjectnessBasedSaliencyImageRequest.Revision?)](generateobjectnessbasedsaliencyimagerequest/init(_:).md)
  Creates an objectness saliency image request.
### Getting the revision
- [let revision: GenerateObjectnessBasedSaliencyImageRequest.Revision](generateobjectnessbasedsaliencyimagerequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [GenerateObjectnessBasedSaliencyImageRequest.Revision]](generateobjectnessbasedsaliencyimagerequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [GenerateObjectnessBasedSaliencyImageRequest.Revision](generateobjectnessbasedsaliencyimagerequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.
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
- [struct SaliencyImageObservation](saliencyimageobservation.md)
  An observation that contains a grayscale heat map of important areas across an image.

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

- [struct GenerateAttentionBasedSaliencyImageRequest](generateattentionbasedsaliencyimagerequest.md)
  An object that produces a heat map that identifies the parts of an image most likely to draw attention.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateobjectnessbasedsaliencyimagerequest)*