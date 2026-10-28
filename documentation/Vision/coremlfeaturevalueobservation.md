# CoreMLFeatureValueObservation

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An object that represents a collection of key-value information that a Core ML image-analysis request produces.

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
struct CoreMLFeatureValueObservation
```

## Overview

This type of observation results from performing a [`CoreMLRequest`](./coremlrequest.md) image analysis with a [Core ML](../CoreML/CoreML.md) model whose role is prediction rather than classification or image-to-image processing.

The framework infers that an [`MLModel`](../CoreML/mlmodel.md) object is a predictor model if that model predicts multiple features. You can tell that a model predicts multiple features when its [`modelDescription`](../CoreML/mlmodel/modeldescription.md) object has a `nil` value for its [`predictedFeatureName`](../CoreML/mlmodeldescription/predictedfeaturename.md) property, or when it inserts its output in an [`outputDescriptionsByName`](../CoreML/mlmodeldescription/outputdescriptionsbyname.md) dictionary.

The confidence for these observations is always `1.0`.

## Topics

### Creating an observation
- [init?(VNCoreMLFeatureValueObservation)](./coremlfeaturevalueobservation/init%28_%29.md)
  Creates a feature value observation.
### Inspecting an observation
- [enum RequestDescriptor](./requestdescriptor.md)
  A type that describes the request and revision combination.
### Getting the feature name and value
- [let featureName: String](./coremlfeaturevalueobservation/featurename.md)
  The name in the model description of the model that produces this observation.
- [let featureValue: MLSendableFeatureValue](./coremlfeaturevalueobservation/featurevalue.md)
  The feature result of a request that outputs neither a classification nor an image.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [VisionObservation](./visionobservation.md)

## See Also

### Understanding the result
- [struct PixelBufferObservation](./pixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.
- [struct ClassificationObservation](./classificationobservation.md)
  An object that represents classification information that an image-analysis request produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/coremlfeaturevalueobservation)*