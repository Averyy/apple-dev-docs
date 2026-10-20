# CoreMLModelContainer

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

A model container to use with an image-analysis request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
struct CoreMLModelContainer
```

## Topics

### Creating a model container
- [init(model: MLModel, featureProvider: (any MLFeatureProvider)?) throws](./coremlmodelcontainer/init%28model,featureprovider%29.md)
### Getting the feature name
- [var inputImageFeatureName: String](./coremlmodelcontainer/inputimagefeaturename.md)
  The name of the feature value that Vision sets from the request handler.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring a request
- [var supportedIdentifiers: [String]?](./coremlrequest/supportedidentifiers.md)
  The classification identifiers supported by the request.
- [let modelContainer: CoreMLModelContainer](./coremlrequest/modelcontainer.md)
  The model to base the image analysis request on.
- [enum ComputeStage](./computestage.md)
  Types that represent the compute stage.
- [var cropAndScaleAction: ImageCropAndScaleAction](./coremlrequest/cropandscaleaction.md)
  An optional setting that tells the Vision algorithm how to scale an input image.
- [enum ImageCropAndScaleAction](./imagecropandscaleaction.md)
  A scale to apply to an input image before performing a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/coremlmodelcontainer)*