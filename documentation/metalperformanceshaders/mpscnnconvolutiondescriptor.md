# MPSCNNConvolutionDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: cl

A description of the attributes of a convolution kernel.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNConvolutionDescriptor : NSObject
```

#### Overview

You use an [`MPSCNNConvolutionDescriptor`](mpscnnconvolutiondescriptor.md) object to describe the properties of an [`MPSCNNConvolution`](mpscnnconvolution.md) kernel such as its size, pixel format and CPU cache mode.

## Topics

### Initializers
- [init?(coder: NSCoder)](mpscnnconvolutiondescriptor/2867024-init.md)
- [init(kernelWidth: Int, kernelHeight: Int, inputFeatureChannels: Int, outputFeatureChannels: Int)](mpscnnconvolutiondescriptor/1648813-init.md)
- [init(kernelWidth: Int, kernelHeight: Int, inputFeatureChannels: Int, outputFeatureChannels: Int, neuronFilter: MPSCNNNeuron?)](mpscnnconvolutiondescriptor/1648876-init.md)
  Creates a convolution descriptor with an optional neuron filter.
### Instance Properties
- [var groups: Int](mpscnnconvolutiondescriptor/1648849-groups.md)
  The number of groups that the input and output channels are divided into.
- [var inputFeatureChannels: Int](mpscnnconvolutiondescriptor/1648934-inputfeaturechannels.md)
  The number of feature channels per pixel in the input image.
- [var kernelHeight: Int](mpscnnconvolutiondescriptor/1648904-kernelheight.md)
  The height of the kernel window.
- [var kernelWidth: Int](mpscnnconvolutiondescriptor/1648959-kernelwidth.md)
  The width of the kernel window.
- [var outputFeatureChannels: Int](mpscnnconvolutiondescriptor/1648852-outputfeaturechannels.md)
  The number of feature channels per pixel in the output image.
- [var strideInPixelsX: Int](mpscnnconvolutiondescriptor/1648908-strideinpixelsx.md)
  The output stride (downsampling factor) in the x dimension.
- [var strideInPixelsY: Int](mpscnnconvolutiondescriptor/1648847-strideinpixelsy.md)
  The output stride (downsampling factor) in the y dimension.
- [var neuron: MPSCNNNeuron?](mpscnnconvolutiondescriptor/1829442-neuron.md)
  The neuron filter to be applied as part of the convolution operation.
- [var dilationRateX: Int](mpscnnconvolutiondescriptor/2881195-dilationratex.md)
- [var dilationRateY: Int](mpscnnconvolutiondescriptor/2881196-dilationratey.md)
- [func neuronParameterA() -> Float](mpscnnconvolutiondescriptor/2875215-neuronparametera.md)
- [func neuronParameterB() -> Float](mpscnnconvolutiondescriptor/2875213-neuronparameterb.md)
- [func neuronType() -> MPSCNNNeuronType](mpscnnconvolutiondescriptor/2875219-neurontype.md)
- [var fusedNeuronDescriptor: MPSNNNeuronDescriptor](mpscnnconvolutiondescriptor/2953957-fusedneurondescriptor.md)
### Instance Methods
- [func encode(with: NSCoder)](mpscnnconvolutiondescriptor/2866972-encode.md)
- [func setBatchNormalizationParametersForInferenceWithMean(UnsafePointer<Float>?, variance: UnsafePointer<Float>?, gamma: UnsafePointer<Float>?, beta: UnsafePointer<Float>?, epsilon: Float)](mpscnnconvolutiondescriptor/2867057-setbatchnormalizationparametersf.md)
- [func setNeuronToPReLUWithParametersA(Data)](mpscnnconvolutiondescriptor/2921663-setneurontopreluwithparametersa.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float)](mpscnnconvolutiondescriptor/2921657-setneurontype.md)
### Type Properties
- [class var supportsSecureCoding: Bool](mpscnnconvolutiondescriptor/2867154-supportssecurecoding.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor)*