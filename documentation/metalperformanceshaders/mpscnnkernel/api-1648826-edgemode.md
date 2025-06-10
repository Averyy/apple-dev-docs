# edgeMode

**Framework**: Metal Performance Shaders  
**Kind**: instp

The edge mode to use when texture reads stray off the edge of an image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var edgeMode: MPSImageEdgeMode { get set }
```

#### Discussion

Most [`MPSKernel`](mpskernel.md) objects can read off the edge of the source image. This can happen because of a negative offset property, because the  value of `offset + clipRect.size` is larger than the source image or because the filter looks at neighboring pixels, such as a convolution filter. 

The default value is [`MPSImageEdgeMode.zero`](mpsimageedgemode/zero.md). 

> **Note**: For an [`MPSCNNPoolingAverage`](mpscnnpoolingaverage.md) object, specifying a [`MPSImageEdgeMode.clamp`](mpsimageedgemode/clamp.md) edge mode is interpreted as a "shrink-to-edge" operation, which shrinks the effective filtering window to remain within the source image borders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/1648826-edgemode)*