# ComputeStage

**Framework**: Vision  
**Kind**: enum

Types that represent the compute stage.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum ComputeStage
```

#### Overview

The main compute stage represents the essential functionality of a request. Requests that provide additional analysis — or conversion of the data by the main stage — can also report a post-processing stage.

## Topics

### Getting the compute stages
- [ComputeStage.main](computestage/main.md)
  A stage that represents where the system performs the main functionality.
- [ComputeStage.postProcessing](computestage/postprocessing.md)
  A stage that represents where the system performs additional analysis after the main compute stage.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var supportedIdentifiers: [String]?](coremlrequest/supportedidentifiers.md)
  The classification identifiers supported by the request.
- [let modelContainer: CoreMLModelContainer](coremlrequest/modelcontainer.md)
  The model to base the image analysis request on.
- [struct CoreMLModelContainer](coremlmodelcontainer.md)
  A model container to use with an image-analysis request.
- [var cropAndScaleAction: ImageCropAndScaleAction](coremlrequest/cropandscaleaction.md)
  An optional setting that tells the Vision algorithm how to scale an input image.
- [enum ImageCropAndScaleAction](imagecropandscaleaction.md)
  A scale to apply to an input image before performing a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/computestage)*