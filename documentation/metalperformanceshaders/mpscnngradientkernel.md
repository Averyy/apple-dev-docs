# MPSCNNGradientKernel

**Framework**: Metal Performance Shaders  
**Kind**: cl

The base class for gradient layers.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNGradientKernel : MPSCNNBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnngradientkernel/2942647-init.md)
- [init(device: any MTLDevice)](mpscnngradientkernel/2942657-init.md)
### Instance Properties
- [var kernelOffsetX: Int](mpscnngradientkernel/2942676-kerneloffsetx.md)
- [var kernelOffsetY: Int](mpscnngradientkernel/2942644-kerneloffsety.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceGradient: MPSImage, sourceImage: MPSImage, gradientState: MPSState) -> MPSImage](mpscnngradientkernel/2942663-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceGradient: MPSImage, sourceImage: MPSImage, gradientState: MPSState, destinationGradient: MPSImage)](mpscnngradientkernel/2942675-encode.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], gradientStates: [MPSState]) -> [MPSImage]](mpscnngradientkernel/2942668-encodebatch.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], gradientStates: [MPSState], destinationGradients: [MPSImage])](mpscnngradientkernel/2942653-encodebatch.md)

## Relationships

### Inherits From
- [MPSCNNBinaryKernel](mpscnnbinarykernel.md)

## See Also

- [class MPSCNNKernel](mpscnnkernel.md)
  Base class for neural network layers.
- [class MPSCNNBinaryKernel](mpscnnbinarykernel.md)
  A convolution neural network kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngradientkernel)*