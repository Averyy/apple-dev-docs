# MPSCNNDropoutGradient

**Framework**: Metal Performance Shaders  
**Kind**: cl

A gradient dropout filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNDropoutGradient : MPSCNNGradientKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnndropoutgradient/2942521-init.md)
- [init(device: any MTLDevice, keepProbability: Float, seed: Int, maskStrideInPixels: MTLSize)](mpscnndropoutgradient/2942518-init.md)
### Instance Properties
- [var keepProbability: Float](mpscnndropoutgradient/2942520-keepprobability.md)
- [var maskStrideInPixels: MTLSize](mpscnndropoutgradient/2942515-maskstrideinpixels.md)
- [var seed: Int](mpscnndropoutgradient/2942528-seed.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](mpscnngradientkernel.md)

## See Also

- [class MPSCNNDropout](mpscnndropout.md)
  A dropout filter.
- [class MPSCNNDropoutGradientState](mpscnndropoutgradientstate.md)
  A class that stores the mask used by dropout and gradient dropout filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndropoutgradient)*