# VNCoreMLModel

**Framework**: Vision  
**Kind**: class

A container for the model to use with Vision requests.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNCoreMLModel
```

#### Overview

A [`Core ML`](https://developer.apple.com/documentation/CoreML) model encapsulates the information trained from a data set used to drive Vision recognition requests. See [`Getting a Core ML Model`](https://developer.apple.com/documentation/CoreML/getting-a-core-ml-model) for instructions on training your own model. Once you train the model, use this class to initialize a [`VNCoreMLRequest`](vncoremlrequest.md) for identification.

## Topics

### Initializing a Model
- [convenience init(for: MLModel) throws](vncoremlmodel/init(for:).md)
  Creates a model container to use with a Core ML request.
### Providing Features
- [var featureProvider: (any MLFeatureProvider)?](vncoremlmodel/featureprovider.md)
  An optional object to support inputs outside Vision.
- [var inputImageFeatureName: String](vncoremlmodel/inputimagefeaturename.md)
  The name of the feature value that Vision sets from the request handler.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init(model: VNCoreMLModel)](vncoremlrequest/init(model:).md)
  Creates a model container to use with an image analysis request based on the model you provide.
- [init(model: VNCoreMLModel, completionHandler: VNRequestCompletionHandler?)](vncoremlrequest/init(model:completionhandler:).md)
  Creates a model container to use with an image analysis request based on the model you provide, with an optional completion handler.
- [var model: VNCoreMLModel](vncoremlrequest/model.md)
  The model to base the image analysis request on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncoremlmodel)*