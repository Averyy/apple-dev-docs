# MPSCNNPoolingL2Norm

**Framework**: Metal Performance Shaders  
**Kind**: cl

An L2-norm pooling filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNPoolingL2Norm : MPSCNNPooling
```

#### Overview

For each pixel, returns L2-Norm of pixels in the `kernelWidth * kernelHeight` filter region:

![out[c,x,y] = sqrt ( sum_{dx,dy} in[c,x+dx,y+dy] * in[c,x+dx,y+dy] )](https://docs-assets.developer.apple.com/published/866dd98e74/54e12ca6-60ea-486a-ae23-be6b2a527ccc.png)

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnpoolingl2norm/2867141-init.md)
  Initializes an L2-norm pooling filter.
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int)](mpscnnpoolingl2norm/2875162-init.md)
  Initializes an L2-norm pooling filter.

## Relationships

### Inherits From
- [MPSCNNPooling](mpscnnpooling.md)

## See Also

- [class MPSCNNPoolingAverage](mpscnnpoolingaverage.md)
  An average pooling filter.
- [class MPSCNNPoolingAverageGradient](mpscnnpoolingaveragegradient.md)
  A gradient average pooling filter.
- [class MPSCNNPoolingMax](mpscnnpoolingmax.md)
  A max pooling filter.
- [class MPSCNNDilatedPoolingMax](mpscnndilatedpoolingmax.md)
  A dilated max pooling filter.
- [class MPSCNNPooling](mpscnnpooling.md)
  A pooling kernel.
- [class MPSCNNPoolingGradient](mpscnnpoolinggradient.md)
  A gradient pooling kernel.
- [class MPSCNNDilatedPoolingMaxGradient](mpscnndilatedpoolingmaxgradient.md)
  A gradient dilated max pooling filter.
- [class MPSCNNPoolingL2NormGradient](mpscnnpoolingl2normgradient.md)
  A gradient L2-norm pooling filter.
- [class MPSCNNPoolingMaxGradient](mpscnnpoolingmaxgradient.md)
  A gradient max pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpoolingl2norm)*