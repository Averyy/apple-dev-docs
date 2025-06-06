# MPSCNNNeuron

**Framework**: Metal Performance Shaders  
**Kind**: cl

A filter that applies a neuron activation function.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNNeuron : MPSCNNKernel
```

#### Overview

Do not use this class directly; use one of the [`MPSCNNNeuron`](mpscnnneuron.md) subclasses instead.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnneuron/2867058-init.md)
- [init(device: any MTLDevice, neuronDescriptor: MPSNNNeuronDescriptor)](mpscnnneuron/2942315-init.md)
### Instance Properties
- [var a: Float](mpscnnneuron/2942297-a.md)
- [var b: Float](mpscnnneuron/2942306-b.md)
- [var c: Float](mpscnnneuron/2942303-c.md)
- [var data: Data?](mpscnnneuron/2942308-data.md)
- [var neuronType: MPSCNNNeuronType](mpscnnneuron/2942309-neurontype.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)

## See Also

- [class MPSCNNNeuronAbsolute](mpscnnneuronabsolute.md)
  An absolute neuron filter.
- [class MPSCNNNeuronELU](mpscnnneuronelu.md)
  A parametric ELU neuron filter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuron)*