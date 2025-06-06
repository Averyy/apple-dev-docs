# MPSCNNNeuronPReLU

**Framework**: Metal Performance Shaders  
**Kind**: cl

A parametric ReLU (Rectified Linear Unit) neuron filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNNeuronPReLU : MPSCNNNeuron
```

#### Overview

For each pixel in an image, the filter applies the following function:

![f(x_i) = x_i, if x_i &gt;= 0 | a_i * x_i if x_i &lt; 0](https://docs-assets.developer.apple.com/published/7bf64e09ae/6a48ed04-382c-4b68-9ea0-1f726e9fef05.png)

Where `i` in `[0 ... channels - 1]`. That is, parameters `a``ᵢ` are learned and applied to each channel separately. Compare this to [`MPSCNNNeuronReLU`](mpscnnneuronrelu.md) where parameter `a` is shared across all channels.

## Topics

### Initializers
- [init(device: any MTLDevice, a: UnsafePointer<Float>, count: Int)](mpscnnneuronprelu/2921661-init.md)

## Relationships

### Inherits From
- [MPSCNNNeuron](mpscnnneuron.md)

## See Also

- [class MPSCNNNeuronAbsolute](mpscnnneuronabsolute.md)
  An absolute neuron filter.
- [class MPSCNNNeuronELU](mpscnnneuronelu.md)
  A parametric ELU neuron filter.
- [class MPSCNNNeuronHardSigmoid](mpscnnneuronhardsigmoid.md)
  A hard sigmoid neuron filter.
- [class MPSCNNNeuronLinear](mpscnnneuronlinear.md)
  A linear neuron filter.
- [class MPSCNNNeuronReLUN](mpscnnneuronrelun.md)
  A ReLUN neuron filter.
- [class MPSCNNNeuronReLU](mpscnnneuronrelu.md)
  A ReLU (Rectified Linear Unit) neuron filter.
- [class MPSCNNNeuronSigmoid](mpscnnneuronsigmoid.md)
  A sigmoid neuron filter.
- [class MPSCNNNeuronSoftPlus](mpscnnneuronsoftplus.md)
  A parametric softplus neuron filter.
- [class MPSCNNNeuronSoftSign](mpscnnneuronsoftsign.md)
  A softsign neuron filter.
- [class MPSCNNNeuronTanH](mpscnnneurontanh.md)
  A hyperbolic tangent neuron filter.
- [class MPSCNNNeuron](mpscnnneuron.md)
  A filter that applies a neuron activation function.
- [class MPSCNNNeuronExponential](mpscnnneuronexponential.md)
  An exponential neuron filter.
- [class MPSCNNNeuronGradient](mpscnnneurongradient.md)
  A gradient neuron filter.
- [class MPSCNNNeuronLogarithm](mpscnnneuronlogarithm.md)
  A logarithm neuron filter.
- [class MPSCNNNeuronPower](mpscnnneuronpower.md)
  A power neuron filter.
- [class MPSNNNeuronDescriptor](mpsnnneurondescriptor.md)
  An object that specifies properties used by a neuron kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuronprelu)*