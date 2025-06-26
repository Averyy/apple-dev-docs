# MPSMatrixFullyConnected

**Framework**: Metal Performance Shaders  
**Kind**: class

A kernel for applying a fully connected neural network layer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixFullyConnected
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixfullyconnected/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsmatrixfullyconnected/init(device:).md)
### Instance Properties
- [var alpha: Double](mpsmatrixfullyconnected/alpha.md)
- [var sourceInputFeatureChannels: Int](mpsmatrixfullyconnected/sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](mpsmatrixfullyconnected/sourcenumberoffeaturevectors.md)
- [var sourceOutputFeatureChannels: Int](mpsmatrixfullyconnected/sourceoutputfeaturechannels.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixfullyconnected/copy(with:device:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, weightMatrix: MPSMatrix, biasVector: MPSVector?, resultMatrix: MPSMatrix)](mpsmatrixfullyconnected/encode(commandbuffer:inputmatrix:weightmatrix:biasvector:resultmatrix:).md)
- [func neuronParameterA() -> Float](mpsmatrixfullyconnected/neuronparametera.md)
- [func neuronParameterB() -> Float](mpsmatrixfullyconnected/neuronparameterb.md)
- [func neuronParameterC() -> Float](mpsmatrixfullyconnected/neuronparameterc.md)
- [func neuronType() -> MPSCNNNeuronType](mpsmatrixfullyconnected/neurontype.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](mpsmatrixfullyconnected/setneurontype(_:parametera:parameterb:parameterc:).md)

## Relationships

### Inherits From
- [MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)
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

- [class MPSMatrixFullyConnectedGradient](mpsmatrixfullyconnectedgradient.md)
  A kernel for applying a fully gradient connected neural network layer.
- [class MPSMatrixNeuron](mpsmatrixneuron.md)
  A neuron activation kernel that operates on matrices.
- [class MPSMatrixNeuronGradient](mpsmatrixneurongradient.md)
  A gradient neuron activation kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixfullyconnected)*