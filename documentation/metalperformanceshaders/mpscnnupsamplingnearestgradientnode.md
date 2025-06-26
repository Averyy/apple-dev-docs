# MPSCNNUpsamplingNearestGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSCNNUpsamplingNearestGradientNode
```

## Topics

### Initializers
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, gradientState: MPSNNGradientStateNode, scaleFactorX: Double, scaleFactorY: Double)](mpscnnupsamplingnearestgradientnode/init(sourcegradient:sourceimage:gradientstate:scalefactorx:scalefactory:).md)
### Instance Properties
- [var scaleFactorX: Double](mpscnnupsamplingnearestgradientnode/scalefactorx.md)
- [var scaleFactorY: Double](mpscnnupsamplingnearestgradientnode/scalefactory.md)

## Relationships

### Inherits From
- [MPSNNGradientFilterNode](mpsnngradientfilternode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSCNNUpsamplingBilinearNode](mpscnnupsamplingbilinearnode.md)
  A representation of a bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingNearestNode](mpscnnupsamplingnearestnode.md)
  A representation of a nearest spatial upsampling filter.
- [class MPSCNNUpsamplingBilinearGradientNode](mpscnnupsamplingbilineargradientnode.md)
  A representation of a gradient bilinear spatial upsampling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnupsamplingnearestgradientnode)*