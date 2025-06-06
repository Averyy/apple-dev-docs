# MPSCNNConvolutionWeightsAndBiasesState

**Framework**: Metal Performance Shaders  
**Kind**: cl

A class that stores weights and biases.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNConvolutionWeightsAndBiasesState : MPSState
```

## Topics

### Initializers
- [init(device: any MTLDevice, cnnConvolutionDescriptor: MPSCNNConvolutionDescriptor)](mpscnnconvolutionweightsandbiasesstate/2953004-init.md)
- [init(weights: any MTLBuffer, biases: (any MTLBuffer)?)](mpscnnconvolutionweightsandbiasesstate/2953008-init.md)
- [init(weights: any MTLBuffer, weightsOffset: Int, biases: (any MTLBuffer)?, biasesOffset: Int, cnnConvolutionDescriptor: MPSCNNConvolutionDescriptor)](mpscnnconvolutionweightsandbiasesstate/3325843-init.md)
### Instance Properties
- [var biases: (any MTLBuffer)?](mpscnnconvolutionweightsandbiasesstate/2953002-biases.md)
- [var biasesOffset: Int](mpscnnconvolutionweightsandbiasesstate/3325842-biasesoffset.md)
- [var weights: any MTLBuffer](mpscnnconvolutionweightsandbiasesstate/2953006-weights.md)
- [var weightsOffset: Int](mpscnnconvolutionweightsandbiasesstate/3325844-weightsoffset.md)
### Type Methods
- [class func temporaryCNNConvolutionWeightsAndBiasesState(with: any MTLCommandBuffer, cnnConvolutionDescriptor: MPSCNNConvolutionDescriptor) -> Self](mpscnnconvolutionweightsandbiasesstate/2953005-temporarycnnconvolutionweightsan.md)

## Relationships

### Inherits From
- [MPSState](mpsstate.md)

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
- [class MPSCNNConvolutionGradient](mpscnnconvolutiongradient.md)
  A gradient convolution kernel.
- [class MPSCNNConvolutionGradientState](mpscnnconvolutiongradientstate.md)
  An object that exposes a gradient convolution kernel's gradient with respect to weights and biases.
- [protocol MPSImageSizeEncodingState](mpsimagesizeencodingstate.md)
  A protocol for objects that contain information about an image size elsewhere in the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutionweightsandbiasesstate)*