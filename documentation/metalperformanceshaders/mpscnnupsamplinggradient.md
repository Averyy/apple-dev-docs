# MPSCNNUpsamplingGradient

**Framework**: Metal Performance Shaders  
**Kind**: class

A gradient filter that upsamples an existing Metal Performance Shaders image.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNUpsamplingGradient
```

## Topics

### Instance Properties
- [var scaleFactorX: Double](mpscnnupsamplinggradient/scalefactorx.md)
- [var scaleFactorY: Double](mpscnnupsamplinggradient/scalefactory.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](mpscnngradientkernel.md)
### Inherited By
- [MPSCNNUpsamplingBilinearGradient](mpscnnupsamplingbilineargradient.md)
- [MPSCNNUpsamplingNearestGradient](mpscnnupsamplingnearestgradient.md)
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

- [class MPSCNNUpsampling](mpscnnupsampling.md)
  A filter that resamples an existing MPS image.
- [class MPSCNNUpsamplingBilinear](mpscnnupsamplingbilinear.md)
  A bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingNearest](mpscnnupsamplingnearest.md)
  A nearest spatial upsampling filter.
- [class MPSCNNUpsamplingBilinearGradient](mpscnnupsamplingbilineargradient.md)
  A gradient bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingNearestGradient](mpscnnupsamplingnearestgradient.md)
  A gradient upsampling filter that samples the pixel nearest to the source when upsampling to the destination pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnupsamplinggradient)*