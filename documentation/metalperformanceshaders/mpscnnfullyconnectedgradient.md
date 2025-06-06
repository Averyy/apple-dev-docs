# MPSCNNFullyConnectedGradient

**Framework**: Metal Performance Shaders  
**Kind**: cl

A gradient fully connected convolution layer.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNFullyConnectedGradient : MPSCNNConvolutionGradient
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnfullyconnectedgradient/2951923-init.md)
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnfullyconnectedgradient/2951921-init.md)

## Relationships

### Inherits From
- [MPSCNNConvolutionGradient](mpscnnconvolutiongradient.md)

## See Also

- [class MPSCNNBinaryFullyConnected](mpscnnbinaryfullyconnected.md)
  A fully connected convolution layer with binary weights and optionally binarized input image.
- [class MPSCNNFullyConnected](mpscnnfullyconnected.md)
  A fully connected convolution layer, also known as an inner product layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnfullyconnectedgradient)*