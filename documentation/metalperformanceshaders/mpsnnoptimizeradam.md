# MPSNNOptimizerAdam

**Framework**: Metal Performance Shaders  
**Kind**: cl

An optimization layer that performs an Adam pdate.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNOptimizerAdam : MPSNNOptimizer
```

## Topics

### Initializers
- [init(device: any MTLDevice, beta1: Double, beta2: Double, epsilon: Float, timeStep: Int, optimizerDescriptor: MPSNNOptimizerDescriptor)](mpsnnoptimizeradam/2966718-init.md)
- [init(device: any MTLDevice, learningRate: Float)](mpsnnoptimizeradam/2966719-init.md)
### Instance Properties
- [var beta1: Double](mpsnnoptimizeradam/2966714-beta1.md)
- [var beta2: Double](mpsnnoptimizeradam/2966715-beta2.md)
- [var epsilon: Float](mpsnnoptimizeradam/2966717-epsilon.md)
- [var timeStep: Int](mpsnnoptimizeradam/2966720-timestep.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationGradientState: MPSCNNBatchNormalizationState, batchNormalizationSourceState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector], inputVelocityVectors: [MPSVector], maximumVelocityVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizeradam/3175013-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationGradientState: MPSCNNBatchNormalizationState, batchNormalizationSourceState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector]?, inputVelocityVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizeradam/3013781-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector], inputVelocityVectors: [MPSVector], maximumVelocityVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizeradam/3175014-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector]?, inputVelocityVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizeradam/3019334-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, convolutionGradientState: MPSCNNConvolutionGradientState, convolutionSourceState: MPSCNNConvolutionWeightsAndBiasesState, inputMomentumVectors: [MPSVector], inputVelocityVectors: [MPSVector], maximumVelocityVectors: [MPSVector]?, resultState: MPSCNNConvolutionWeightsAndBiasesState)](mpsnnoptimizeradam/3175015-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, convolutionGradientState: MPSCNNConvolutionGradientState, convolutionSourceState: MPSCNNConvolutionWeightsAndBiasesState, inputMomentumVectors: [MPSVector]?, inputVelocityVectors: [MPSVector]?, resultState: MPSCNNConvolutionWeightsAndBiasesState)](mpsnnoptimizeradam/3013782-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientMatrix: MPSMatrix, inputValuesMatrix: MPSMatrix, inputMomentumMatrix: MPSMatrix, inputVelocityMatrix: MPSMatrix, maximumVelocityMatrix: MPSMatrix?, resultValuesMatrix: MPSMatrix)](mpsnnoptimizeradam/3197825-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientMatrix: MPSMatrix, inputValuesMatrix: MPSMatrix, inputMomentumMatrix: MPSMatrix, inputVelocityMatrix: MPSMatrix, resultValuesMatrix: MPSMatrix)](mpsnnoptimizeradam/3197826-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientVector: MPSVector, inputValuesVector: MPSVector, inputMomentumVector: MPSVector, inputVelocityVector: MPSVector, maximumVelocityVector: MPSVector?, resultValuesVector: MPSVector)](mpsnnoptimizeradam/3175016-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientVector: MPSVector, inputValuesVector: MPSVector, inputMomentumVector: MPSVector, inputVelocityVector: MPSVector, resultValuesVector: MPSVector)](mpsnnoptimizeradam/2966716-encode.md)

## Relationships

### Inherits From
- [MPSNNOptimizer](mpsnnoptimizer.md)

## See Also

- [class MPSNNOptimizerRMSProp](mpsnnoptimizerrmsprop.md)
  An optimization layer that performs a root mean square propagation update.
- [class MPSNNOptimizerStochasticGradientDescent](mpsnnoptimizerstochasticgradientdescent.md)
  An optimization layer that performs a gradient descent with an optional momentum update.
- [class MPSNNOptimizer](mpsnnoptimizer.md)
  The base class for optimization layers.
- [class MPSNNOptimizerDescriptor](mpsnnoptimizerdescriptor.md)
  An object that specifies properties used by an optimizer kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizeradam)*