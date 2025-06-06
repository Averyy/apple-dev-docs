# MPSCNNUpsamplingBilinearNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

A representation of a bilinear spatial upsampling filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNUpsamplingBilinearNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, integerScaleFactorX: Int, integerScaleFactorY: Int)](mpscnnupsamplingbilinearnode/2875152-init.md)
- [init(source: MPSNNImageNode, integerScaleFactorX: Int, integerScaleFactorY: Int, alignCorners: Bool)](mpscnnupsamplingbilinearnode/2966688-init.md)
### Instance Properties
- [var scaleFactorX: Double](mpscnnupsamplingbilinearnode/2875153-scalefactorx.md)
- [var scaleFactorY: Double](mpscnnupsamplingbilinearnode/2875150-scalefactory.md)
- [var alignCorners: Bool](mpscnnupsamplingbilinearnode/2966687-aligncorners.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)

## See Also

- [class MPSCNNUpsamplingNearestNode](mpscnnupsamplingnearestnode.md)
  A representation of a nearest spatial upsampling filter.
- [class MPSCNNUpsamplingBilinearGradientNode](mpscnnupsamplingbilineargradientnode.md)
  A representation of a gradient bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingNearestGradientNode](mpscnnupsamplingnearestgradientnode.md)
  A representation of a gradient nearest spatial upsampling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnupsamplingbilinearnode)*