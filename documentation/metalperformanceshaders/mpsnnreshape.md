# MPSNNReshape

**Framework**: Metal Performance Shaders  
**Kind**: cl

The base class for reshape operations.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSNNReshape : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsnnreshape/2951930-init.md)
- [init(device: any MTLDevice)](mpsnnreshape/2951929-init.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool, reshapedWidth: Int, reshapedHeight: Int, reshapedFeatureChannels: Int) -> MPSImage](mpsnnreshape/3547991-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, reshapedWidth: Int, reshapedHeight: Int, reshapedFeatureChannels: Int) -> MPSImage](mpsnnreshape/3547992-encode.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool, reshapedWidth: Int, reshapedHeight: Int, reshapedFeatureChannels: Int) -> [MPSImage]](mpsnnreshape/3547989-encodebatch.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], reshapedWidth: Int, reshapedHeight: Int, reshapedFeatureChannels: Int) -> [MPSImage]](mpsnnreshape/3547990-encodebatch.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreshape)*