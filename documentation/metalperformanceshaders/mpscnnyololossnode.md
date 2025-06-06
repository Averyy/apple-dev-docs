# MPSCNNYOLOLossNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

A representation of a YOLO loss kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNYOLOLossNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, lossDescriptor: MPSCNNYOLOLossDescriptor)](mpscnnyololossnode/2976514-init.md)
### Instance Properties
- [var inputLabels: MPSNNLabelsNode](mpscnnyololossnode/2976515-inputlabels.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)

## See Also

- [class MPSCNNLossNode](mpscnnlossnode.md)
  A representation of a loss kernel.
- [class MPSNNLabelsNode](mpsnnlabelsnode.md)
  A placeholder node denoting the per-element weight buffer used by loss and gradient loss kernels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnyololossnode)*