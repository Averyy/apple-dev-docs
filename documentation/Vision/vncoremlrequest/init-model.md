# init(model:)

**Framework**: Vision  
**Kind**: init

Creates a model container to use with an image analysis request based on the model you provide.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(model: VNCoreMLModel)
```

#### Discussion

Initialization can fail if the [`Core ML`](https://developer.apple.com/documentation/CoreML) model you provide isn’t supported in Vision, such as if the model doesn’t accept an image as input.

## Parameters

- `model`: The   model on which to base the Vision request.

## See Also

- [init(model: VNCoreMLModel, completionHandler: VNRequestCompletionHandler?)](vncoremlrequest/init(model:completionhandler:).md)
  Creates a model container to use with an image analysis request based on the model you provide, with an optional completion handler.
- [var model: VNCoreMLModel](vncoremlrequest/model.md)
  The model to base the image analysis request on.
- [class VNCoreMLModel](vncoremlmodel.md)
  A container for the model to use with Vision requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncoremlrequest/init(model:))*