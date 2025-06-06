# MPSCNNDilatedPoolingMaxNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

A representation of a dilated max pooling filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNDilatedPoolingMaxNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, filterSize: Int)](mpscnndilatedpoolingmaxnode/2873240-init.md)
- [init(source: MPSNNImageNode, filterSize: Int, stride: Int, dilationRate: Int)](mpscnndilatedpoolingmaxnode/2887340-init.md)
- [init(source: MPSNNImageNode, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int, dilationRateX: Int, dilationRateY: Int)](mpscnndilatedpoolingmaxnode/2887339-init.md)
### Instance Properties
- [var dilationRateX: Int](mpscnndilatedpoolingmaxnode/2887341-dilationratex.md)
- [var dilationRateY: Int](mpscnndilatedpoolingmaxnode/2887342-dilationratey.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)

## See Also

- [class MPSCNNPoolingAverageNode](mpscnnpoolingaveragenode.md)
  A representation of an average pooling filter.
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
- [class MPSCNNPoolingGradientNode](mpscnnpoolinggradientnode.md)
  A representation of a gradient pooling kernel.
- [class MPSCNNPoolingL2NormGradientNode](mpscnnpoolingl2normgradientnode.md)
  A representation of a gradient L2-norm pooling filter.
- [class MPSCNNPoolingMaxGradientNode](mpscnnpoolingmaxgradientnode.md)
  A representation of a gradient max pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndilatedpoolingmaxnode)*