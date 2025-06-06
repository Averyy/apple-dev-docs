# MPSCNNUpsamplingNearestGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

A representation of a gradient nearest spatial upsampling filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNUpsamplingNearestGradientNode : MPSNNGradientFilterNode
```

## Topics

### Initializers
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, gradientState: MPSNNGradientStateNode, scaleFactorX: Double, scaleFactorY: Double)](mpscnnupsamplingnearestgradientnode/2947983-init.md)
### Instance Properties
- [var scaleFactorX: Double](mpscnnupsamplingnearestgradientnode/2948024-scalefactorx.md)
- [var scaleFactorY: Double](mpscnnupsamplingnearestgradientnode/2948035-scalefactory.md)

## Relationships

### Inherits From
- [MPSNNGradientFilterNode](mpsnngradientfilternode.md)

## See Also

- [class MPSCNNUpsamplingBilinearNode](mpscnnupsamplingbilinearnode.md)
  A representation of a bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingNearestNode](mpscnnupsamplingnearestnode.md)
  A representation of a nearest spatial upsampling filter.
- [class MPSCNNUpsamplingBilinearGradientNode](mpscnnupsamplingbilineargradientnode.md)
  A representation of a gradient bilinear spatial upsampling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnupsamplingnearestgradientnode)*