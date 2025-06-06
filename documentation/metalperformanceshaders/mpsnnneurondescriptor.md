# MPSNNNeuronDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: cl

An object that specifies properties used by a neuron kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSNNNeuronDescriptor : NSObject
```

## Topics

### Instance Properties
- [var a: Float](mpsnnneurondescriptor/2942316-a.md)
- [var b: Float](mpsnnneurondescriptor/2942302-b.md)
- [var c: Float](mpsnnneurondescriptor/2942305-c.md)
- [var data: Data?](mpsnnneurondescriptor/2942299-data.md)
- [var neuronType: MPSCNNNeuronType](mpsnnneurondescriptor/2942292-neurontype.md)
### Type Methods
- [class func cnnNeuronDescriptor(with: MPSCNNNeuronType) -> MPSNNNeuronDescriptor](mpsnnneurondescriptor/2942307-cnnneurondescriptor.md)
- [class func cnnNeuronDescriptor(with: MPSCNNNeuronType, a: Float) -> MPSNNNeuronDescriptor](mpsnnneurondescriptor/2942301-cnnneurondescriptor.md)
- [class func cnnNeuronDescriptor(with: MPSCNNNeuronType, a: Float, b: Float) -> MPSNNNeuronDescriptor](mpsnnneurondescriptor/2942295-cnnneurondescriptor.md)
- [class func cnnNeuronDescriptor(with: MPSCNNNeuronType, a: Float, b: Float, c: Float) -> MPSNNNeuronDescriptor](mpsnnneurondescriptor/2942296-cnnneurondescriptor.md)
- [class func cnnNeuronPReLUDescriptor(with: Data, noCopy: Bool) -> MPSNNNeuronDescriptor](mpsnnneurondescriptor/2942317-cnnneuronpreludescriptor.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnneurondescriptor)*