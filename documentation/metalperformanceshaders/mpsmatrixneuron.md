# MPSMatrixNeuron

**Framework**: Metal Performance Shaders  
**Kind**: cl

A neuron activation kernel that operates on matrices.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixNeuron : MPSMatrixUnaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixneuron/2935600-init.md)
- [init(device: any MTLDevice)](mpsmatrixneuron/2935603-init.md)
### Instance Properties
- [var alpha: Double](mpsmatrixneuron/2935605-alpha.md)
- [var sourceInputFeatureChannels: Int](mpsmatrixneuron/2935599-sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](mpsmatrixneuron/2935607-sourcenumberoffeaturevectors.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixneuron/2935604-copy.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, biasVector: MPSVector?, resultMatrix: MPSMatrix)](mpsmatrixneuron/2935606-encode.md)
- [func neuronParameterA() -> Float](mpsmatrixneuron/2935583-neuronparametera.md)
- [func neuronParameterB() -> Float](mpsmatrixneuron/2935585-neuronparameterb.md)
- [func neuronParameterC() -> Float](mpsmatrixneuron/2935598-neuronparameterc.md)
- [func neuronType() -> MPSCNNNeuronType](mpsmatrixneuron/2935587-neurontype.md)
- [func setNeuronToPReLUWithParametersA(Data)](mpsmatrixneuron/2935610-setneurontopreluwithparametersa.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](mpsmatrixneuron/2935590-setneurontype.md)

## Relationships

### Inherits From
- [MPSMatrixUnaryKernel](mpsmatrixunarykernel.md)

## See Also

- [class MPSMatrixFullyConnected](mpsmatrixfullyconnected.md)
  A kernel for applying a fully connected neural network layer.
- [class MPSMatrixFullyConnectedGradient](mpsmatrixfullyconnectedgradient.md)
  A kernel for applying a fully gradient connected neural network layer.
- [class MPSMatrixNeuronGradient](mpsmatrixneurongradient.md)
  A gradient neuron activation kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixneuron)*