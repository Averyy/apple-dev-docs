# MPSNNOptimizerStochasticGradientDescent

**Framework**: Metal Performance Shaders  
**Kind**: cl

An optimization layer that performs a gradient descent with an optional momentum update.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNOptimizerStochasticGradientDescent : MPSNNOptimizer
```

## Topics

### Initializers
- [init(device: any MTLDevice, learningRate: Float)](mpsnnoptimizerstochasticgradientdescent/2966741-init.md)
- [init(device: any MTLDevice, momentumScale: Float, useNesterovMomentum: Bool, optimizerDescriptor: MPSNNOptimizerDescriptor)](mpsnnoptimizerstochasticgradientdescent/3675591-init.md)
- [init(device: any MTLDevice, momentumScale: Float, useNestrovMomentum: Bool, optimizerDescriptor: MPSNNOptimizerDescriptor)](mpsnnoptimizerstochasticgradientdescent/2966742-init.md)
### Instance Properties
- [var momentumScale: Float](mpsnnoptimizerstochasticgradientdescent/2966743-momentumscale.md)
- [var useNesterovMomentum: Bool](mpsnnoptimizerstochasticgradientdescent/3675592-usenesterovmomentum.md)
- [var useNestrovMomentum: Bool](mpsnnoptimizerstochasticgradientdescent/2966744-usenestrovmomentum.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationGradientState: MPSCNNBatchNormalizationState, batchNormalizationSourceState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizerstochasticgradientdescent/3013785-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizerstochasticgradientdescent/3019336-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, convolutionGradientState: MPSCNNConvolutionGradientState, convolutionSourceState: MPSCNNConvolutionWeightsAndBiasesState, inputMomentumVectors: [MPSVector]?, resultState: MPSCNNConvolutionWeightsAndBiasesState)](mpsnnoptimizerstochasticgradientdescent/3013786-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientMatrix: MPSMatrix, inputValuesMatrix: MPSMatrix, inputMomentumMatrix: MPSMatrix?, resultValuesMatrix: MPSMatrix)](mpsnnoptimizerstochasticgradientdescent/3197828-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientVector: MPSVector, inputValuesVector: MPSVector, inputMomentumVector: MPSVector?, resultValuesVector: MPSVector)](mpsnnoptimizerstochasticgradientdescent/2966740-encode.md)

## Relationships

### Inherits From
- [MPSNNOptimizer](mpsnnoptimizer.md)

## See Also

- [class MPSNNOptimizerAdam](mpsnnoptimizeradam.md)
  An optimization layer that performs an Adam pdate.
- [class MPSNNOptimizerRMSProp](mpsnnoptimizerrmsprop.md)
  An optimization layer that performs a root mean square propagation update.
- [class MPSNNOptimizer](mpsnnoptimizer.md)
  The base class for optimization layers.
- [class MPSNNOptimizerDescriptor](mpsnnoptimizerdescriptor.md)
  An object that specifies properties used by an optimizer kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizerstochasticgradientdescent)*