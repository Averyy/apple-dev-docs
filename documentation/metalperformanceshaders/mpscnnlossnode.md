# MPSCNNLossNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

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
class MPSCNNLossNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, lossDescriptor: MPSCNNLossDescriptor)](mpscnnlossnode/2951947-init.md)
### Instance Properties
- [var inputLabels: MPSNNLabelsNode](mpscnnlossnode/2951942-inputlabels.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)

## See Also

- [class MPSCNNYOLOLossNode](mpscnnyololossnode.md)
  A representation of a YOLO loss kernel.
- [class MPSNNLabelsNode](mpsnnlabelsnode.md)
  A placeholder node denoting the per-element weight buffer used by loss and gradient loss kernels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlossnode)*