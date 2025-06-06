# GenerateForegroundInstanceMaskRequest

**Framework**: Vision  
**Kind**: struct

A request that generates an instance mask of noticeable objects to separate from the background.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct GenerateForegroundInstanceMaskRequest
```

#### Overview

This request generates an [`InstanceMaskObservation`](instancemaskobservation.md) object with instance-mask data.

## Topics

### Creating a request
- [init(GenerateForegroundInstanceMaskRequest.Revision?)](generateforegroundinstancemaskrequest/init(_:).md)
  Creates a foreground instance-mask request.
### Getting the revision
- [let revision: GenerateForegroundInstanceMaskRequest.Revision](generateforegroundinstancemaskrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [GenerateForegroundInstanceMaskRequest.Revision]](generateforegroundinstancemaskrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [GenerateForegroundInstanceMaskRequest.Revision](generateforegroundinstancemaskrequest/revision-swift.enum.md)
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
- [struct InstanceMaskObservation](instancemaskobservation.md)
  An observation that contains an instance mask that labels instances in the mask.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ImageProcessingRequest](imageprocessingrequest.md)
- [Sendable](../Swift/Sendable.md)
- [VisionRequest](visionrequest.md)

## See Also

- [struct GenerateImageFeaturePrintRequest](generateimagefeatureprintrequest.md)
  An image-based request to generate feature prints from an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateforegroundinstancemaskrequest)*