# MPSNNOptimizerStochasticGradientDescent

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSNNOptimizerStochasticGradientDescent
```

## Topics

### Initializers
- [init(device: any MTLDevice, learningRate: Float)](mpsnnoptimizerstochasticgradientdescent/init(device:learningrate:).md)
- [init(device: any MTLDevice, momentumScale: Float, useNesterovMomentum: Bool, optimizerDescriptor: MPSNNOptimizerDescriptor)](mpsnnoptimizerstochasticgradientdescent/init(device:momentumscale:usenesterovmomentum:optimizerdescriptor:).md)
- [init(device: any MTLDevice, momentumScale: Float, useNestrovMomentum: Bool, optimizerDescriptor: MPSNNOptimizerDescriptor)](mpsnnoptimizerstochasticgradientdescent/init(device:momentumscale:usenestrovmomentum:optimizerdescriptor:).md)
### Instance Properties
- [var momentumScale: Float](mpsnnoptimizerstochasticgradientdescent/momentumscale.md)
- [var useNesterovMomentum: Bool](mpsnnoptimizerstochasticgradientdescent/usenesterovmomentum.md)
- [var useNestrovMomentum: Bool](mpsnnoptimizerstochasticgradientdescent/usenestrovmomentum.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationGradientState: MPSCNNBatchNormalizationState, batchNormalizationSourceState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizerstochasticgradientdescent/encode(commandbuffer:batchnormalizationgradientstate:batchnormalizationsourcestate:inputmomentumvectors:resultstate:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizerstochasticgradientdescent/encode(commandbuffer:batchnormalizationstate:inputmomentumvectors:resultstate:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, convolutionGradientState: MPSCNNConvolutionGradientState, convolutionSourceState: MPSCNNConvolutionWeightsAndBiasesState, inputMomentumVectors: [MPSVector]?, resultState: MPSCNNConvolutionWeightsAndBiasesState)](mpsnnoptimizerstochasticgradientdescent/encode(commandbuffer:convolutiongradientstate:convolutionsourcestate:inputmomentumvectors:resultstate:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientMatrix: MPSMatrix, inputValuesMatrix: MPSMatrix, inputMomentumMatrix: MPSMatrix?, resultValuesMatrix: MPSMatrix)](mpsnnoptimizerstochasticgradientdescent/encode(commandbuffer:inputgradientmatrix:inputvaluesmatrix:inputmomentummatrix:resultvaluesmatrix:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientVector: MPSVector, inputValuesVector: MPSVector, inputMomentumVector: MPSVector?, resultValuesVector: MPSVector)](mpsnnoptimizerstochasticgradientdescent/encode(commandbuffer:inputgradientvector:inputvaluesvector:inputmomentumvector:resultvaluesvector:).md)

## Relationships

### Inherits From
- [MPSNNOptimizer](mpsnnoptimizer.md)
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