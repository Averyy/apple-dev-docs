# MPSCNNDropoutNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

A representation of a dropout filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNDropoutNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode)](mpscnndropoutnode/2947969-init.md)
- [init(source: MPSNNImageNode, keepProbability: Float)](mpscnndropoutnode/2948000-init.md)
- [init(source: MPSNNImageNode, keepProbability: Float, seed: Int, maskStrideInPixels: MTLSize)](mpscnndropoutnode/2947990-init.md)
### Instance Properties
- [var keepProbability: Float](mpscnndropoutnode/2947982-keepprobability.md)
- [var maskStrideInPixels: MTLSize](mpscnndropoutnode/2947998-maskstrideinpixels.md)
- [var seed: Int](mpscnndropoutnode/2948030-seed.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)

## See Also

- [class MPSCNNDropoutGradientNode](mpscnndropoutgradientnode.md)
  A representation of a gradient dropout filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndropoutnode)*