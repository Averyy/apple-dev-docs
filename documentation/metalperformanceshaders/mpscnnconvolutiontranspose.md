# MPSCNNConvolutionTranspose

**Framework**: Metal Performance Shaders  
**Kind**: cl

A transposed convolution kernel.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNConvolutionTranspose : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnconvolutiontranspose/2866995-init.md)
  Initializes a transposed convolution kernel.
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnconvolutiontranspose/2867157-init.md)
  Initializes a transposed convolution kernel.
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
### Instance Properties
- [var groups: Int](mpscnnconvolutiontranspose/2867099-groups.md)
- [var inputFeatureChannels: Int](mpscnnconvolutiontranspose/2867174-inputfeaturechannels.md)
- [var kernelOffsetX: Int](mpscnnconvolutiontranspose/2867176-kerneloffsetx.md)
- [var kernelOffsetY: Int](mpscnnconvolutiontranspose/2867086-kerneloffsety.md)
- [var outputFeatureChannels: Int](mpscnnconvolutiontranspose/2867016-outputfeaturechannels.md)
- [var accumulatorPrecisionOption: MPSNNConvolutionAccumulatorPrecisionOption](mpscnnconvolutiontranspose/2951924-accumulatorprecisionoption.md)
- [var dataSource: any MPSCNNConvolutionDataSource](mpscnnconvolutiontranspose/3131769-datasource.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, convolutionGradientState: MPSCNNConvolutionGradientState?) -> MPSImage](mpscnnconvolutiontranspose/2942409-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, convolutionGradientState: MPSCNNConvolutionGradientState?, destinationImage: MPSImage)](mpscnnconvolutiontranspose/2942429-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, convolutionGradientState: MPSCNNConvolutionGradientState?, destinationState: AutoreleasingUnsafeMutablePointer<MPSCNNConvolutionTransposeGradientState?>, destinationStateIsTemporary: Bool) -> MPSImage](mpscnnconvolutiontranspose/3131771-encode.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], convolutionGradientStates: [MPSCNNConvolutionGradientState]?) -> [MPSImage]](mpscnnconvolutiontranspose/2942406-encodebatch.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], convolutionGradientStates: [MPSCNNConvolutionGradientState]?, destinationImages: [MPSImage])](mpscnnconvolutiontranspose/2942411-encodebatch.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], convolutionGradientStates: [MPSCNNConvolutionGradientState]?, destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool) -> [MPSImage]](mpscnnconvolutiontranspose/3131770-encodebatch.md)
- [func exportWeightsAndBiases(with: any MTLCommandBuffer, resultStateCanBeTemporary: Bool) -> MPSCNNConvolutionWeightsAndBiasesState](mpscnnconvolutiontranspose/3131772-exportweightsandbiases.md)
- [func reloadWeightsAndBiases(with: any MTLCommandBuffer, state: MPSCNNConvolutionWeightsAndBiasesState)](mpscnnconvolutiontranspose/3131774-reloadweightsandbiases.md)
- [func reloadWeightsAndBiasesFromDataSource()](mpscnnconvolutiontranspose/3131773-reloadweightsandbiasesfromdataso.md)
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSCNNConvolutionGradientState]?, destinationImage: MPSImage) -> MPSCNNConvolutionTransposeGradientState?](mpscnnconvolutiontranspose/3131776-resultstate.md)
- [func resultStateBatch(sourceImage: [MPSImage], sourceStates: [[MPSCNNConvolutionGradientState]]?, destinationImage: [MPSImage]) -> [MPSCNNConvolutionTransposeGradientState]?](mpscnnconvolutiontranspose/3131775-resultstatebatch.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSCNNConvolutionGradientState]?, destinationImage: MPSImage) -> MPSCNNConvolutionTransposeGradientState?](mpscnnconvolutiontranspose/3131778-temporaryresultstate.md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, sourceImage: [MPSImage], sourceStates: [[MPSCNNConvolutionGradientState]]?, destinationImage: [MPSImage]) -> [MPSCNNConvolutionTransposeGradientState]?](mpscnnconvolutiontranspose/3131777-temporaryresultstatebatch.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)

## See Also

- [class MPSCNNBinaryConvolution](mpscnnbinaryconvolution.md)
  A convolution kernel with binary weights and an input image using binary approximations.
- [class MPSCNNConvolution](mpscnnconvolution.md)
  A convolution kernel that convolves the input image with a set of filters, with each producing one feature map in the output image.
- [class MPSCNNDepthWiseConvolutionDescriptor](mpscnndepthwiseconvolutiondescriptor.md)
  A description of a convolution object that does depthwise convolution.
- [class MPSCNNSubPixelConvolutionDescriptor](mpscnnsubpixelconvolutiondescriptor.md)
  A description of a convolution object that does subpixel upsampling and reshaping. 
- [class MPSCNNConvolutionGradient](mpscnnconvolutiongradient.md)
  A gradient convolution kernel.
- [class MPSCNNConvolutionGradientState](mpscnnconvolutiongradientstate.md)
  An object that exposes a gradient convolution kernel's gradient with respect to weights and biases.
- [protocol MPSImageSizeEncodingState](mpsimagesizeencodingstate.md)
  A protocol for objects that contain information about an image size elsewhere in the graph.
- [class MPSCNNConvolutionWeightsAndBiasesState](mpscnnconvolutionweightsandbiasesstate.md)
  A class that stores weights and biases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontranspose)*