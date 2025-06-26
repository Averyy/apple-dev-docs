# MPSCNNNeuronType

**Framework**: Metal Performance Shaders  
**Kind**: enum

The types of neuron filter to append to a convolution.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum MPSCNNNeuronType
```

## Topics

### Enumeration Cases
- [MPSCNNNeuronType.none](mpscnnneurontype/none.md)
  A neuron type indicating no neuron filter.
- [MPSCNNNeuronType.reLU](mpscnnneurontype/relu.md)
  A neuron type indicating a rectified linear unit neuron filter.
- [MPSCNNNeuronType.linear](mpscnnneurontype/linear.md)
  A neuron type indicating a linear neuron filter.
- [MPSCNNNeuronType.sigmoid](mpscnnneurontype/sigmoid.md)
  A neuron type indicating a sigmoid neuron filter.
- [MPSCNNNeuronType.hardSigmoid](mpscnnneurontype/hardsigmoid.md)
  A neuron type indicating a hard sigmoid neuron filter.
- [MPSCNNNeuronType.tanH](mpscnnneurontype/tanh.md)
  A neuron type indicating a hyperbolic tangent neuron filter.
- [MPSCNNNeuronType.absolute](mpscnnneurontype/absolute.md)
  A neuron type indicating an absolute neuron filter.
- [MPSCNNNeuronType.softPlus](mpscnnneurontype/softplus.md)
  A neuron type indicating a parametric softplus neuron filter.
- [MPSCNNNeuronType.softSign](mpscnnneurontype/softsign.md)
  A neuron type indicating a softsign neuron filter.
- [MPSCNNNeuronType.ELU](mpscnnneurontype/elu.md)
  A neuron type indicating a parametric exponential linear unit neuron filter.
- [MPSCNNNeuronType.count](mpscnnneurontype/count.md)
- [MPSCNNNeuronType.exponential](mpscnnneurontype/exponential.md)
- [MPSCNNNeuronType.geLU](mpscnnneurontype/gelu.md)
- [MPSCNNNeuronType.logarithm](mpscnnneurontype/logarithm.md)
- [MPSCNNNeuronType.pReLU](mpscnnneurontype/prelu.md)
- [MPSCNNNeuronType.power](mpscnnneurontype/power.md)
- [MPSCNNNeuronType.reLUN](mpscnnneurontype/relun.md)
### Initializers
- [init?(rawValue: Int32)](mpscnnneurontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [var neuronParameterA: Float](mpscnnconvolution/neuronparametera.md)
- [var neuronParameterB: Float](mpscnnconvolution/neuronparameterb.md)
- [var accumulatorPrecisionOption: MPSNNConvolutionAccumulatorPrecisionOption](mpscnnconvolution/accumulatorprecisionoption.md)
- [var channelMultiplier: Int](mpscnnconvolution/channelmultiplier.md)
- [var dataSource: any MPSCNNConvolutionDataSource](mpscnnconvolution/datasource.md)
- [var fusedNeuronDescriptor: MPSNNNeuronDescriptor?](mpscnnconvolution/fusedneurondescriptor.md)
- [var neuronParameterC: Float](mpscnnconvolution/neuronparameterc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneurontype)*