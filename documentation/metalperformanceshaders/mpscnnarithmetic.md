# MPSCNNArithmetic

**Framework**: Metal Performance Shaders  
**Kind**: cl

The base class for arithmetic operators.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNArithmetic : MPSCNNBinaryKernel
```

## Topics

### Instance Properties
- [var bias: Float](mpscnnarithmetic/2942499-bias.md)
- [var maximumValue: Float](mpscnnarithmetic/2942498-maximumvalue.md)
- [var minimumValue: Float](mpscnnarithmetic/2942502-minimumvalue.md)
- [var primaryScale: Float](mpscnnarithmetic/2942509-primaryscale.md)
- [var primaryStrideInFeatureChannels: Int](mpscnnarithmetic/2947963-primarystrideinfeaturechannels.md)
- [var secondaryScale: Float](mpscnnarithmetic/2942497-secondaryscale.md)
- [var secondaryStrideInFeatureChannels: Int](mpscnnarithmetic/2947964-secondarystrideinfeaturechannels.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationState: MPSCNNArithmeticGradientState, destinationImage: MPSImage)](mpscnnarithmetic/2954876-encode.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage], destinationStates: [MPSCNNArithmeticGradientState], destinationImages: [MPSImage])](mpscnnarithmetic/2954877-encodebatch.md)

## Relationships

### Inherits From
- [MPSCNNBinaryKernel](mpscnnbinarykernel.md)

## See Also

- [class MPSCNNAdd](mpscnnadd.md)
  An addition operator.
- [class MPSCNNAddGradient](mpscnnaddgradient.md)
  A gradient addition operator.
- [class MPSCNNSubtract](mpscnnsubtract.md)
  A subtraction operator.
- [class MPSCNNSubtractGradient](mpscnnsubtractgradient.md)
  A gradient subtraction operator.
- [class MPSCNNMultiply](mpscnnmultiply.md)
  A multiply operator.
- [class MPSCNNMultiplyGradient](mpscnnmultiplygradient.md)
  A gradient multiply operator.
- [class MPSCNNDivide](mpscnndivide.md)
  A division operator.
- [class MPSCNNArithmeticGradient](mpscnnarithmeticgradient.md)
  The base class for gradient arithmetic operators.
- [class MPSCNNArithmeticGradientState](mpscnnarithmeticgradientstate.md)
  An object that stores the clamp mask used by gradient arithmetic operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnarithmetic)*