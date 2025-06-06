# supportedIdentifiers

**Framework**: Vision  
**Kind**: property

The classification identifiers supported by the request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var supportedIdentifiers: [String]? { get }
```

#### Discussion

This returns `nil` if the configuration isn’t supported.

## See Also

- [let modelContainer: CoreMLModelContainer](coremlrequest/modelcontainer.md)
  The model to base the image analysis request on.
- [struct CoreMLModelContainer](coremlmodelcontainer.md)
  A model container to use with an image-analysis request.
- [enum ComputeStage](computestage.md)
  Types that represent the compute stage.
- [var cropAndScaleAction: ImageCropAndScaleAction](coremlrequest/cropandscaleaction.md)
  An optional setting that tells the Vision algorithm how to scale an input image.
- [enum ImageCropAndScaleAction](imagecropandscaleaction.md)
  A scale to apply to an input image before performing a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/coremlrequest/supportedidentifiers)*