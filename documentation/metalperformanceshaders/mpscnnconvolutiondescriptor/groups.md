# groups

**Framework**: Metal Performance Shaders  
**Kind**: property

The number of groups that the input and output channels are divided into.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var groups: Int { get set }
```

#### Discussion

The default value is `1`.

Groups let you reduce parametrization. If the value of this property is set to `n`, the input is divided into `n` groups with `inputFeatureChannels``/n` channels in each group. Similarly, the output is divided into `n` groups with `outputFeatureChannels/n` channels in each group.  The `ith` group in the input is only connected to the `ith` group in the output, so the number of weights (parameters) needed is reduced by a factor of `n`. Both the value of the [`inputFeatureChannels`](mpscnnconvolutiondescriptor/inputfeaturechannels.md) and [`outputFeatureChannels`](mpscnnconvolutiondescriptor/outputfeaturechannels.md) properties must be divisible by `n` and the number of channels in each group must be a multiple of `4`.

## See Also

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
- [var fusedNeuronDescriptor: MPSNNNeuronDescriptor](mpscnnconvolutiondescriptor/fusedneurondescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/groups)*