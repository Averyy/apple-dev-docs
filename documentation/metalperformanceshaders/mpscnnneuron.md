# MPSCNNNeuron

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSCNNNeuron
```

#### Overview

Do not use this class directly; use one of the [`MPSCNNNeuron`](mpscnnneuron.md) subclasses instead.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnneuron/init(coder:device:).md)
- [init(device: any MTLDevice, neuronDescriptor: MPSNNNeuronDescriptor)](mpscnnneuron/init(device:neurondescriptor:).md)
### Instance Properties
- [var a: Float](mpscnnneuron/a.md)
- [var b: Float](mpscnnneuron/b.md)
- [var c: Float](mpscnnneuron/c.md)
- [var data: Data?](mpscnnneuron/data.md)
- [var neuronType: MPSCNNNeuronType](mpscnnneuron/neurontype.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)
### Inherited By
- [MPSCNNNeuronAbsolute](mpscnnneuronabsolute.md)
- [MPSCNNNeuronELU](mpscnnneuronelu.md)
- [MPSCNNNeuronExponential](mpscnnneuronexponential.md)
- [MPSCNNNeuronHardSigmoid](mpscnnneuronhardsigmoid.md)
- [MPSCNNNeuronLinear](mpscnnneuronlinear.md)
- [MPSCNNNeuronLogarithm](mpscnnneuronlogarithm.md)
- [MPSCNNNeuronPReLU](mpscnnneuronprelu.md)
- [MPSCNNNeuronPower](mpscnnneuronpower.md)
- [MPSCNNNeuronReLU](mpscnnneuronrelu.md)
- [MPSCNNNeuronReLUN](mpscnnneuronrelun.md)
- [MPSCNNNeuronSigmoid](mpscnnneuronsigmoid.md)
- [MPSCNNNeuronSoftPlus](mpscnnneuronsoftplus.md)
- [MPSCNNNeuronSoftSign](mpscnnneuronsoftsign.md)
- [MPSCNNNeuronTanH](mpscnnneurontanh.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuron)*