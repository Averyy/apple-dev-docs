# VNPixelBufferObservation

**Framework**: Vision  
**Kind**: class

An object that represents an image that an image-analysis request produces.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNPixelBufferObservation
```

#### Overview

This type of observation results from performing a [`VNCoreMLRequest`](vncoremlrequest.md) image analysis with a Core ML model that has an image-to-image processing role. For example, this observation might result from a model that analyzes the style of one image and then transfers that style to a different image.

Vision infers that an [`MLModel`](https://developer.apple.com/documentation/CoreML/MLModel) object is an image-to-image model if that model includes an image. Its [`modelDescription`](https://developer.apple.com/documentation/CoreML/MLModel/modelDescription) object includes an image-typed feature description in its [`outputDescriptionsByName`](https://developer.apple.com/documentation/CoreML/MLModelDescription/outputDescriptionsByName) dictionary.

## Topics

### Parsing Observation Content
- [var pixelBuffer: CVPixelBuffer](vnpixelbufferobservation/pixelbuffer.md)
  The image that results from a request with image output.
- [var featureName: String?](vnpixelbufferobservation/featurename.md)
  A feature name that the CoreML model defines.
### Getting the supported pixel formats
- [func supportedOutputPixelFormats() throws -> [NSNumber]](vngeneratepersonsegmentationrequest/supportedoutputpixelformats.md)
  Returns a list of output pixel formats that the request supports.

## Relationships

### Inherits From
- [VNObservation](vnobservation.md)
### Inherited By
- [VNSaliencyImageObservation](vnsaliencyimageobservation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [Classifying Images with Vision and Core ML](../CoreML/classifying-images-with-vision-and-core-ml.md)
  Crop and scale photos using the Vision framework and classify them with a Core ML model.
- [Training a Create ML Model to Classify Flowers](training-a-create-ml-model-to-classify-flowers.md)
  Train a flower classifier using Create ML in Swift Playgrounds, and apply the resulting model to real-time image classification using Vision.
- [class VNCoreMLRequest](vncoremlrequest.md)
  An image-analysis request that uses a Core ML model to process images.
- [class VNClassificationObservation](vnclassificationobservation.md)
  An object that represents classification information that an image-analysis request produces.
- [class VNCoreMLFeatureValueObservation](vncoremlfeaturevalueobservation.md)
  An object that represents a collection of key-value information that a Core ML image-analysis request produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnpixelbufferobservation)*