# VNCoreMLFeatureValueObservation

**Framework**: Vision  
**Kind**: class

An object that represents a collection of key-value information that a Core ML image-analysis request produces.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNCoreMLFeatureValueObservation
```

#### Overview

This type of observation results from performing a [`VNCoreMLRequest`](vncoremlrequest.md) image analysis with a Core ML model whose role is prediction rather than classification or image-to-image processing.

Vision infers that an [`MLModel`](https://developer.apple.com/documentation/coreml/mlmodel) object is a predictor model if that model predicts multiple features. You can tell that a model predicts multiple features when its [`modelDescription`](https://developer.apple.com/documentation/coreml/mlmodel/modeldescription) object has a `nil` value for its [`predictedFeatureName`](https://developer.apple.com/documentation/coreml/mlmodeldescription/predictedfeaturename) property, or when it inserts its output in an [`outputDescriptionsByName`](https://developer.apple.com/documentation/coreml/mlmodeldescription/outputdescriptionsbyname) dictionary.

## Topics

### Obtaining Feature Values
- [var featureValue: MLFeatureValue](vncoremlfeaturevalueobservation/featurevalue.md)
  The feature result of a [`VNCoreMLRequest`](vncoremlrequest.md) that outputs neither a classification nor an image.
- [var featureName: String](vncoremlfeaturevalueobservation/featurename.md)
  The name used in the model description of the CoreML model that produced this observation.

## Relationships

### Inherits From
- [VNObservation](vnobservation.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [Classifying Images with Vision and Core ML](../coreml/classifying-images-with-vision-and-core-ml.md)
  Crop and scale photos using the Vision framework and classify them with a Core ML model.
- [Training a Create ML Model to Classify Flowers](training-a-create-ml-model-to-classify-flowers.md)
  Train a flower classifier using Create ML in Swift Playgrounds, and apply the resulting model to real-time image classification using Vision.
- [class VNCoreMLRequest](vncoremlrequest.md)
  An image-analysis request that uses a Core ML model to process images.
- [class VNClassificationObservation](vnclassificationobservation.md)
  An object that represents classification information that an image-analysis request produces.
- [class VNPixelBufferObservation](vnpixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncoremlfeaturevalueobservation)*