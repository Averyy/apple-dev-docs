# MPSMatrixNeuron

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSMatrixNeuron
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixneuron/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsmatrixneuron/init(device:).md)
### Instance Properties
- [var alpha: Double](mpsmatrixneuron/alpha.md)
- [var sourceInputFeatureChannels: Int](mpsmatrixneuron/sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](mpsmatrixneuron/sourcenumberoffeaturevectors.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixneuron/copy(with:device:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, biasVector: MPSVector?, resultMatrix: MPSMatrix)](mpsmatrixneuron/encode(commandbuffer:inputmatrix:biasvector:resultmatrix:).md)
- [func neuronParameterA() -> Float](mpsmatrixneuron/neuronparametera.md)
- [func neuronParameterB() -> Float](mpsmatrixneuron/neuronparameterb.md)
- [func neuronParameterC() -> Float](mpsmatrixneuron/neuronparameterc.md)
- [func neuronType() -> MPSCNNNeuronType](mpsmatrixneuron/neurontype.md)
- [func setNeuronToPReLUWithParametersA(Data)](mpsmatrixneuron/setneurontopreluwithparametersa(_:).md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](mpsmatrixneuron/setneurontype(_:parametera:parameterb:parameterc:).md)

## Relationships

### Inherits From
- [MPSMatrixUnaryKernel](mpsmatrixunarykernel.md)
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

- [class MPSMatrixFullyConnected](mpsmatrixfullyconnected.md)
  A kernel for applying a fully connected neural network layer.
- [class MPSMatrixFullyConnectedGradient](mpsmatrixfullyconnectedgradient.md)
  A kernel for applying a fully gradient connected neural network layer.
- [class MPSMatrixNeuronGradient](mpsmatrixneurongradient.md)
  A gradient neuron activation kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixneuron)*