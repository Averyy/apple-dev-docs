# MPSMatrixNeuronGradient

**Framework**: Metal Performance Shaders  
**Kind**: cl

A gradient neuron activation kernel that operates on matrices.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixNeuronGradient : MPSMatrixBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixneurongradient/2966676-init.md)
- [init(device: any MTLDevice)](mpsmatrixneurongradient/2966677-init.md)
### Instance Properties
- [var alpha: Double](mpsmatrixneurongradient/2966673-alpha.md)
- [var sourceInputFeatureChannels: Int](mpsmatrixneurongradient/2966684-sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](mpsmatrixneurongradient/2966685-sourcenumberoffeaturevectors.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixneurongradient/2966674-copy.md)
- [func encode(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, inputMatrix: MPSMatrix, biasVector: MPSVector?, resultGradientForDataMatrix: MPSMatrix, resultGradientForBiasVector: MPSVector?)](mpsmatrixneurongradient/2966675-encode.md)
- [func neuronParameterA() -> Float](mpsmatrixneurongradient/2966678-neuronparametera.md)
- [func neuronParameterB() -> Float](mpsmatrixneurongradient/2966679-neuronparameterb.md)
- [func neuronParameterC() -> Float](mpsmatrixneurongradient/2966680-neuronparameterc.md)
- [func neuronType() -> MPSCNNNeuronType](mpsmatrixneurongradient/2966681-neurontype.md)
- [func setNeuronToPReLUWithParametersA(Data)](mpsmatrixneurongradient/2966682-setneurontopreluwithparametersa.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](mpsmatrixneurongradient/2966683-setneurontype.md)

## Relationships

### Inherits From
- [MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)

## See Also

- [class MPSMatrixFullyConnected](mpsmatrixfullyconnected.md)
  A kernel for applying a fully connected neural network layer.
- [class MPSMatrixFullyConnectedGradient](mpsmatrixfullyconnectedgradient.md)
  A kernel for applying a fully gradient connected neural network layer.
- [class MPSMatrixNeuron](mpsmatrixneuron.md)
  A neuron activation kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixneurongradient)*