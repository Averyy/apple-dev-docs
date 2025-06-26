# MPSNNLossGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNLossGradientNode
```

## Topics

### Initializers
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, labels: MPSNNImageNode, gradientState: MPSNNGradientStateNode?, lossDescriptor: MPSCNNLossDescriptor, isLabelsGradientFilter: Bool)](mpsnnlossgradientnode/init(sourcegradient:sourceimage:labels:gradientstate:lossdescriptor:islabelsgradientfilter:).md)
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, labels: MPSNNImageNode, weights: MPSNNImageNode?, gradientState: MPSNNGradientStateNode?, lossDescriptor: MPSCNNLossDescriptor, isLabelsGradientFilter: Bool)](mpsnnlossgradientnode/init(sourcegradient:sourceimage:labels:weights:gradientstate:lossdescriptor:islabelsgradientfilter:)-3rcen.md)
- [convenience init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, labels: MPSNNImageNode, weights: MPSNNImageNode, gradientState: MPSNNGradientStateNode?, lossDescriptor: MPSCNNLossDescriptor, isLabelsGradientFilter: Bool)](mpsnnlossgradientnode/init(sourcegradient:sourceimage:labels:weights:gradientstate:lossdescriptor:islabelsgradientfilter:)-9eqch.md)
- [init(sources: [MPSNNImageNode], gradientState: MPSNNGradientStateNode?, lossDescriptor: MPSCNNLossDescriptor, isLabelsGradientFilter: Bool)](mpsnnlossgradientnode/init(sources:gradientstate:lossdescriptor:islabelsgradientfilter:).md)
### Instance Properties
- [var delta: Float](mpsnnlossgradientnode/delta.md)
- [var epsilon: Float](mpsnnlossgradientnode/epsilon.md)
- [var isLabelsGradientFilter: Bool](mpsnnlossgradientnode/islabelsgradientfilter.md)
- [var labelSmoothing: Float](mpsnnlossgradientnode/labelsmoothing.md)
- [var lossType: MPSCNNLossType](mpsnnlossgradientnode/losstype.md)
- [var numberOfClasses: Int](mpsnnlossgradientnode/numberofclasses.md)
- [var propertyCallBack: (any MPSNNLossCallback)?](mpsnnlossgradientnode/propertycallback.md)
- [var reduceAcrossBatch: Bool](mpsnnlossgradientnode/reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](mpsnnlossgradientnode/reductiontype.md)
- [var weight: Float](mpsnnlossgradientnode/weight.md)

## Relationships

### Inherits From
- [MPSNNGradientFilterNode](mpsnngradientfilternode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnlossgradientnode)*