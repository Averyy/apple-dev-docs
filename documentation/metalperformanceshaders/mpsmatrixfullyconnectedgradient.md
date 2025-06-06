# MPSMatrixFullyConnectedGradient

**Framework**: Metal Performance Shaders  
**Kind**: cl

A kernel for applying a fully gradient connected neural network layer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixFullyConnectedGradient : MPSMatrixBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixfullyconnectedgradient/2966667-init.md)
- [init(device: any MTLDevice)](mpsmatrixfullyconnectedgradient/2966668-init.md)
### Instance Properties
- [var alpha: Double](mpsmatrixfullyconnectedgradient/2966663-alpha.md)
- [var sourceInputFeatureChannels: Int](mpsmatrixfullyconnectedgradient/2966669-sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](mpsmatrixfullyconnectedgradient/2966670-sourcenumberoffeaturevectors.md)
- [var sourceOutputFeatureChannels: Int](mpsmatrixfullyconnectedgradient/2966671-sourceoutputfeaturechannels.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixfullyconnectedgradient/2966664-copy.md)
- [func encodeForData(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, weightMatrix: MPSMatrix, resultGradientForDataMatrix: MPSMatrix)](mpsmatrixfullyconnectedgradient/2966665-encodefordata.md)
- [func encodeForWeightsAndBias(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, inputMatrix: MPSMatrix, resultGradientForWeightMatrix: MPSMatrix, resultGradientForBiasVector: MPSVector?)](mpsmatrixfullyconnectedgradient/2966666-encodeforweightsandbias.md)

## Relationships

### Inherits From
- [MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)

## See Also

- [class MPSMatrixFullyConnected](mpsmatrixfullyconnected.md)
  A kernel for applying a fully connected neural network layer.
- [class MPSMatrixNeuron](mpsmatrixneuron.md)
  A neuron activation kernel that operates on matrices.
- [class MPSMatrixNeuronGradient](mpsmatrixneurongradient.md)
  A gradient neuron activation kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixfullyconnectedgradient)*