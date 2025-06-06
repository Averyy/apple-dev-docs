# MPSCNNPoolingGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

A representation of a gradient pooling kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNPoolingGradientNode : MPSNNGradientFilterNode
```

## Topics

### Initializers
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, gradientState: MPSNNGradientStateNode, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int, paddingPolicy: (any MPSNNPadding)?)](mpscnnpoolinggradientnode/2948011-init.md)
### Instance Properties
- [var kernelHeight: Int](mpscnnpoolinggradientnode/2947992-kernelheight.md)
- [var kernelWidth: Int](mpscnnpoolinggradientnode/2948034-kernelwidth.md)
- [var strideInPixelsX: Int](mpscnnpoolinggradientnode/2948018-strideinpixelsx.md)
- [var strideInPixelsY: Int](mpscnnpoolinggradientnode/2948048-strideinpixelsy.md)

## Relationships

### Inherits From
- [MPSNNGradientFilterNode](mpsnngradientfilternode.md)

## See Also

- [class MPSCNNPoolingAverageNode](mpscnnpoolingaveragenode.md)
  A representation of an average pooling filter.
- [class MPSCNNDilatedPoolingMaxNode](mpscnndilatedpoolingmaxnode.md)
  A representation of a dilated max pooling filter.
- [class MPSCNNPoolingL2NormNode](mpscnnpoolingl2normnode.md)
  A representation of a L2-norm pooling filter.
- [class MPSCNNPoolingMaxNode](mpscnnpoolingmaxnode.md)
  A representation of a max pooling filter.
- [class MPSCNNPoolingNode](mpscnnpoolingnode.md)
  A representation of a MPS CNN pooling kernel.
- [class MPSCNNDilatedPoolingMaxGradientNode](mpscnndilatedpoolingmaxgradientnode.md)
  A representation of a gradient dilated max pooling filter.
- [class MPSCNNPoolingAverageGradientNode](mpscnnpoolingaveragegradientnode.md)
  A representation of a gradient average pooling filter.
- [class MPSCNNPoolingL2NormGradientNode](mpscnnpoolingl2normgradientnode.md)
  A representation of a gradient L2-norm pooling filter.
- [class MPSCNNPoolingMaxGradientNode](mpscnnpoolingmaxgradientnode.md)
  A representation of a gradient max pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpoolinggradientnode)*