# MPSCNNCrossChannelNormalizationGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

A representation of a gradient normalization kernel applied across feature channels.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNCrossChannelNormalizationGradientNode : MPSNNGradientFilterNode
```

## Topics

### Initializers
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, gradientState: MPSNNGradientStateNode, kernelSize: Int)](mpscnncrosschannelnormalizationgradientnode/2948043-init.md)
### Instance Properties
- [var kernelSize: Int](mpscnncrosschannelnormalizationgradientnode/2948049-kernelsize.md)

## Relationships

### Inherits From
- [MPSNNGradientFilterNode](mpsnngradientfilternode.md)

## See Also

- [class MPSCNNBinaryConvolutionNode](mpscnnbinaryconvolutionnode.md)
  A representation of a convolution kernel with binary weights and an input image using binary approximations.
- [class MPSCNNConvolutionNode](mpscnnconvolutionnode.md)
  A representation of a convolution kernel.
- [class MPSCNNConvolutionTransposeNode](mpscnnconvolutiontransposenode.md)
  A representation of a transposed convolution.
- [class MPSCNNConvolutionGradientNode](mpscnnconvolutiongradientnode.md)
  A representation of a gradient convolution kernel.
- [class MPSCNNConvolutionGradientStateNode](mpscnnconvolutiongradientstatenode.md)
  A representation of a gradient convolution state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnncrosschannelnormalizationgradientnode)*