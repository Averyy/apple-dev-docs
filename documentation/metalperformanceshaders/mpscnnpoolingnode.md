# MPSCNNPoolingNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

A representation of a MPS CNN pooling kernel.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNPoolingNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, filterSize: Int)](mpscnnpoolingnode/2866488-init.md)
- [init(source: MPSNNImageNode, filterSize: Int, stride: Int)](mpscnnpoolingnode/2866444-init.md)
- [init(source: MPSNNImageNode, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int)](mpscnnpoolingnode/2866471-init.md)
### Instance Properties
- [var kernelHeight: Int](mpscnnpoolingnode/2993001-kernelheight.md)
- [var kernelWidth: Int](mpscnnpoolingnode/2993002-kernelwidth.md)
- [var strideInPixelsX: Int](mpscnnpoolingnode/2993003-strideinpixelsx.md)
- [var strideInPixelsY: Int](mpscnnpoolingnode/2993004-strideinpixelsy.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)

## See Also

- [class MPSCNNPoolingAverageNode](mpscnnpoolingaveragenode.md)
  A representation of an average pooling filter.
- [class MPSCNNDilatedPoolingMaxNode](mpscnndilatedpoolingmaxnode.md)
  A representation of a dilated max pooling filter.
- [class MPSCNNPoolingL2NormNode](mpscnnpoolingl2normnode.md)
  A representation of a L2-norm pooling filter.
- [class MPSCNNPoolingMaxNode](mpscnnpoolingmaxnode.md)
  A representation of a max pooling filter.
- [class MPSCNNDilatedPoolingMaxGradientNode](mpscnndilatedpoolingmaxgradientnode.md)
  A representation of a gradient dilated max pooling filter.
- [class MPSCNNPoolingAverageGradientNode](mpscnnpoolingaveragegradientnode.md)
  A representation of a gradient average pooling filter.
- [class MPSCNNPoolingGradientNode](mpscnnpoolinggradientnode.md)
  A representation of a gradient pooling kernel.
- [class MPSCNNPoolingL2NormGradientNode](mpscnnpoolingl2normgradientnode.md)
  A representation of a gradient L2-norm pooling filter.
- [class MPSCNNPoolingMaxGradientNode](mpscnnpoolingmaxgradientnode.md)
  A representation of a gradient max pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpoolingnode)*