# MPSCNNDropout

**Framework**: Metal Performance Shaders  
**Kind**: cl

A dropout filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNDropout : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnndropout/2942514-init.md)
- [init(device: any MTLDevice, keepProbability: Float, seed: Int, maskStrideInPixels: MTLSize)](mpscnndropout/2942522-init.md)
### Instance Properties
- [var keepProbability: Float](mpscnndropout/2942524-keepprobability.md)
- [var maskStrideInPixels: MTLSize](mpscnndropout/2942519-maskstrideinpixels.md)
- [var seed: Int](mpscnndropout/2942517-seed.md)
### Instance Methods
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNDropoutGradientState?](mpscnndropout/3131793-resultstate.md)
- [func resultStateBatch(sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> MPSCNNDropoutGradientState?](mpscnndropout/3131792-resultstatebatch.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNDropoutGradientState?](mpscnndropout/3131795-temporaryresultstate.md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSCNNDropoutGradientState]?](mpscnndropout/3131794-temporaryresultstatebatch.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)

## See Also

- [class MPSCNNDropoutGradient](mpscnndropoutgradient.md)
  A gradient dropout filter.
- [class MPSCNNDropoutGradientState](mpscnndropoutgradientstate.md)
  A class that stores the mask used by dropout and gradient dropout filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndropout)*