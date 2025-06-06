# MPSCNNLogSoftMaxGradient

**Framework**: Metal Performance Shaders  
**Kind**: cl

A gradient logarithmic softmax filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNLogSoftMaxGradient : MPSCNNGradientKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnlogsoftmaxgradient/2942619-init.md)
- [init(device: any MTLDevice)](mpscnnlogsoftmaxgradient/2942622-init.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](mpscnngradientkernel.md)

## See Also

- [class MPSCNNSoftMax](mpscnnsoftmax.md)
  A neural transfer function that is useful for classification tasks.
- [class MPSCNNLogSoftMax](mpscnnlogsoftmax.md)
  A neural transfer function that  is useful for constructing a loss function to be minimized when training neural networks.
- [class MPSCNNSoftMaxGradient](mpscnnsoftmaxgradient.md)
  A gradient softmax filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlogsoftmaxgradient)*