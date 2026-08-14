# VNClassificationObservation

**Framework**: Vision  
**Kind**: class

An object that represents classification information that an image-analysis request produces.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNClassificationObservation
```

#### Overview

This type of observation results from performing a [`VNCoreMLRequest`](vncoremlrequest.md) image analysis with a Core ML model whose role is classification (rather than prediction or image-to-image processing). Vision infers that an [`MLModel`](https://developer.apple.com/documentation/coreml/mlmodel) object is a classifier model if that model predicts a single feature. That is, the model’s [`modelDescription`](https://developer.apple.com/documentation/coreml/mlmodel/modeldescription) object has a non-`nil` value for its [`predictedFeatureName`](https://developer.apple.com/documentation/coreml/mlmodeldescription/predictedfeaturename) property.

## Topics

### Determining Classification
- [var identifier: String](vnclassificationobservation/identifier.md)
  Classification label identifying the type of observation.
### Measuring Confidence and Precision
- [var hasPrecisionRecallCurve: Bool](vnclassificationobservation/hasprecisionrecallcurve.md)
  A Boolean variable indicating whether the observation contains precision and recall curves.
- [func hasMinimumPrecision(Float, forRecall: Float) -> Bool](vnclassificationobservation/hasminimumprecision(_:forrecall:).md)
  Determines whether the observation for a specific recall has a minimum precision value.
- [func hasMinimumRecall(Float, forPrecision: Float) -> Bool](vnclassificationobservation/hasminimumrecall(_:forprecision:).md)
  Determines whether the observation for a specific precision has a minimum recall value.

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
- [class VNPixelBufferObservation](vnpixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.
- [class VNCoreMLFeatureValueObservation](vncoremlfeaturevalueobservation.md)
  An object that represents a collection of key-value information that a Core ML image-analysis request produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnclassificationobservation)*