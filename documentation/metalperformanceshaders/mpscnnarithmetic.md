# MPSCNNArithmetic

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSCNNArithmetic
```

## Topics

### Instance Properties
- [var bias: Float](mpscnnarithmetic/bias.md)
- [var maximumValue: Float](mpscnnarithmetic/maximumvalue.md)
- [var minimumValue: Float](mpscnnarithmetic/minimumvalue.md)
- [var primaryScale: Float](mpscnnarithmetic/primaryscale.md)
- [var primaryStrideInFeatureChannels: Int](mpscnnarithmetic/primarystrideinfeaturechannels.md)
- [var secondaryScale: Float](mpscnnarithmetic/secondaryscale.md)
- [var secondaryStrideInFeatureChannels: Int](mpscnnarithmetic/secondarystrideinfeaturechannels.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationState: MPSCNNArithmeticGradientState, destinationImage: MPSImage)](mpscnnarithmetic/encode(commandbuffer:primaryimage:secondaryimage:destinationstate:destinationimage:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage], destinationStates: [MPSCNNArithmeticGradientState], destinationImages: [MPSImage])](mpscnnarithmetic/encodebatch(commandbuffer:primaryimages:secondaryimages:destinationstates:destinationimages:).md)

## Relationships

### Inherits From
- [MPSCNNBinaryKernel](mpscnnbinarykernel.md)
### Inherited By
- [MPSCNNAdd](mpscnnadd.md)
- [MPSCNNDivide](mpscnndivide.md)
- [MPSCNNMultiply](mpscnnmultiply.md)
- [MPSCNNSubtract](mpscnnsubtract.md)
- [MPSNNCompare](mpsnncompare.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

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