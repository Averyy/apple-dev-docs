# init(model:completionHandler:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a model container to use with an image analysis request based on the model you provide, with an optional completion handler.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(model: VNCoreMLModel, completionHandler: VNRequestCompletionHandler? = nil)
```

```objc
- (instancetype) initWithModel:(VNCoreMLModel *) model completionHandler:(VNRequestCompletionHandler) completionHandler;
```

#### Discussion

Initialization can fail if the [Core ML](../../CoreML/CoreML.md) model you provide isn’t supported in Vision, such as if the model doesn’t accept an image as input.

## Parameters

- `model`: The [Core ML](../../CoreML/CoreML.md) model on which to base the Vision request.
- `completionHandler`: An optional block of code to execute after model initialization.

## See Also

### Initializing with a Core ML Model
- [convenience init(model: VNCoreMLModel)](./init%28model%29.md)
  Creates a model container to use with an image analysis request based on the model you provide.
- [var model: VNCoreMLModel](./model.md)
  The model to base the image analysis request on.
- [class VNCoreMLModel](../vncoremlmodel.md)
  A container for the model to use with Vision requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncoremlrequest/init(model:completionhandler:))*