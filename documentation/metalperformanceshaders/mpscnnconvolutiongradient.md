# MPSCNNConvolutionGradient

**Framework**: Metal Performance Shaders  
**Kind**: cl

A gradient convolution kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNConvolutionGradient : MPSCNNGradientKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnconvolutiongradient/2942425-init.md)
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnconvolutiongradient/2942414-init.md)
### Instance Properties
- [var channelMultiplier: Int](mpscnnconvolutiongradient/2966658-channelmultiplier.md)
- [var dataSource: any MPSCNNConvolutionDataSource](mpscnnconvolutiongradient/2953959-datasource.md)
- [var gradientOption: MPSCNNConvolutionGradientOption](mpscnnconvolutiongradient/2942432-gradientoption.md)
- [var groups: Int](mpscnnconvolutiongradient/2942430-groups.md)
- [var serializeWeightsAndBiases: Bool](mpscnnconvolutiongradient/2951926-serializeweightsandbiases.md)
- [var sourceGradientFeatureChannels: Int](mpscnnconvolutiongradient/2947880-sourcegradientfeaturechannels.md)
- [var sourceImageFeatureChannels: Int](mpscnnconvolutiongradient/2947882-sourceimagefeaturechannels.md)
### Instance Methods
- [func reloadWeightsAndBiases(with: any MTLCommandBuffer, state: MPSCNNConvolutionWeightsAndBiasesState)](mpscnnconvolutiongradient/2953960-reloadweightsandbiases.md)
- [func reloadWeightsAndBiasesFromDataSource()](mpscnnconvolutiongradient/2966659-reloadweightsandbiasesfromdataso.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](mpscnngradientkernel.md)

## See Also

- [class MPSCNNBinaryConvolution](mpscnnbinaryconvolution.md)
  A convolution kernel with binary weights and an input image using binary approximations.
- [class MPSCNNConvolution](mpscnnconvolution.md)
  A convolution kernel that convolves the input image with a set of filters, with each producing one feature map in the output image.
- [class MPSCNNDepthWiseConvolutionDescriptor](mpscnndepthwiseconvolutiondescriptor.md)
  A description of a convolution object that does depthwise convolution.
- [class MPSCNNSubPixelConvolutionDescriptor](mpscnnsubpixelconvolutiondescriptor.md)
  A description of a convolution object that does subpixel upsampling and reshaping. 
- [class MPSCNNConvolutionTranspose](mpscnnconvolutiontranspose.md)
  A transposed convolution kernel.
- [class MPSCNNConvolutionGradientState](mpscnnconvolutiongradientstate.md)
  An object that exposes a gradient convolution kernel's gradient with respect to weights and biases.
- [protocol MPSImageSizeEncodingState](mpsimagesizeencodingstate.md)
  A protocol for objects that contain information about an image size elsewhere in the graph.
- [class MPSCNNConvolutionWeightsAndBiasesState](mpscnnconvolutionweightsandbiasesstate.md)
  A class that stores weights and biases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiongradient)*