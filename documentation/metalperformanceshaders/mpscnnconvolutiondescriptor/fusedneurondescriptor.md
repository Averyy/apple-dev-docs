# fusedNeuronDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: property

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var fusedNeuronDescriptor: MPSNNNeuronDescriptor { get set }
```

## See Also

- [var groups: Int](mpscnnconvolutiondescriptor/groups.md)
  The number of groups that the input and output channels are divided into.
- [var inputFeatureChannels: Int](mpscnnconvolutiondescriptor/inputfeaturechannels.md)
  The number of feature channels per pixel in the input image.
- [var kernelHeight: Int](mpscnnconvolutiondescriptor/kernelheight.md)
  The height of the kernel window.
- [var kernelWidth: Int](mpscnnconvolutiondescriptor/kernelwidth.md)
  The width of the kernel window.
- [var outputFeatureChannels: Int](mpscnnconvolutiondescriptor/outputfeaturechannels.md)
  The number of feature channels per pixel in the output image.
- [var strideInPixelsX: Int](mpscnnconvolutiondescriptor/strideinpixelsx.md)
  The output stride (downsampling factor) in the x dimension.
- [var strideInPixelsY: Int](mpscnnconvolutiondescriptor/strideinpixelsy.md)
  The output stride (downsampling factor) in the y dimension.
- [var neuron: MPSCNNNeuron?](mpscnnconvolutiondescriptor/neuron.md)
  The neuron filter to be applied as part of the convolution operation.
- [var dilationRateX: Int](mpscnnconvolutiondescriptor/dilationratex.md)
- [var dilationRateY: Int](mpscnnconvolutiondescriptor/dilationratey.md)
- [func neuronParameterA() -> Float](mpscnnconvolutiondescriptor/neuronparametera.md)
- [func neuronParameterB() -> Float](mpscnnconvolutiondescriptor/neuronparameterb.md)
- [func neuronType() -> MPSCNNNeuronType](mpscnnconvolutiondescriptor/neurontype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/fusedneurondescriptor)*