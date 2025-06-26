# MPSCNNNeuronELU

**Framework**: Metal Performance Shaders  
**Kind**: class

A parametric ELU neuron filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNNeuronELU
```

#### Overview

For each pixel in an image, the filter applies the following function:

![f(x) = a * (exp(x) - 1) if x <  0 | f(x) = [` a * (exp(x) - 1) if x <  0`](https://developer.apple.commedia-2903539)

## Topics

### Initializers
- [init(device: any MTLDevice, a: Float)](mpscnnneuronelu/init(device:a:).md)
  Initializes a parametric ELU neuron filter.

## Relationships

### Inherits From
- [MPSCNNNeuron](mpscnnneuron.md)
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

- [class MPSCNNNeuronAbsolute](mpscnnneuronabsolute.md)
  An absolute neuron filter.
- [class MPSCNNNeuronHardSigmoid](mpscnnneuronhardsigmoid.md)
  A hard sigmoid neuron filter.
- [class MPSCNNNeuronLinear](mpscnnneuronlinear.md)
  A linear neuron filter.
- [class MPSCNNNeuronPReLU](mpscnnneuronprelu.md)
  A parametric ReLU (Rectified Linear Unit) neuron filter.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuronelu)*