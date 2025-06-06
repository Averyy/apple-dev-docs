# MPSNNForwardLossNode

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
class MPSNNForwardLossNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, labels: MPSNNImageNode, lossDescriptor: MPSCNNLossDescriptor)](mpsnnforwardlossnode/3131832-init.md)
- [init(source: MPSNNImageNode, labels: MPSNNImageNode, weights: MPSNNImageNode?, lossDescriptor: MPSCNNLossDescriptor)](mpsnnforwardlossnode/3131833-init.md)
- [init(source: MPSNNImageNode, labels: MPSNNImageNode, weights: MPSNNImageNode, lossDescriptor: MPSCNNLossDescriptor)](mpsnnforwardlossnode/3131838-init.md)
- [init(sources: [MPSNNImageNode], lossDescriptor: MPSCNNLossDescriptor)](mpsnnforwardlossnode/3131834-init.md)
### Instance Properties
- [var delta: Float](mpsnnforwardlossnode/3131826-delta.md)
- [var epsilon: Float](mpsnnforwardlossnode/3131827-epsilon.md)
- [var labelSmoothing: Float](mpsnnforwardlossnode/3131835-labelsmoothing.md)
- [var lossType: MPSCNNLossType](mpsnnforwardlossnode/3131836-losstype.md)
- [var numberOfClasses: Int](mpsnnforwardlossnode/3131840-numberofclasses.md)
- [var propertyCallBack: (any MPSNNLossCallback)?](mpsnnforwardlossnode/3131841-propertycallback.md)
- [var reduceAcrossBatch: Bool](mpsnnforwardlossnode/3547987-reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](mpsnnforwardlossnode/3131842-reductiontype.md)
- [var weight: Float](mpsnnforwardlossnode/3131843-weight.md)
### Instance Methods
- [func gradientFilter(withSource: MPSNNImageNode) -> MPSNNLossGradientNode](mpsnnforwardlossnode/3131828-gradientfilter.md)
- [func gradientFilter(withSources: [MPSNNImageNode]) -> MPSNNLossGradientNode](mpsnnforwardlossnode/3131829-gradientfilter.md)
- [func gradientFilters(withSource: MPSNNImageNode) -> [MPSNNLossGradientNode]](mpsnnforwardlossnode/3131830-gradientfilters.md)
- [func gradientFilters(withSources: [MPSNNImageNode]) -> [MPSNNLossGradientNode]](mpsnnforwardlossnode/3131831-gradientfilters.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnforwardlossnode)*