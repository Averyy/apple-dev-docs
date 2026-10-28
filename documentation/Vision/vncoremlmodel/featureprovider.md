# featureProvider

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

An optional object to support inputs outside Vision.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var featureProvider: (any MLFeatureProvider)? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) id<MLFeatureProvider> featureProvider;
```

## Discussion

This optional object conforms to the [`MLFeatureProvider`](../../CoreML/mlfeatureprovider.md) protocol that the model uses to predict inputs that are not supplied by Vision. Vision provides the MLModel with the image for the [`inputImageFeatureName`](./inputimagefeaturename.md) via the `VNRequestHandler`.

A feature provider is necessary for models that have more than one required input. Models with only one image input won’t use the feature provider.

## See Also

### Providing Features
- [var inputImageFeatureName: String](./inputimagefeaturename.md)
  The name of the feature value that Vision sets from the request handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncoremlmodel/featureprovider)*