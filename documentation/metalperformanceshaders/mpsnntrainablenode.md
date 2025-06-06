# MPSNNTrainableNode

**Framework**: Metal Performance Shaders  
**Kind**: intf

A protocol that defines methods that determine whether and when neural network training parameters are updated.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
protocol MPSNNTrainableNode
```

## Topics

### Instance Properties
- [var trainingStyle: MPSNNTrainingStyle](mpsnntrainablenode/2952971-trainingstyle.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
### Conforming Types
- [MPSCNNBatchNormalizationGradientNode](mpscnnbatchnormalizationgradientnode.md)
- [MPSCNNBatchNormalizationNode](mpscnnbatchnormalizationnode.md)
- [MPSCNNConvolutionGradientNode](mpscnnconvolutiongradientnode.md)
- [MPSCNNConvolutionNode](mpscnnconvolutionnode.md)
- [MPSCNNGroupNormalizationGradientNode](mpscnngroupnormalizationgradientnode.md)
- [MPSCNNGroupNormalizationNode](mpscnngroupnormalizationnode.md)
- [MPSCNNInstanceNormalizationGradientNode](mpscnninstancenormalizationgradientnode.md)
- [MPSCNNInstanceNormalizationNode](mpscnninstancenormalizationnode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnntrainablenode)*