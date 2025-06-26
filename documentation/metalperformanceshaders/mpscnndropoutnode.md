# MPSCNNDropoutNode

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSCNNDropoutNode
```

## Topics

### Initializers
- [convenience init(source: MPSNNImageNode)](mpscnndropoutnode/init(source:).md)
- [convenience init(source: MPSNNImageNode, keepProbability: Float)](mpscnndropoutnode/init(source:keepprobability:).md)
- [init(source: MPSNNImageNode, keepProbability: Float, seed: Int, maskStrideInPixels: MTLSize)](mpscnndropoutnode/init(source:keepprobability:seed:maskstrideinpixels:).md)
### Instance Properties
- [var keepProbability: Float](mpscnndropoutnode/keepprobability.md)
- [var maskStrideInPixels: MTLSize](mpscnndropoutnode/maskstrideinpixels.md)
- [var seed: Int](mpscnndropoutnode/seed.md)

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

- [class MPSCNNDropoutGradientNode](mpscnndropoutgradientnode.md)
  A representation of a gradient dropout filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndropoutnode)*