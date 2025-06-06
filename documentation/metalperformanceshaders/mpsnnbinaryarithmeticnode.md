# MPSNNBinaryArithmeticNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

Virtual base class for basic arithmetic nodes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNBinaryArithmeticNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(leftSource: MPSNNImageNode, rightSource: MPSNNImageNode)](mpsnnbinaryarithmeticnode/2890825-init.md)
- [init(sources: [MPSNNImageNode])](mpsnnbinaryarithmeticnode/2890820-init.md)
### Instance Properties
- [var bias: Float](mpsnnbinaryarithmeticnode/2952964-bias.md)
- [var maximumValue: Float](mpsnnbinaryarithmeticnode/2952979-maximumvalue.md)
- [var minimumValue: Float](mpsnnbinaryarithmeticnode/2952970-minimumvalue.md)
- [var primaryScale: Float](mpsnnbinaryarithmeticnode/2952966-primaryscale.md)
- [var primaryStrideInFeatureChannels: Int](mpsnnbinaryarithmeticnode/2952983-primarystrideinfeaturechannels.md)
- [var primaryStrideInPixelsX: Int](mpsnnbinaryarithmeticnode/2952973-primarystrideinpixelsx.md)
- [var primaryStrideInPixelsY: Int](mpsnnbinaryarithmeticnode/2952996-primarystrideinpixelsy.md)
- [var secondaryScale: Float](mpsnnbinaryarithmeticnode/2952976-secondaryscale.md)
- [var secondaryStrideInFeatureChannels: Int](mpsnnbinaryarithmeticnode/2952974-secondarystrideinfeaturechannels.md)
- [var secondaryStrideInPixelsX: Int](mpsnnbinaryarithmeticnode/2952972-secondarystrideinpixelsx.md)
- [var secondaryStrideInPixelsY: Int](mpsnnbinaryarithmeticnode/2952985-secondarystrideinpixelsy.md)
### Instance Methods
- [func gradientClass() -> AnyClass](mpsnnbinaryarithmeticnode/2952978-gradientclass.md)
- [func gradientFilters(withSources: [MPSNNImageNode]) -> [MPSNNGradientFilterNode]](mpsnnbinaryarithmeticnode/2952967-gradientfilters.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)

## See Also

- [class MPSNNAdditionNode](mpsnnadditionnode.md)
  A representation of an addition operator.
- [class MPSNNAdditionGradientNode](mpsnnadditiongradientnode.md)
  A representation of a gradient addition operator.
- [class MPSNNSubtractionNode](mpsnnsubtractionnode.md)
  A representation of an subtraction operator.
- [class MPSNNSubtractionGradientNode](mpsnnsubtractiongradientnode.md)
  A representation of a gradient subtraction operator.
- [class MPSNNMultiplicationNode](mpsnnmultiplicationnode.md)
  A representation of a multiplication operator.
- [class MPSNNMultiplicationGradientNode](mpsnnmultiplicationgradientnode.md)
  A representation of a gradient multiplication operator.
- [class MPSNNDivisionNode](mpsnndivisionnode.md)
  A representation of a division operator.
- [class MPSNNArithmeticGradientNode](mpsnnarithmeticgradientnode.md)
  A representation of the base class for gradient arithmetic operators.
- [class MPSNNArithmeticGradientStateNode](mpsnnarithmeticgradientstatenode.md)
  A representation of the clamp mask used by gradient arithmetic operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnbinaryarithmeticnode)*