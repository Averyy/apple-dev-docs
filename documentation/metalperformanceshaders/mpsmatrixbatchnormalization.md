# MPSMatrixBatchNormalization

**Framework**: Metal Performance Shaders  
**Kind**: cl

A batch normalization kernel that operates on matrices.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixBatchNormalization : MPSMatrixUnaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixbatchnormalization/2980734-init.md)
- [init(device: any MTLDevice)](mpsmatrixbatchnormalization/2980735-init.md)
### Instance Properties
- [var computeStatistics: Bool](mpsmatrixbatchnormalization/2980730-computestatistics.md)
- [var epsilon: Float](mpsmatrixbatchnormalization/2980733-epsilon.md)
- [var sourceInputFeatureChannels: Int](mpsmatrixbatchnormalization/2980741-sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](mpsmatrixbatchnormalization/2980742-sourcenumberoffeaturevectors.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixbatchnormalization/2980731-copy.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, meanVector: MPSVector, varianceVector: MPSVector, gammaVector: MPSVector?, betaVector: MPSVector?, resultMatrix: MPSMatrix)](mpsmatrixbatchnormalization/2980732-encode.md)
- [func neuronParameterA() -> Float](mpsmatrixbatchnormalization/2980736-neuronparametera.md)
- [func neuronParameterB() -> Float](mpsmatrixbatchnormalization/2980737-neuronparameterb.md)
- [func neuronParameterC() -> Float](mpsmatrixbatchnormalization/2980738-neuronparameterc.md)
- [func neuronType() -> MPSCNNNeuronType](mpsmatrixbatchnormalization/2980739-neurontype.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](mpsmatrixbatchnormalization/2980740-setneurontype.md)

## Relationships

### Inherits From
- [MPSMatrixUnaryKernel](mpsmatrixunarykernel.md)

## See Also

- [class MPSMatrixBatchNormalizationGradient](mpsmatrixbatchnormalizationgradient.md)
  A batch normalization gradient kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixbatchnormalization)*