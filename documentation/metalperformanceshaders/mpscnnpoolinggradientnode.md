# MPSCNNPoolingGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSCNNPoolingGradientNode
```

## Topics

### Initializers
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, gradientState: MPSNNGradientStateNode, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int, paddingPolicy: (any MPSNNPadding)?)](mpscnnpoolinggradientnode/init(sourcegradient:sourceimage:gradientstate:kernelwidth:kernelheight:strideinpixelsx:strideinpixelsy:paddingpolicy:).md)
### Instance Properties
- [var kernelHeight: Int](mpscnnpoolinggradientnode/kernelheight.md)
- [var kernelWidth: Int](mpscnnpoolinggradientnode/kernelwidth.md)
- [var strideInPixelsX: Int](mpscnnpoolinggradientnode/strideinpixelsx.md)
- [var strideInPixelsY: Int](mpscnnpoolinggradientnode/strideinpixelsy.md)

## Relationships

### Inherits From
- [MPSNNGradientFilterNode](mpsnngradientfilternode.md)
### Inherited By
- [MPSCNNDilatedPoolingMaxGradientNode](mpscnndilatedpoolingmaxgradientnode.md)
- [MPSCNNPoolingAverageGradientNode](mpscnnpoolingaveragegradientnode.md)
- [MPSCNNPoolingL2NormGradientNode](mpscnnpoolingl2normgradientnode.md)
- [MPSCNNPoolingMaxGradientNode](mpscnnpoolingmaxgradientnode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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