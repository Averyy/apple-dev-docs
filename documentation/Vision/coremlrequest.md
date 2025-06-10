# CoreMLRequest

**Framework**: Vision  
**Kind**: struct

An image-analysis request that uses a Core ML model to process images.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct CoreMLRequest
```

#### Overview

The results array of a [`Core ML`](https://developer.apple.com/documentation/CoreML)-based image-analysis request contain a different observation type, depending on the kind of `MLModel` object you use:

- If the model predicts a single feature and the model’s [`MLModelDescription`](https://developer.apple.com/documentation/CoreML/MLModelDescription) object has a non-`nil` value for [`predictedFeatureName`](https://developer.apple.com/documentation/CoreML/MLModelDescription/predictedFeatureName), then Vision treats the model as a classifier. The results are [`ClassificationObservation`](classificationobservation.md) objects.
- If the model’s outputs include at least one output with a feature type of [`MLFeatureType.image`](https://developer.apple.com/documentation/CoreML/MLFeatureType/image), Vision treats that model as an image-to-image model. The results are [`PixelBufferObservation`](pixelbufferobservation.md) objects.
- Otherwise, Vision treats the model as a general predictor model. The results are [`CoreMLFeatureValueObservation`](coremlfeaturevalueobservation.md) objects.

> **Note**:  Vision forwards all confidence values from Core ML models as-is and doesn’t normalize them to [0, 1].

## Topics

### Creating a request
- [init(model: CoreMLModelContainer, CoreMLRequest.Revision?)](coremlrequest/init(model:_:).md)
  Creates a Core ML request.
### Getting the revision
- [let revision: CoreMLRequest.Revision](coremlrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [CoreMLRequest.Revision]](coremlrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [CoreMLRequest.Revision](coremlrequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.
### Inspecting a request
- [var supportedIdentifiers: [String]?](coremlrequest/supportedidentifiers.md)
  The classification identifiers supported by the request.
- [let modelContainer: CoreMLModelContainer](coremlrequest/modelcontainer.md)
  The model to base the image analysis request on.
- [struct CoreMLModelContainer](coremlmodelcontainer.md)
  A model container to use with an image-analysis request.
- [enum ComputeStage](computestage.md)
  Types that represent the compute stage.
- [var cropAndScaleAction: ImageCropAndScaleAction](coremlrequest/cropandscaleaction.md)
  An optional setting that tells the Vision algorithm how to scale an input image.
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

- [struct CoreMLFeatureValueObservation](coremlfeaturevalueobservation.md)
  An object that represents a collection of key-value information that a Core ML image-analysis request produces.
- [struct ClassificationObservation](classificationobservation.md)
  An object that represents classification information that an image-analysis request produces.
- [struct PixelBufferObservation](pixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/coremlrequest)*