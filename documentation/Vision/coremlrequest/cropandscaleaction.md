# cropAndScaleAction

**Framework**: Vision  
**Kind**: property

An optional setting that tells the Vision algorithm how to scale an input image.

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

Scaling an image ensures that the entire image fits into the algorithm’s input image dimensions, which may require a change in aspect ratio. The default value is [`ImageCropAndScaleAction.scaleToFill`](imagecropandscaleaction/scaletofill.md).

## See Also

- [var supportedIdentifiers: [String]?](coremlrequest/supportedidentifiers.md)
  The classification identifiers supported by the request.
- [let modelContainer: CoreMLModelContainer](coremlrequest/modelcontainer.md)
  The model to base the image analysis request on.
- [struct CoreMLModelContainer](coremlmodelcontainer.md)
  A model container to use with an image-analysis request.
- [enum ComputeStage](computestage.md)
  Types that represent the compute stage.
- [enum ImageCropAndScaleAction](imagecropandscaleaction.md)
  A scale to apply to an input image before performing a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/coremlrequest/cropandscaleaction)*