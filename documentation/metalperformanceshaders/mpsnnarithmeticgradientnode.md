# MPSNNArithmeticGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

A representation of the base class for gradient arithmetic operators.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSNNArithmeticGradientNode : MPSNNGradientFilterNode
```

## Topics

### Initializers
- [init(gradientImages: [MPSNNImageNode], forwardFilter: MPSNNFilterNode, isSecondarySourceFilter: Bool)](mpsnnarithmeticgradientnode/2952980-init.md)
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, gradientState: MPSNNBinaryGradientStateNode, isSecondarySourceFilter: Bool)](mpsnnarithmeticgradientnode/2956166-init.md)
### Instance Properties
- [var bias: Float](mpsnnarithmeticgradientnode/2952988-bias.md)
- [var isSecondarySourceFilter: Bool](mpsnnarithmeticgradientnode/2952987-issecondarysourcefilter.md)
- [var maximumValue: Float](mpsnnarithmeticgradientnode/2952986-maximumvalue.md)
- [var minimumValue: Float](mpsnnarithmeticgradientnode/2952989-minimumvalue.md)
- [var primaryScale: Float](mpsnnarithmeticgradientnode/2952993-primaryscale.md)
- [var secondaryScale: Float](mpsnnarithmeticgradientnode/2952981-secondaryscale.md)
- [var secondaryStrideInFeatureChannels: Int](mpsnnarithmeticgradientnode/2952984-secondarystrideinfeaturechannels.md)
- [var secondaryStrideInPixelsX: Int](mpsnnarithmeticgradientnode/2952968-secondarystrideinpixelsx.md)
- [var secondaryStrideInPixelsY: Int](mpsnnarithmeticgradientnode/2952994-secondarystrideinpixelsy.md)

## Relationships

### Inherits From
- [MPSNNGradientFilterNode](mpsnngradientfilternode.md)

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
- [class MPSNNBinaryArithmeticNode](mpsnnbinaryarithmeticnode.md)
  Virtual base class for basic arithmetic nodes.
- [class MPSNNArithmeticGradientStateNode](mpsnnarithmeticgradientstatenode.md)
  A representation of the clamp mask used by gradient arithmetic operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnarithmeticgradientnode)*