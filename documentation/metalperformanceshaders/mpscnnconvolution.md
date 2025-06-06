# MPSCNNConvolution

**Framework**: Metal Performance Shaders  
**Kind**: cl

A convolution kernel that convolves the input image with a set of filters, with each producing one feature map in the output image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNConvolution : MPSCNNKernel
```

#### Overview

The attributes of a convolution operation are described by an [`MPSCNNConvolutionDescriptor`](mpscnnconvolutiondescriptor.md) object. 

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnconvolution/2867142-init.md)
- [init(device: any MTLDevice, convolutionDescriptor: MPSCNNConvolutionDescriptor, kernelWeights: UnsafePointer<Float>, biasTerms: UnsafePointer<Float>?, flags: MPSCNNConvolutionFlags)](mpscnnconvolution/1648861-init.md)
  Initializes a convolution kernel.
- [class MPSCNNConvolutionDescriptor](mpscnnconvolutiondescriptor.md)
  A description of the attributes of a convolution kernel.
- [enum MPSCNNConvolutionFlags](mpscnnconvolutionflags.md)
  Options used to control how kernel weights are stored and used in the CNN kernels
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnconvolution/2867092-init.md)
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
### Instance Properties
- [var inputFeatureChannels: Int](mpscnnconvolution/1845268-inputfeaturechannels.md)
  The number of feature channels per pixel in the input image.
- [var outputFeatureChannels: Int](mpscnnconvolution/1845271-outputfeaturechannels.md)
  The number of feature channels per pixel in the output image.
- [var groups: Int](mpscnnconvolution/1845269-groups.md)
  The number of groups that the input and output channels are divided into.
- [var subPixelScaleFactor: Int](mpscnnconvolution/2873341-subpixelscalefactor.md)
- [var neuron: MPSCNNNeuron?](mpscnnconvolution/1845274-neuron.md)
  The neuron filter to be applied as part of the convolution operation.
- [class MPSCNNNeuron](mpscnnneuron.md)
  A filter that applies a neuron activation function.
- [var neuronType: MPSCNNNeuronType](mpscnnconvolution/2875190-neurontype.md)
- [enum MPSCNNNeuronType](mpscnnneurontype.md)
  The types of neuron filter to append to a convolution.
- [var neuronParameterA: Float](mpscnnconvolution/2875214-neuronparametera.md)
- [var neuronParameterB: Float](mpscnnconvolution/2875218-neuronparameterb.md)
- [var accumulatorPrecisionOption: MPSNNConvolutionAccumulatorPrecisionOption](mpscnnconvolution/2942410-accumulatorprecisionoption.md)
- [var channelMultiplier: Int](mpscnnconvolution/2919729-channelmultiplier.md)
- [var dataSource: any MPSCNNConvolutionDataSource](mpscnnconvolution/2953961-datasource.md)
- [var fusedNeuronDescriptor: MPSNNNeuronDescriptor?](mpscnnconvolution/3013776-fusedneurondescriptor.md)
- [var neuronParameterC: Float](mpscnnconvolution/2935626-neuronparameterc.md)
### Instance Methods
- [func exportWeightsAndBiases(with: any MTLCommandBuffer, resultStateCanBeTemporary: Bool) -> MPSCNNConvolutionWeightsAndBiasesState](mpscnnconvolution/2953001-exportweightsandbiases.md)
- [func reloadWeightsAndBiases(with: any MPSCNNConvolutionDataSource)](mpscnnconvolution/2942428-reloadweightsandbiases.md)
- [func reloadWeightsAndBiases(with: any MTLCommandBuffer, state: MPSCNNConvolutionWeightsAndBiasesState)](mpscnnconvolution/2953962-reloadweightsandbiases.md)
- [func reloadWeightsAndBiasesFromDataSource()](mpscnnconvolution/2966657-reloadweightsandbiasesfromdataso.md)
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNConvolutionGradientState?](mpscnnconvolution/2947883-resultstate.md)
- [func resultStateBatch(sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSCNNConvolutionGradientState]?](mpscnnconvolution/2947881-resultstatebatch.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNConvolutionGradientState?](mpscnnconvolution/2947885-temporaryresultstate.md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSCNNConvolutionGradientState]?](mpscnnconvolution/2947886-temporaryresultstatebatch.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)

## See Also

- [class MPSCNNBinaryConvolution](mpscnnbinaryconvolution.md)
  A convolution kernel with binary weights and an input image using binary approximations.
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
- [class MPSCNNConvolutionWeightsAndBiasesState](mpscnnconvolutionweightsandbiasesstate.md)
  A class that stores weights and biases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolution)*