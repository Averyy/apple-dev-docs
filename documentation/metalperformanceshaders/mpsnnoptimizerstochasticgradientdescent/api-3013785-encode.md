# encode(commandBuffer:batchNormalizationGradientState:batchNormalizationSourceState:inputMomentumVectors:resultState:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationGradientState: MPSCNNBatchNormalizationState, batchNormalizationSourceState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizerstochasticgradientdescent/3013785-encode)*