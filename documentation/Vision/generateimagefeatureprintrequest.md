# GenerateImageFeaturePrintRequest

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An image-based request to generate feature prints from an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
struct GenerateImageFeaturePrintRequest
```

#### Overview

This request generates an [`FeaturePrintObservation`](./featureprintobservation.md) object with the features in an image.

## Topics

### Creating a request
- [init(GenerateImageFeaturePrintRequest.Revision?)](./generateimagefeatureprintrequest/init%28_%29.md)
  Creates an image-feature print request.
### Performing a request
- [func perform(on: URL, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./imageprocessingrequest/perform%28on,orientation%29-80bya.md)
  Performs the request on an image URL and produces observations.
- [func perform(on: Data, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./imageprocessingrequest/perform%28on,orientation%29-3f3f1.md)
  Performs the request on image data and produces observations.
- [func perform(on: CGImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./imageprocessingrequest/perform%28on,orientation%29-qxxx.md)
  Performs the request on a Core Graphics image and produces observations.
- [func perform(on: CVPixelBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./imageprocessingrequest/perform%28on,orientation%29-xspx.md)
  Performs the request on a pixel buffer and produces observations.
- [func perform(on: CMSampleBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./imageprocessingrequest/perform%28on,orientation%29-3hddl.md)
  Performs the request on a Core Media buffer and produces observations.
- [func perform(on: CIImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](./imageprocessingrequest/perform%28on,orientation%29-85ex1.md)
  Performs the request on a Core Image image and produces observations.
### Understanding the result
- [struct FeaturePrintObservation](./featureprintobservation.md)
  An observation that provides the recognized feature print.
### Configuring a request
- [var cropAndScaleAction: ImageCropAndScaleAction](./generateimagefeatureprintrequest/cropandscaleaction.md)
  An optional setting that tells the algorithm how to scale an input image before generating the result.
- [enum ImageCropAndScaleAction](./imagecropandscaleaction.md)
  A scale to apply to an input image before performing a request.
### Getting the revision
- [let revision: GenerateImageFeaturePrintRequest.Revision](./generateimagefeatureprintrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [GenerateImageFeaturePrintRequest.Revision]](./generateimagefeatureprintrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [GenerateImageFeaturePrintRequest.Revision](./generateimagefeatureprintrequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [ImageProcessingRequest](./imageprocessingrequest.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [VisionRequest](./visionrequest.md)

## See Also

### Image registration and comparison
- [class TrackHomographicImageRegistrationRequest](./trackhomographicimageregistrationrequest.md)
  An image-analysis request that you track over time to determine the perspective warp matrix necessary to align the content of two images.
- [class TrackTranslationalImageRegistrationRequest](./tracktranslationalimageregistrationrequest.md)
  An image-analysis request that you track over time to determine the affine transform necessary to align the content of two images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateimagefeatureprintrequest)*