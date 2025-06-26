# MPSCNNNeuronNode

**Framework**: Metal Performance Shaders  
**Kind**: class

The virtual base class for MPS CNN neuron nodes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNNeuronNode
```

## Topics

### Supporting Types
- [enum MPSCNNNeuronType](mpscnnneurontype.md)
  The types of neuron filter to append to a convolution.
### Initializers
- [convenience init(source: MPSNNImageNode, descriptor: MPSNNNeuronDescriptor)](mpscnnneuronnode/init(source:descriptor:).md)
### Instance Properties
- [var a: Float](mpscnnneuronnode/a.md)
- [var b: Float](mpscnnneuronnode/b.md)
- [var c: Float](mpscnnneuronnode/c.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)
### Inherited By
- [MPSCNNNeuronAbsoluteNode](mpscnnneuronabsolutenode.md)
- [MPSCNNNeuronELUNode](mpscnnneuronelunode.md)
- [MPSCNNNeuronExponentialNode](mpscnnneuronexponentialnode.md)
- [MPSCNNNeuronGeLUNode](mpscnnneurongelunode.md)
- [MPSCNNNeuronHardSigmoidNode](mpscnnneuronhardsigmoidnode.md)
- [MPSCNNNeuronLinearNode](mpscnnneuronlinearnode.md)
- [MPSCNNNeuronLogarithmNode](mpscnnneuronlogarithmnode.md)
- [MPSCNNNeuronPReLUNode](mpscnnneuronprelunode.md)
- [MPSCNNNeuronPowerNode](mpscnnneuronpowernode.md)
- [MPSCNNNeuronReLUNNode](mpscnnneuronrelunnode.md)
- [MPSCNNNeuronReLUNode](mpscnnneuronrelunode.md)
- [MPSCNNNeuronSigmoidNode](mpscnnneuronsigmoidnode.md)
- [MPSCNNNeuronSoftPlusNode](mpscnnneuronsoftplusnode.md)
- [MPSCNNNeuronSoftSignNode](mpscnnneuronsoftsignnode.md)
- [MPSCNNNeuronTanHNode](mpscnnneurontanhnode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSCNNNeuronAbsoluteNode](mpscnnneuronabsolutenode.md)
  A representation of an absolute neuron filter.
- [class MPSCNNNeuronELUNode](mpscnnneuronelunode.md)
  A representation of a parametric ELU neuron filter.
- [class MPSCNNNeuronHardSigmoidNode](mpscnnneuronhardsigmoidnode.md)
  A representation of a hard sigmoid neuron filter.
- [class MPSCNNNeuronLinearNode](mpscnnneuronlinearnode.md)
  A representation of a linear neuron filter.
- [class MPSCNNNeuronPReLUNode](mpscnnneuronprelunode.md)
  A representation a PReLU neuron filter.
- [class MPSCNNNeuronReLUNNode](mpscnnneuronrelunnode.md)
  A representation a ReLUN neuron filter.
- [class MPSCNNNeuronReLUNode](mpscnnneuronrelunode.md)
  A representation a ReLU neuron filter.
- [class MPSCNNNeuronSigmoidNode](mpscnnneuronsigmoidnode.md)
  A representation of a sigmoid neuron filter.
- [class MPSCNNNeuronSoftPlusNode](mpscnnneuronsoftplusnode.md)
  A representation of a parametric softplus neuron filter.
- [class MPSCNNNeuronSoftSignNode](mpscnnneuronsoftsignnode.md)
  A representation of a softsign neuron filter.
- [class MPSCNNNeuronTanHNode](mpscnnneurontanhnode.md)
  A representation of a hyperbolic tangent neuron filter.
- [class MPSCNNNeuronExponentialNode](mpscnnneuronexponentialnode.md)
  A representation of an exponential neuron filter.
- [class MPSCNNNeuronGradientNode](mpscnnneurongradientnode.md)
  A representation of a gradient exponential neuron filter.
- [class MPSCNNNeuronLogarithmNode](mpscnnneuronlogarithmnode.md)
  A representation of a logarithm neuron filter.
- [class MPSCNNNeuronPowerNode](mpscnnneuronpowernode.md)
  A representation of a power neuron filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuronnode)*