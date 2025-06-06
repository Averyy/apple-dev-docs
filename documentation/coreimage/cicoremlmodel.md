# CICoreMLModel

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a Core ML model filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CICoreMLModel
```

## Topics

### Instance Properties
- [var headIndex: Float](cicoremlmodel/3228195-headindex.md)
  A number that specifies which output of a multihead Core ML model applies the effect on the image.
- [var inputImage: CIImage?](cicoremlmodel/3228196-inputimage.md)
  The image to use as an input image.
- [var model: MLModel](cicoremlmodel/3228197-model.md)
  The Core ML model used to apply the effect on the image.
- [var softmaxNormalization: Bool](cicoremlmodel/3228198-softmaxnormalization.md)
  A Boolean value that specifies whether to apply Softmax normalization to the output of the model.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func coreMLModel() -> any CIFilter & CICoreMLModel](cifilter/3228305-coremlmodel.md)
  Filters an image with a Core ML model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicoremlmodel)*