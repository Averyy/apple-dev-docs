# model

**Framework**: Vision  
**Kind**: property

The model to base the image analysis request on.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var model: VNCoreMLModel { get }
```

#### Discussion

This object wraps a [`Core ML`](https://developer.apple.com/documentation/CoreML) model.

## See Also

- [convenience init(model: VNCoreMLModel)](vncoremlrequest/init(model:).md)
  Creates a model container to use with an image analysis request based on the model you provide.
- [init(model: VNCoreMLModel, completionHandler: VNRequestCompletionHandler?)](vncoremlrequest/init(model:completionhandler:).md)
  Creates a model container to use with an image analysis request based on the model you provide, with an optional completion handler.
- [class VNCoreMLModel](vncoremlmodel.md)
  A container for the model to use with Vision requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncoremlrequest/model)*