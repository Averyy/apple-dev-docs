# MPSCNNUpsamplingNearestNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

A representation of a nearest spatial upsampling filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNUpsamplingNearestNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, integerScaleFactorX: Int, integerScaleFactorY: Int)](mpscnnupsamplingnearestnode/2875222-init.md)
### Instance Properties
- [var scaleFactorX: Double](mpscnnupsamplingnearestnode/2875209-scalefactorx.md)
- [var scaleFactorY: Double](mpscnnupsamplingnearestnode/2875155-scalefactory.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)

## See Also

- [class MPSCNNUpsamplingBilinearNode](mpscnnupsamplingbilinearnode.md)
  A representation of a bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingBilinearGradientNode](mpscnnupsamplingbilineargradientnode.md)
  A representation of a gradient bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingNearestGradientNode](mpscnnupsamplingnearestgradientnode.md)
  A representation of a gradient nearest spatial upsampling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnupsamplingnearestnode)*