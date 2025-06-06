# MPSCNNDropoutGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

A representation of a gradient dropout filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNDropoutGradientNode : MPSNNGradientFilterNode
```

## Topics

### Initializers
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, gradientState: MPSNNGradientStateNode, keepProbability: Float, seed: Int, maskStrideInPixels: MTLSize)](mpscnndropoutgradientnode/2948001-init.md)
### Instance Properties
- [var keepProbability: Float](mpscnndropoutgradientnode/2947988-keepprobability.md)
- [var maskStrideInPixels: MTLSize](mpscnndropoutgradientnode/2947972-maskstrideinpixels.md)
- [var seed: Int](mpscnndropoutgradientnode/2948003-seed.md)

## Relationships

### Inherits From
- [MPSNNGradientFilterNode](mpsnngradientfilternode.md)

## See Also

- [class MPSCNNDropoutNode](mpscnndropoutnode.md)
  A representation of a dropout filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndropoutgradientnode)*