# MPSNNBinaryGradientStateNode

**Framework**: Metal Performance Shaders  
**Kind**: class

A representation of the state created to record the properties of a binary gradient kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSNNBinaryGradientStateNode
```

## Relationships

### Inherits From
- [MPSNNStateNode](mpsnnstatenode.md)
### Inherited By
- [MPSNNArithmeticGradientStateNode](mpsnnarithmeticgradientstatenode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var label: String?](mpsnnfilternode/label.md)
- [var paddingPolicy: any MPSNNPadding](mpsnnfilternode/paddingpolicy.md)
- [protocol MPSNNPadding](mpsnnpadding.md)
  The protocol that provides a description of how kernels should pad images.
- [var resultImage: MPSNNImageNode](mpsnnfilternode/resultimage.md)
- [var resultState: MPSNNStateNode?](mpsnnfilternode/resultstate.md)
- [var resultStates: [MPSNNStateNode]?](mpsnnfilternode/resultstates.md)
- [class MPSNNStateNode](mpsnnstatenode.md)
  A placeholder node denoting the position in the graph of a state object.
- [class MPSNNGradientStateNode](mpsnngradientstatenode.md)
  A representation of the state created to record the properties of a gradient kernel at the time it was encoded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnbinarygradientstatenode)*