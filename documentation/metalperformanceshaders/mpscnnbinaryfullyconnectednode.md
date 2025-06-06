# MPSCNNBinaryFullyConnectedNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

A representation of a fully connected convolution layer with binary weights and optionally binarized input image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNBinaryFullyConnectedNode : MPSCNNBinaryConvolutionNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, weights: any MPSCNNConvolutionDataSource, scaleValue: Float, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](mpscnnbinaryfullyconnectednode/2866443-init.md)
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [init(source: MPSNNImageNode, weights: any MPSCNNConvolutionDataSource, outputBiasTerms: UnsafePointer<Float>?, outputScaleTerms: UnsafePointer<Float>?, inputBiasTerms: UnsafePointer<Float>?, inputScaleTerms: UnsafePointer<Float>?, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](mpscnnbinaryfullyconnectednode/2942637-init.md)

## Relationships

### Inherits From
- [MPSCNNBinaryConvolutionNode](mpscnnbinaryconvolutionnode.md)

## See Also

- [class MPSCNNFullyConnectedNode](mpscnnfullyconnectednode.md)
  A representation of a fully connected convolution layer, also known as an inner product layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinaryfullyconnectednode)*