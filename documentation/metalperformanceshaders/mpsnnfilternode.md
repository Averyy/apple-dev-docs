# MPSNNFilterNode

**Framework**: Metal Performance Shaders  
**Kind**: class

A placeholder node denoting a neural network filter stage.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNFilterNode
```

## Topics

### Instance Properties
- [var label: String?](mpsnnfilternode/label.md)
- [var paddingPolicy: any MPSNNPadding](mpsnnfilternode/paddingpolicy.md)
- [protocol MPSNNPadding](mpsnnpadding.md)
  The protocol that provides a description of how kernels should pad images.
- [var resultImage: MPSNNImageNode](mpsnnfilternode/resultimage.md)
- [var resultState: MPSNNStateNode?](mpsnnfilternode/resultstate.md)
- [var resultStates: [MPSNNStateNode]?](mpsnnfilternode/resultstates.md)
- [class MPSNNStateNode](mpsnnstatenode.md)
  A placeholder node denoting the position in the graph of a state object.
- [class MPSNNBinaryGradientStateNode](mpsnnbinarygradientstatenode.md)
  A representation of the state created to record the properties of a binary gradient kernel.
- [class MPSNNGradientStateNode](mpsnngradientstatenode.md)
  A representation of the state created to record the properties of a gradient kernel at the time it was encoded.
### Instance Methods
- [func gradientFilter(withSource: MPSNNImageNode) -> MPSNNGradientFilterNode](mpsnnfilternode/gradientfilter(withsource:).md)
- [func gradientFilter(withSources: [MPSNNImageNode]) -> MPSNNGradientFilterNode](mpsnnfilternode/gradientfilter(withsources:).md)
- [func gradientFilters(withSource: MPSNNImageNode) -> [MPSNNGradientFilterNode]](mpsnnfilternode/gradientfilters(withsource:).md)
- [func gradientFilters(withSources: [MPSNNImageNode]) -> [MPSNNGradientFilterNode]](mpsnnfilternode/gradientfilters(withsources:).md)
- [func trainingGraph(withSourceGradient: MPSNNImageNode?, nodeHandler: MPSGradientNodeBlock?) -> [MPSNNFilterNode]?](mpsnnfilternode/traininggraph(withsourcegradient:nodehandler:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MPSCNNBatchNormalizationNode](mpscnnbatchnormalizationnode.md)
- [MPSCNNConvolutionNode](mpscnnconvolutionnode.md)
- [MPSCNNDilatedPoolingMaxNode](mpscnndilatedpoolingmaxnode.md)
- [MPSCNNDropoutNode](mpscnndropoutnode.md)
- [MPSCNNGroupNormalizationNode](mpscnngroupnormalizationnode.md)
- [MPSCNNInstanceNormalizationNode](mpscnninstancenormalizationnode.md)
- [MPSCNNLogSoftMaxNode](mpscnnlogsoftmaxnode.md)
- [MPSCNNLossNode](mpscnnlossnode.md)
- [MPSCNNNeuronNode](mpscnnneuronnode.md)
- [MPSCNNNormalizationNode](mpscnnnormalizationnode.md)
- [MPSCNNPoolingNode](mpscnnpoolingnode.md)
- [MPSCNNSoftMaxNode](mpscnnsoftmaxnode.md)
- [MPSCNNUpsamplingBilinearNode](mpscnnupsamplingbilinearnode.md)
- [MPSCNNUpsamplingNearestNode](mpscnnupsamplingnearestnode.md)
- [MPSCNNYOLOLossNode](mpscnnyololossnode.md)
- [MPSNNBinaryArithmeticNode](mpsnnbinaryarithmeticnode.md)
- [MPSNNConcatenationNode](mpsnnconcatenationnode.md)
- [MPSNNForwardLossNode](mpsnnforwardlossnode.md)
- [MPSNNGradientFilterNode](mpsnngradientfilternode.md)
- [MPSNNGramMatrixCalculationNode](mpsnngrammatrixcalculationnode.md)
- [MPSNNInitialGradientNode](mpsnninitialgradientnode.md)
- [MPSNNPadNode](mpsnnpadnode.md)
- [MPSNNReshapeNode](mpsnnreshapenode.md)
- [MPSNNScaleNode](mpsnnscalenode.md)
- [MPSNNUnaryReductionNode](mpsnnunaryreductionnode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSNNGradientFilterNode](mpsnngradientfilternode.md)
  A representation of a gradient filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnfilternode)*