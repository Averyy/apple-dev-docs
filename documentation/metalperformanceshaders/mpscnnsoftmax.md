# MPSCNNSoftMax

**Framework**: Metal Performance Shaders  
**Kind**: cl

A neural transfer function that is useful for classification tasks.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNSoftMax : MPSCNNKernel
```

#### Overview

The softmax filter is applied across feature channels in a convolutional manner at all spatial locations. The softmax filter can be seen as the combination of an activation function (exponential) and a normalization operator.

For each feature channel per pixel in an image in a feature map, the softmax filter computes the following:

![pixel = exp(pixel(x,y,k))/sum(exp(pixel(x,y,0)) ... exp(pixel(x,y,N-1))](https://docs-assets.developer.apple.com/published/866dd98e74/059f1bf5-2d73-46ae-9162-89419ef01e99.png)

Where `R` is the result channel in the pixel and `N` is the number of feature channels.

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)

## See Also

- [class MPSCNNLogSoftMax](mpscnnlogsoftmax.md)
  A neural transfer function that  is useful for constructing a loss function to be minimized when training neural networks.
- [class MPSCNNLogSoftMaxGradient](mpscnnlogsoftmaxgradient.md)
  A gradient logarithmic softmax filter.
- [class MPSCNNSoftMaxGradient](mpscnnsoftmaxgradient.md)
  A gradient softmax filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnsoftmax)*