# MPSNNFilterNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

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
class MPSNNFilterNode : NSObject
```

## Topics

### Instance Properties
- [var label: String?](mpsnnfilternode/2866465-label.md)
- [var paddingPolicy: any MPSNNPadding](mpsnnfilternode/2866496-paddingpolicy.md)
- [protocol MPSNNPadding](mpsnnpadding.md)
  The protocol that provides a description of how kernels should pad images.
- [var resultImage: MPSNNImageNode](mpsnnfilternode/2866492-resultimage.md)
- [var resultState: MPSNNStateNode?](mpsnnfilternode/2866503-resultstate.md)
- [var resultStates: [MPSNNStateNode]?](mpsnnfilternode/2866486-resultstates.md)
- [class MPSNNStateNode](mpsnnstatenode.md)
  A placeholder node denoting the position in the graph of a state object.
- [class MPSNNBinaryGradientStateNode](mpsnnbinarygradientstatenode.md)
  A representation of the state created to record the properties of a binary gradient kernel.
- [class MPSNNGradientStateNode](mpsnngradientstatenode.md)
  A representation of the state created to record the properties of a gradient kernel at the time it was encoded.
### Instance Methods
- [func gradientFilter(withSource: MPSNNImageNode) -> MPSNNGradientFilterNode](mpsnnfilternode/2953941-gradientfilter.md)
- [func gradientFilter(withSources: [MPSNNImageNode]) -> MPSNNGradientFilterNode](mpsnnfilternode/2948052-gradientfilter.md)
- [func gradientFilters(withSource: MPSNNImageNode) -> [MPSNNGradientFilterNode]](mpsnnfilternode/2953944-gradientfilters.md)
- [func gradientFilters(withSources: [MPSNNImageNode]) -> [MPSNNGradientFilterNode]](mpsnnfilternode/2951955-gradientfilters.md)
- [func trainingGraph(withSourceGradient: MPSNNImageNode?, nodeHandler: MPSGradientNodeBlock?) -> [MPSNNFilterNode]?](mpsnnfilternode/3020688-traininggraph.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [class MPSNNGradientFilterNode](mpsnngradientfilternode.md)
  A representation of a gradient filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnfilternode)*