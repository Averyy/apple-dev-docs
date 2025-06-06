# MPSNNOptimizerRMSProp

**Framework**: Metal Performance Shaders  
**Kind**: cl

An optimization layer that performs a root mean square propagation update.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNOptimizerRMSProp : MPSNNOptimizer
```

## Topics

### Initializers
- [init(device: any MTLDevice, decay: Double, epsilon: Float, optimizerDescriptor: MPSNNOptimizerDescriptor)](mpsnnoptimizerrmsprop/2966737-init.md)
- [init(device: any MTLDevice, learningRate: Float)](mpsnnoptimizerrmsprop/2966738-init.md)
### Instance Properties
- [var decay: Double](mpsnnoptimizerrmsprop/2966734-decay.md)
- [var epsilon: Float](mpsnnoptimizerrmsprop/2966736-epsilon.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationGradientState: MPSCNNBatchNormalizationState, batchNormalizationSourceState: MPSCNNBatchNormalizationState, inputSumOfSquaresVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizerrmsprop/3013783-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState, inputSumOfSquaresVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizerrmsprop/3019335-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, convolutionGradientState: MPSCNNConvolutionGradientState, convolutionSourceState: MPSCNNConvolutionWeightsAndBiasesState, inputSumOfSquaresVectors: [MPSVector]?, resultState: MPSCNNConvolutionWeightsAndBiasesState)](mpsnnoptimizerrmsprop/3013784-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientMatrix: MPSMatrix, inputValuesMatrix: MPSMatrix, inputSumOfSquaresMatrix: MPSMatrix, resultValuesMatrix: MPSMatrix)](mpsnnoptimizerrmsprop/3197827-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientVector: MPSVector, inputValuesVector: MPSVector, inputSumOfSquaresVector: MPSVector, resultValuesVector: MPSVector)](mpsnnoptimizerrmsprop/2966735-encode.md)

## Relationships

### Inherits From
- [MPSNNOptimizer](mpsnnoptimizer.md)

## See Also

- [class MPSNNOptimizerAdam](mpsnnoptimizeradam.md)
  An optimization layer that performs an Adam pdate.
- [class MPSNNOptimizerStochasticGradientDescent](mpsnnoptimizerstochasticgradientdescent.md)
  An optimization layer that performs a gradient descent with an optional momentum update.
- [class MPSNNOptimizer](mpsnnoptimizer.md)
  The base class for optimization layers.
- [class MPSNNOptimizerDescriptor](mpsnnoptimizerdescriptor.md)
  An object that specifies properties used by an optimizer kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizerrmsprop)*