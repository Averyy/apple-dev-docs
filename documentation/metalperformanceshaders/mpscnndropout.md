# MPSCNNDropout

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSCNNDropout
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnndropout/init(coder:device:).md)
- [init(device: any MTLDevice, keepProbability: Float, seed: Int, maskStrideInPixels: MTLSize)](mpscnndropout/init(device:keepprobability:seed:maskstrideinpixels:).md)
### Instance Properties
- [var keepProbability: Float](mpscnndropout/keepprobability.md)
- [var maskStrideInPixels: MTLSize](mpscnndropout/maskstrideinpixels.md)
- [var seed: Int](mpscnndropout/seed.md)
### Instance Methods
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNDropoutGradientState?](mpscnndropout/resultstate(sourceimage:sourcestates:destinationimage:).md)
- [func resultStateBatch(sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> MPSCNNDropoutGradientState?](mpscnndropout/resultstatebatch(sourceimage:sourcestates:destinationimage:).md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSCNNDropoutGradientState?](mpscnndropout/temporaryresultstate(commandbuffer:sourceimage:sourcestates:destinationimage:).md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSCNNDropoutGradientState]?](mpscnndropout/temporaryresultstatebatch(commandbuffer:sourceimage:sourcestates:destinationimage:).md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)
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

- [class MPSCNNDropoutGradient](mpscnndropoutgradient.md)
  A gradient dropout filter.
- [class MPSCNNDropoutGradientState](mpscnndropoutgradientstate.md)
  A class that stores the mask used by dropout and gradient dropout filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndropout)*