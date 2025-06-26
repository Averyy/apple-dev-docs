# MPSCNNSoftMaxGradient

**Framework**: Metal Performance Shaders  
**Kind**: class

A gradient softmax filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNSoftMaxGradient
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnsoftmaxgradient/init(coder:device:).md)
- [init(device: any MTLDevice)](mpscnnsoftmaxgradient/init(device:).md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](mpscnngradientkernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSCNNSoftMax](mpscnnsoftmax.md)
  A neural transfer function that is useful for classification tasks.
- [class MPSCNNLogSoftMax](mpscnnlogsoftmax.md)
  A neural transfer function that  is useful for constructing a loss function to be minimized when training neural networks.
- [class MPSCNNLogSoftMaxGradient](mpscnnlogsoftmaxgradient.md)
  A gradient logarithmic softmax filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnsoftmaxgradient)*