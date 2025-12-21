# GeneratePersonInstanceMaskRequest

**Framework**: Vision  
**Kind**: struct

A request that produces a mask of individual people it finds in the input image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct GeneratePersonInstanceMaskRequest
```

#### Overview

The request returns the resulting image mask in an instance of [`InstanceMaskObservation`](instancemaskobservation.md).

## Topics

### Creating a request
- [init(GeneratePersonInstanceMaskRequest.Revision?)](generatepersoninstancemaskrequest/init(_:).md)
  Creates a person instance mask request.
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
- [struct InstanceMaskObservation](instancemaskobservation.md)
  An observation that contains an instance mask that labels instances in the mask.
### Getting the revision
- [let revision: GeneratePersonInstanceMaskRequest.Revision](generatepersoninstancemaskrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [GeneratePersonInstanceMaskRequest.Revision]](generatepersoninstancemaskrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [GeneratePersonInstanceMaskRequest.Revision](generatepersoninstancemaskrequest/revision-swift.enum.md)
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

- [struct GenerateForegroundInstanceMaskRequest](generateforegroundinstancemaskrequest.md)
  A request that generates an instance mask of noticeable objects to separate from the background.
- [class GeneratePersonSegmentationRequest](generatepersonsegmentationrequest.md)
  A request that produces a matte image for a person it finds in the input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generatepersoninstancemaskrequest)*