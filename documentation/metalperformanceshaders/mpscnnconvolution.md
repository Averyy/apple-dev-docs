# MPSCNNConvolution

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSCNNConvolution
```

#### Overview

The attributes of a convolution operation are described by an [`MPSCNNConvolutionDescriptor`](mpscnnconvolutiondescriptor.md) object.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnconvolution/init(coder:device:).md)
- [init(device: any MTLDevice, convolutionDescriptor: MPSCNNConvolutionDescriptor, kernelWeights: UnsafePointer<Float>, biasTerms: UnsafePointer<Float>?, flags: MPSCNNConvolutionFlags)](mpscnnconvolution/init(device:convolutiondescriptor:kernelweights:biasterms:flags:).md)
  Initializes a convolution kernel.
- [class MPSCNNConvolutionDescriptor](mpscnnconvolutiondescriptor.md)
  A description of the attributes of a convolution kernel.
- [enum MPSCNNConvolutionFlags](mpscnnconvolutionflags.md)
  Options used to control how kernel weights are stored and used in the CNN kernels
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnconvolution/init(device:weights:).md)
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
### Instance Properties
- [var inputFeatureChannels: Int](mpscnnconvolution/inputfeaturechannels.md)
  The number of feature channels per pixel in the input image.
- [var outputFeatureChannels: Int](mpscnnconvolution/outputfeaturechannels.md)
  The number of feature channels per pixel in the output image.
- [var groups: Int](mpscnnconvolution/groups.md)
  The number of groups that the input and output channels are divided into.
- [var subPixelScaleFactor: Int](mpscnnconvolution/subpixelscalefactor.md)
- [var neuron: MPSCNNNeuron?](mpscnnconvolution/neuron.md)
  The neuron filter to be applied as part of the convolution operation.
- [class MPSCNNNeuron](mpscnnneuron.md)
  A filter that applies a neuron activation function.
- [var neuronType: MPSCNNNeuronType](mpscnnconvolution/neurontype.md)
- [enum MPSCNNNeuronType](mpscnnneurontype.md)
  The types of neuron filter to append to a convolution.
- [var neuronParameterA: Float](mpscnnconvolution/neuronparametera.md)
- [var neuronParameterB: Float](mpscnnconvolution/neuronparameterb.md)
- [var accumulatorPrecisionOption: MPSNNConvolutionAccumulatorPrecisionOption](mpscnnconvolution/accumulatorprecisionoption.md)
- [var channelMultiplier: Int](mpscnnconvolution/channelmultiplier.md)
- [var dataSource: any MPSCNNConvolutionDataSource](mpscnnconvolution/datasource.md)
- [var fusedNeuronDescriptor: MPSNNNeuronDescriptor?](mpscnnconvolution/fusedneurondescriptor.md)
- [var neuronParameterC: Float](mpscnnconvolution/neuronparameterc.md)
### Instance Methods
- [func exportWeightsAndBiases(with: any MTLCommandBuffer, resultStateCanBeTemporary: Bool) -> MPSCNNConvolutionWeightsAndBiasesState](mpscnnconvolution/exportweightsandbiases(with:resultstatecanbetemporary:).md)
- [func reloadWeightsAndBiases(with: any MPSCNNConvolutionDataSource)](mpscnnconvolution/reloadweightsandbiases(with:).md)
- [func reloadWeightsAndBiases(with: any MTLCommandBuffer, state: MPSCNNConvolutionWeightsAndBiasesState)](mpscnnconvolution/reloadweightsandbiases(with:state:).md)
- [func reloadWeightsAndBiasesFromDataSource()](mpscnnconvolution/reloadweightsandbiasesfromdatasource.md)
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNConvolutionGradientState?](mpscnnconvolution/resultstate(sourceimage:sourcestates:destinationimage:).md)
- [func resultStateBatch(sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSCNNConvolutionGradientState]?](mpscnnconvolution/resultstatebatch(sourceimage:sourcestates:destinationimage:).md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNConvolutionGradientState?](mpscnnconvolution/temporaryresultstate(commandbuffer:sourceimage:sourcestates:destinationimage:).md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSCNNConvolutionGradientState]?](mpscnnconvolution/temporaryresultstatebatch(commandbuffer:sourceimage:sourcestates:destinationimage:).md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)
### Inherited By
- [MPSCNNFullyConnected](mpscnnfullyconnected.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

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
  An object that exposes a gradient convolution kernel’s gradient with respect to weights and biases.
- [protocol MPSImageSizeEncodingState](mpsimagesizeencodingstate.md)
  A protocol for objects that contain information about an image size elsewhere in the graph.
- [class MPSCNNConvolutionWeightsAndBiasesState](mpscnnconvolutionweightsandbiasesstate.md)
  A class that stores weights and biases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolution)*