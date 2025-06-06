# MPSCNNArithmeticGradient

**Framework**: Metal Performance Shaders  
**Kind**: cl

The base class for gradient arithmetic operators.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNArithmeticGradient : MPSCNNGradientKernel
```

## Topics

### Instance Properties
- [var bias: Float](mpscnnarithmeticgradient/2951855-bias.md)
- [var isSecondarySourceFilter: Bool](mpscnnarithmeticgradient/2951852-issecondarysourcefilter.md)
- [var maximumValue: Float](mpscnnarithmeticgradient/2951854-maximumvalue.md)
- [var minimumValue: Float](mpscnnarithmeticgradient/2951858-minimumvalue.md)
- [var primaryScale: Float](mpscnnarithmeticgradient/2951861-primaryscale.md)
- [var secondaryScale: Float](mpscnnarithmeticgradient/2951856-secondaryscale.md)
- [var secondaryStrideInFeatureChannels: Int](mpscnnarithmeticgradient/2951853-secondarystrideinfeaturechannels.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](mpscnngradientkernel.md)

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
- [class MPSCNNArithmetic](mpscnnarithmetic.md)
  The base class for arithmetic operators.
- [class MPSCNNArithmeticGradientState](mpscnnarithmeticgradientstate.md)
  An object that stores the clamp mask used by gradient arithmetic operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnarithmeticgradient)*