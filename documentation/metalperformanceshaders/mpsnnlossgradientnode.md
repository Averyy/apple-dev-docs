# MPSNNLossGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNLossGradientNode : MPSNNGradientFilterNode
```

## Topics

### Initializers
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, labels: MPSNNImageNode, gradientState: MPSNNGradientStateNode?, lossDescriptor: MPSCNNLossDescriptor, isLabelsGradientFilter: Bool)](mpsnnlossgradientnode/3131855-init.md)
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, labels: MPSNNImageNode, weights: MPSNNImageNode?, gradientState: MPSNNGradientStateNode?, lossDescriptor: MPSCNNLossDescriptor, isLabelsGradientFilter: Bool)](mpsnnlossgradientnode/3131856-init.md)
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, labels: MPSNNImageNode, weights: MPSNNImageNode, gradientState: MPSNNGradientStateNode?, lossDescriptor: MPSCNNLossDescriptor, isLabelsGradientFilter: Bool)](mpsnnlossgradientnode/3131862-init.md)
- [init(sources: [MPSNNImageNode], gradientState: MPSNNGradientStateNode?, lossDescriptor: MPSCNNLossDescriptor, isLabelsGradientFilter: Bool)](mpsnnlossgradientnode/3131857-init.md)
### Instance Properties
- [var delta: Float](mpsnnlossgradientnode/3131853-delta.md)
- [var epsilon: Float](mpsnnlossgradientnode/3131854-epsilon.md)
- [var isLabelsGradientFilter: Bool](mpsnnlossgradientnode/3131858-islabelsgradientfilter.md)
- [var labelSmoothing: Float](mpsnnlossgradientnode/3131859-labelsmoothing.md)
- [var lossType: MPSCNNLossType](mpsnnlossgradientnode/3131860-losstype.md)
- [var numberOfClasses: Int](mpsnnlossgradientnode/3131864-numberofclasses.md)
- [var propertyCallBack: (any MPSNNLossCallback)?](mpsnnlossgradientnode/3131865-propertycallback.md)
- [var reduceAcrossBatch: Bool](mpsnnlossgradientnode/3547988-reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](mpsnnlossgradientnode/3131866-reductiontype.md)
- [var weight: Float](mpsnnlossgradientnode/3131867-weight.md)

## Relationships

### Inherits From
- [MPSNNGradientFilterNode](mpsnngradientfilternode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnlossgradientnode)*