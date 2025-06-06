# encode(commandBuffer:batchNormalizationState:inputMomentumVectors:inputVelocityVectors:maximumVelocityVectors:resultState:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector], inputVelocityVectors: [MPSVector], maximumVelocityVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizeradam/3175014-encode)*