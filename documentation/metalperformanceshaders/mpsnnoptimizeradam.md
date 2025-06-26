# MPSNNOptimizerAdam

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSNNOptimizerAdam
```

## Topics

### Initializers
- [init(device: any MTLDevice, beta1: Double, beta2: Double, epsilon: Float, timeStep: Int, optimizerDescriptor: MPSNNOptimizerDescriptor)](mpsnnoptimizeradam/init(device:beta1:beta2:epsilon:timestep:optimizerdescriptor:).md)
- [init(device: any MTLDevice, learningRate: Float)](mpsnnoptimizeradam/init(device:learningrate:).md)
### Instance Properties
- [var beta1: Double](mpsnnoptimizeradam/beta1.md)
- [var beta2: Double](mpsnnoptimizeradam/beta2.md)
- [var epsilon: Float](mpsnnoptimizeradam/epsilon.md)
- [var timeStep: Int](mpsnnoptimizeradam/timestep.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationGradientState: MPSCNNBatchNormalizationState, batchNormalizationSourceState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector], inputVelocityVectors: [MPSVector], maximumVelocityVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizeradam/encode(commandbuffer:batchnormalizationgradientstate:batchnormalizationsourcestate:inputmomentumvectors:inputvelocityvectors:maximumvelocityvectors:resultstate:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationGradientState: MPSCNNBatchNormalizationState, batchNormalizationSourceState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector]?, inputVelocityVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizeradam/encode(commandbuffer:batchnormalizationgradientstate:batchnormalizationsourcestate:inputmomentumvectors:inputvelocityvectors:resultstate:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector], inputVelocityVectors: [MPSVector], maximumVelocityVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizeradam/encode(commandbuffer:batchnormalizationstate:inputmomentumvectors:inputvelocityvectors:maximumvelocityvectors:resultstate:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector]?, inputVelocityVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)](mpsnnoptimizeradam/encode(commandbuffer:batchnormalizationstate:inputmomentumvectors:inputvelocityvectors:resultstate:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, convolutionGradientState: MPSCNNConvolutionGradientState, convolutionSourceState: MPSCNNConvolutionWeightsAndBiasesState, inputMomentumVectors: [MPSVector], inputVelocityVectors: [MPSVector], maximumVelocityVectors: [MPSVector]?, resultState: MPSCNNConvolutionWeightsAndBiasesState)](mpsnnoptimizeradam/encode(commandbuffer:convolutiongradientstate:convolutionsourcestate:inputmomentumvectors:inputvelocityvectors:maximumvelocityvectors:resultstate:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, convolutionGradientState: MPSCNNConvolutionGradientState, convolutionSourceState: MPSCNNConvolutionWeightsAndBiasesState, inputMomentumVectors: [MPSVector]?, inputVelocityVectors: [MPSVector]?, resultState: MPSCNNConvolutionWeightsAndBiasesState)](mpsnnoptimizeradam/encode(commandbuffer:convolutiongradientstate:convolutionsourcestate:inputmomentumvectors:inputvelocityvectors:resultstate:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientMatrix: MPSMatrix, inputValuesMatrix: MPSMatrix, inputMomentumMatrix: MPSMatrix, inputVelocityMatrix: MPSMatrix, maximumVelocityMatrix: MPSMatrix?, resultValuesMatrix: MPSMatrix)](mpsnnoptimizeradam/encode(commandbuffer:inputgradientmatrix:inputvaluesmatrix:inputmomentummatrix:inputvelocitymatrix:maximumvelocitymatrix:resultvaluesmatrix:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientMatrix: MPSMatrix, inputValuesMatrix: MPSMatrix, inputMomentumMatrix: MPSMatrix, inputVelocityMatrix: MPSMatrix, resultValuesMatrix: MPSMatrix)](mpsnnoptimizeradam/encode(commandbuffer:inputgradientmatrix:inputvaluesmatrix:inputmomentummatrix:inputvelocitymatrix:resultvaluesmatrix:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientVector: MPSVector, inputValuesVector: MPSVector, inputMomentumVector: MPSVector, inputVelocityVector: MPSVector, maximumVelocityVector: MPSVector?, resultValuesVector: MPSVector)](mpsnnoptimizeradam/encode(commandbuffer:inputgradientvector:inputvaluesvector:inputmomentumvector:inputvelocityvector:maximumvelocityvector:resultvaluesvector:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputGradientVector: MPSVector, inputValuesVector: MPSVector, inputMomentumVector: MPSVector, inputVelocityVector: MPSVector, resultValuesVector: MPSVector)](mpsnnoptimizeradam/encode(commandbuffer:inputgradientvector:inputvaluesvector:inputmomentumvector:inputvelocityvector:resultvaluesvector:).md)

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