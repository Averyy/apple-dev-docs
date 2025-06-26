# MPSCNNArithmeticGradient

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSCNNArithmeticGradient
```

## Topics

### Instance Properties
- [var bias: Float](mpscnnarithmeticgradient/bias.md)
- [var isSecondarySourceFilter: Bool](mpscnnarithmeticgradient/issecondarysourcefilter.md)
- [var maximumValue: Float](mpscnnarithmeticgradient/maximumvalue.md)
- [var minimumValue: Float](mpscnnarithmeticgradient/minimumvalue.md)
- [var primaryScale: Float](mpscnnarithmeticgradient/primaryscale.md)
- [var secondaryScale: Float](mpscnnarithmeticgradient/secondaryscale.md)
- [var secondaryStrideInFeatureChannels: Int](mpscnnarithmeticgradient/secondarystrideinfeaturechannels.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](mpscnngradientkernel.md)
### Inherited By
- [MPSCNNAddGradient](mpscnnaddgradient.md)
- [MPSCNNMultiplyGradient](mpscnnmultiplygradient.md)
- [MPSCNNSubtractGradient](mpscnnsubtractgradient.md)
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
- [class MPSCNNArithmetic](mpscnnarithmetic.md)
  The base class for arithmetic operators.
- [class MPSCNNArithmeticGradientState](mpscnnarithmeticgradientstate.md)
  An object that stores the clamp mask used by gradient arithmetic operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnarithmeticgradient)*