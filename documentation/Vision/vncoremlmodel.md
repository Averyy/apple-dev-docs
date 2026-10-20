# VNCoreMLModel

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNCoreMLModel : NSObject
```

#### Overview

A [Core ML](../CoreML/CoreML.md) model encapsulates the information trained from a data set used to drive Vision recognition requests. See [Getting a Core ML Model](../CoreML/getting-a-core-ml-model.md) for instructions on training your own model. Once you train the model, use this class to initialize a [`VNCoreMLRequest`](./vncoremlrequest.md) for identification.

## Topics

### Initializing a Model
- [convenience init(for: MLModel) throws](./vncoremlmodel/init%28for%29.md)
  Creates a model container to use with a Core ML request.
- [convenience init(forMLModel: MLModel) throws](./vncoremlmodel/init%28formlmodel%29.md)
### Providing Features
- [var featureProvider: (any MLFeatureProvider)?](./vncoremlmodel/featureprovider.md)
  An optional object to support inputs outside Vision.
- [var inputImageFeatureName: String](./vncoremlmodel/inputimagefeaturename.md)
  The name of the feature value that Vision sets from the request handler.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Initializing with a Core ML Model
- [convenience init(model: VNCoreMLModel)](./vncoremlrequest/init%28model%29.md)
  Creates a model container to use with an image analysis request based on the model you provide.
- [init(model: VNCoreMLModel, completionHandler: VNRequestCompletionHandler?)](./vncoremlrequest/init%28model,completionhandler%29.md)
  Creates a model container to use with an image analysis request based on the model you provide, with an optional completion handler.
- [var model: VNCoreMLModel](./vncoremlrequest/model.md)
  The model to base the image analysis request on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncoremlmodel)*