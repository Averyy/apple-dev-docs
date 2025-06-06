# MPSMatrixFullyConnected

**Framework**: Metal Performance Shaders  
**Kind**: cl

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
class MPSMatrixFullyConnected : MPSMatrixBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixfullyconnected/2935611-init.md)
- [init(device: any MTLDevice)](mpsmatrixfullyconnected/2935584-init.md)
### Instance Properties
- [var alpha: Double](mpsmatrixfullyconnected/2935608-alpha.md)
- [var sourceInputFeatureChannels: Int](mpsmatrixfullyconnected/2935597-sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](mpsmatrixfullyconnected/2935609-sourcenumberoffeaturevectors.md)
- [var sourceOutputFeatureChannels: Int](mpsmatrixfullyconnected/2935592-sourceoutputfeaturechannels.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixfullyconnected/2935595-copy.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, weightMatrix: MPSMatrix, biasVector: MPSVector?, resultMatrix: MPSMatrix)](mpsmatrixfullyconnected/2935596-encode.md)
- [func neuronParameterA() -> Float](mpsmatrixfullyconnected/2935602-neuronparametera.md)
- [func neuronParameterB() -> Float](mpsmatrixfullyconnected/2935591-neuronparameterb.md)
- [func neuronParameterC() -> Float](mpsmatrixfullyconnected/2935594-neuronparameterc.md)
- [func neuronType() -> MPSCNNNeuronType](mpsmatrixfullyconnected/2935588-neurontype.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](mpsmatrixfullyconnected/2935593-setneurontype.md)

## Relationships

### Inherits From
- [MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)

## See Also

- [class MPSMatrixFullyConnectedGradient](mpsmatrixfullyconnectedgradient.md)
  A kernel for applying a fully gradient connected neural network layer.
- [class MPSMatrixNeuron](mpsmatrixneuron.md)
  A neuron activation kernel that operates on matrices.
- [class MPSMatrixNeuronGradient](mpsmatrixneurongradient.md)
  A gradient neuron activation kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixfullyconnected)*