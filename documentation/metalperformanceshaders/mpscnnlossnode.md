# MPSCNNLossNode

**Framework**: Metal Performance Shaders  
**Kind**: class

A representation of a loss kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNLossNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, lossDescriptor: MPSCNNLossDescriptor)](mpscnnlossnode/init(source:lossdescriptor:).md)
### Instance Properties
- [var inputLabels: MPSNNLabelsNode](mpscnnlossnode/inputlabels.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSCNNYOLOLossNode](mpscnnyololossnode.md)
  A representation of a YOLO loss kernel.
- [class MPSNNLabelsNode](mpsnnlabelsnode.md)
  A placeholder node denoting the per-element weight buffer used by loss and gradient loss kernels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlossnode)*