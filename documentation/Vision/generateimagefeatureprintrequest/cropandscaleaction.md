# cropAndScaleAction

**Framework**: Vision  
**Kind**: property

An optional setting that tells the algorithm how to scale an input image before generating the result.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var cropAndScaleAction: ImageCropAndScaleAction
```

#### Discussion

The system applies scaling before generating the feature print. The default value is [`ImageCropAndScaleAction.scaleToFill`](imagecropandscaleaction/scaletofill.md).

## See Also

- [enum ImageCropAndScaleAction](imagecropandscaleaction.md)
  A scale to apply to an input image before performing a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateimagefeatureprintrequest/cropandscaleaction)*