# VNCoreMLRequest

**Framework**: Vision  
**Kind**: class  
**Role**: Class

An image-analysis request that uses a Core ML model to process images.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNCoreMLRequest
```

```objc
@interface VNCoreMLRequest : VNImageBasedRequest
```

## Overview

The results array of a Core ML-based image analysis request contains a different observation type, depending on the kind of [`MLModel`](../CoreML/mlmodel.md) object you use:

- If the model predicts a single feature, the model’s [`modelDescription`](../CoreML/mlmodel/modeldescription.md) object has a non-`nil` value for [`predictedFeatureName`](../CoreML/mlmodeldescription/predictedfeaturename.md) and Vision treats the model as a classifier. The results are [`VNClassificationObservation`](./vnclassificationobservation.md) objects.
- If the model’s outputs include at least one output with a feature type of [`MLFeatureType.image`](../CoreML/mlfeaturetype/image.md), Vision treats that model as an image-to-image model. The results are [`VNPixelBufferObservation`](./vnpixelbufferobservation.md) objects.
- Otherwise, Vision treats the model as a general predictor model. The results are [`VNCoreMLFeatureValueObservation`](./vncoremlfeaturevalueobservation.md) objects.

> **Note**:  Vision forwards all [`confidence`](./vnobservation/confidence.md) values from Core ML models as-is and doesn’t normalize them to `[0, 1]`.

## Topics

### Initializing with a Core ML Model
- [convenience init(model: VNCoreMLModel)](./vncoremlrequest/init%28model%29.md)
  Creates a model container to use with an image analysis request based on the model you provide.
- [init(model: VNCoreMLModel, completionHandler: VNRequestCompletionHandler?)](./vncoremlrequest/init%28model,completionhandler%29.md)
  Creates a model container to use with an image analysis request based on the model you provide, with an optional completion handler.
- [var model: VNCoreMLModel](./vncoremlrequest/model.md)
  The model to base the image analysis request on.
- [class VNCoreMLModel](./vncoremlmodel.md)
  A container for the model to use with Vision requests.
### Configuring Image Options
- [var imageCropAndScaleOption: VNImageCropAndScaleOption](./vncoremlrequest/imagecropandscaleoption.md)
  An optional setting that tells the Vision algorithm how to scale an input image.
- [enum VNImageCropAndScaleOption](./vnimagecropandscaleoption.md)
  Options that define how Vision crops and scales an input-image.
### Identifying Request Revisions
- [var VNCoreMLRequestRevision1: Int](./vncoremlrequestrevision1.md)
  A constant for specifying revision 1 of a Core ML request.

## Relationships

### Inherits From
- [VNImageBasedRequest](./vnimagebasedrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Machine learning image analysis
- [Classifying Images with Vision and Core ML](../CoreML/classifying-images-with-vision-and-core-ml.md)
  Crop and scale photos using the Vision framework and classify them with a Core ML model.
- [Training a Create ML Model to Classify Flowers](./training-a-create-ml-model-to-classify-flowers.md)
  Train a flower classifier using Create ML in Swift Playgrounds, and apply the resulting model to real-time image classification using Vision.
- [class VNClassificationObservation](./vnclassificationobservation.md)
  An object that represents classification information that an image-analysis request produces.
- [class VNPixelBufferObservation](./vnpixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.
- [class VNCoreMLFeatureValueObservation](./vncoremlfeaturevalueobservation.md)
  An object that represents a collection of key-value information that a Core ML image-analysis request produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncoremlrequest)*