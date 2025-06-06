# MPSMatrixBatchNormalizationGradient

**Framework**: Metal Performance Shaders  
**Kind**: cl

A batch normalization gradient kernel that operates on matrices.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixBatchNormalizationGradient : MPSMatrixBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixbatchnormalizationgradient/2980747-init.md)
- [init(device: any MTLDevice)](mpsmatrixbatchnormalizationgradient/2980748-init.md)
### Instance Properties
- [var epsilon: Float](mpsmatrixbatchnormalizationgradient/2980746-epsilon.md)
- [var sourceInputFeatureChannels: Int](mpsmatrixbatchnormalizationgradient/2980754-sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](mpsmatrixbatchnormalizationgradient/2980755-sourcenumberoffeaturevectors.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixbatchnormalizationgradient/2980744-copy.md)
- [func encode(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, inputMatrix: MPSMatrix, mean: MPSVector, varianceVector: MPSVector, gammaVector: MPSVector?, betaVector: MPSVector?, resultGradientForDataMatrix: MPSMatrix, resultGradientForGammaVector: MPSVector?, resultGradientForBetaVector: MPSVector?)](mpsmatrixbatchnormalizationgradient/2980745-encode.md)
- [func neuronParameterA() -> Float](mpsmatrixbatchnormalizationgradient/2980749-neuronparametera.md)
- [func neuronParameterB() -> Float](mpsmatrixbatchnormalizationgradient/2980750-neuronparameterb.md)
- [func neuronParameterC() -> Float](mpsmatrixbatchnormalizationgradient/2980751-neuronparameterc.md)
- [func neuronType() -> MPSCNNNeuronType](mpsmatrixbatchnormalizationgradient/2980752-neurontype.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](mpsmatrixbatchnormalizationgradient/2980753-setneurontype.md)

## Relationships

### Inherits From
- [MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)

## See Also

- [class MPSMatrixBatchNormalization](mpsmatrixbatchnormalization.md)
  A batch normalization kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixbatchnormalizationgradient)*