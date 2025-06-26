# MPSCNNDropoutGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSCNNDropoutGradientNode
```

## Topics

### Initializers
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, gradientState: MPSNNGradientStateNode, keepProbability: Float, seed: Int, maskStrideInPixels: MTLSize)](mpscnndropoutgradientnode/init(sourcegradient:sourceimage:gradientstate:keepprobability:seed:maskstrideinpixels:).md)
### Instance Properties
- [var keepProbability: Float](mpscnndropoutgradientnode/keepprobability.md)
- [var maskStrideInPixels: MTLSize](mpscnndropoutgradientnode/maskstrideinpixels.md)
- [var seed: Int](mpscnndropoutgradientnode/seed.md)

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

## See Also

- [class MPSCNNDropoutNode](mpscnndropoutnode.md)
  A representation of a dropout filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndropoutgradientnode)*