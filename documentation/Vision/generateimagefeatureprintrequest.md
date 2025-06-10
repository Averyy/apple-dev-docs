# GenerateImageFeaturePrintRequest

**Framework**: Vision  
**Kind**: struct

An image-based request to generate feature prints from an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct GenerateImageFeaturePrintRequest
```

#### Overview

This request generates an [`FeaturePrintObservation`](featureprintobservation.md) object with the features in an image.

## Topics

### Creating a request
- [init(GenerateImageFeaturePrintRequest.Revision?)](generateimagefeatureprintrequest/init(_:).md)
  Creates an image-feature print request.
### Getting the revision
- [let revision: GenerateImageFeaturePrintRequest.Revision](generateimagefeatureprintrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [GenerateImageFeaturePrintRequest.Revision]](generateimagefeatureprintrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [GenerateImageFeaturePrintRequest.Revision](generateimagefeatureprintrequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.
### Inspecting a request
- [var cropAndScaleAction: ImageCropAndScaleAction](generateimagefeatureprintrequest/cropandscaleaction.md)
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
- [struct FeaturePrintObservation](featureprintobservation.md)
  An observation that provides the recognized feature print.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateimagefeatureprintrequest)*