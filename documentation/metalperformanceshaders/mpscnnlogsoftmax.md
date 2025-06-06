# MPSCNNLogSoftMax

**Framework**: Metal Performance Shaders  
**Kind**: cl

A neural transfer function that  is useful for constructing a loss function to be minimized when training neural networks.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNLogSoftMax : MPSCNNKernel
```

#### Overview

The logarithmic softmax filter is calculated by taking the natural logarithm of the result of a softmax filter.

For each feature channel per pixel in an image in a feature map, the logarithmic softmax filter computes the following:

![pixel = pixel(x,y,k)) - ln{sum(exp(pixel(x,y,0)) ... exp(pixel(x,y,N-1))}](https://docs-assets.developer.apple.com/published/866dd98e74/635d7e69-cec5-4062-bbe6-6085ad72b501.png)

Where `R` is the result channel in the pixel, `N` is the number of feature channels, and `y=ln(x)` satisfies `e``ʸ``=x`.

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)

## See Also

- [class MPSCNNSoftMax](mpscnnsoftmax.md)
  A neural transfer function that is useful for classification tasks.
- [class MPSCNNLogSoftMaxGradient](mpscnnlogsoftmaxgradient.md)
  A gradient logarithmic softmax filter.
- [class MPSCNNSoftMaxGradient](mpscnnsoftmaxgradient.md)
  A gradient softmax filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlogsoftmax)*