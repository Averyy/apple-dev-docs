# CoreMLRequest

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An image-analysis request that uses a Core ML model to process images.

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
struct CoreMLRequest
```

## Overview

The results array of a [Core ML](../CoreML/CoreML.md)-based image-analysis request contain a different observation type, depending on the kind of `MLModel` object you use:

- If the model predicts a single feature and the model’s [`MLModelDescription`](../CoreML/mlmodeldescription.md) object has a non-`nil` value for [`predictedFeatureName`](../CoreML/mlmodeldescription/predictedfeaturename.md), then Vision treats the model as a classifier. The results are [`ClassificationObservation`](./classificationobservation.md) objects.
- If the model’s outputs include at least one output with a feature type of [`MLFeatureType.image`](../CoreML/mlfeaturetype/image.md), Vision treats that model as an image-to-image model. The results are [`PixelBufferObservation`](./pixelbufferobservation.md) objects.
- Otherwise, Vision treats the model as a general predictor model. The results are [`CoreMLFeatureValueObservation`](./coremlfeaturevalueobservation.md) objects.

> **Note**:  Vision forwards all confidence values from Core ML models as-is and doesn’t normalize them to [0, 1].

## Topics

### Creating a request
- [init(model: CoreMLModelContainer, CoreMLRequest.Revision?)](./coremlrequest/init%28model,_%29.md)
  Creates a Core ML request.
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
- [struct PixelBufferObservation](./pixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.
- [struct ClassificationObservation](./classificationobservation.md)
  An object that represents classification information that an image-analysis request produces.
- [struct CoreMLFeatureValueObservation](./coremlfeaturevalueobservation.md)
  An object that represents a collection of key-value information that a Core ML image-analysis request produces.
### Configuring a request
- [var supportedIdentifiers: [String]?](./coremlrequest/supportedidentifiers.md)
  The classification identifiers supported by the request.
- [let modelContainer: CoreMLModelContainer](./coremlrequest/modelcontainer.md)
  The model to base the image analysis request on.
- [struct CoreMLModelContainer](./coremlmodelcontainer.md)
  A model container to use with an image-analysis request.
- [enum ComputeStage](./computestage.md)
  Types that represent the compute stage.
- [var cropAndScaleAction: ImageCropAndScaleAction](./coremlrequest/cropandscaleaction.md)
  An optional setting that tells the Vision algorithm how to scale an input image.
- [enum ImageCropAndScaleAction](./imagecropandscaleaction.md)
  A scale to apply to an input image before performing a request.
### Getting the revision
- [let revision: CoreMLRequest.Revision](./coremlrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [CoreMLRequest.Revision]](./coremlrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [CoreMLRequest.Revision](./coremlrequest/revision-swift.enum.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/coremlrequest)*