# kernelWidth

**Framework**: Metal Performance Shaders  
**Kind**: property

The width of the kernel window.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var kernelWidth: Int { get set }
```

#### Discussion

The default value is `3`.

Any positive non-zero value is valid, including even values. The position of the left edge of the kernel window is given by `offset.x - (kernelWidth>>1)`.

## See Also

- [var groups: Int](mpscnnconvolutiondescriptor/groups.md)
  The number of groups that the input and output channels are divided into.
- [var inputFeatureChannels: Int](mpscnnconvolutiondescriptor/inputfeaturechannels.md)
  The number of feature channels per pixel in the input image.
- [var kernelHeight: Int](mpscnnconvolutiondescriptor/kernelheight.md)
  The height of the kernel window.
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
- [var fusedNeuronDescriptor: MPSNNNeuronDescriptor](mpscnnconvolutiondescriptor/fusedneurondescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/kernelwidth)*