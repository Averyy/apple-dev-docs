# MPSNNForwardLoss

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNForwardLoss
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsnnforwardloss/init(coder:device:).md)
- [init(device: any MTLDevice, lossDescriptor: MPSCNNLossDescriptor)](mpsnnforwardloss/init(device:lossdescriptor:).md)
### Instance Properties
- [var delta: Float](mpsnnforwardloss/delta.md)
- [var epsilon: Float](mpsnnforwardloss/epsilon.md)
- [var labelSmoothing: Float](mpsnnforwardloss/labelsmoothing.md)
- [var lossType: MPSCNNLossType](mpsnnforwardloss/losstype.md)
- [var numberOfClasses: Int](mpsnnforwardloss/numberofclasses.md)
- [var reduceAcrossBatch: Bool](mpsnnforwardloss/reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](mpsnnforwardloss/reductiontype.md)
- [var weight: Float](mpsnnforwardloss/weight.md)
### Instance Methods
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSImage], weights: [MPSImage]?, destinationStates: [MPSState]?, destinationImages: [MPSImage])](mpsnnforwardloss/encodebatch(commandbuffer:sourceimages:labels:weights:destinationstates:destinationimages:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSImage], weights: [MPSImage]?, outStates: AutoreleasingUnsafeMutablePointer<NSArray?>?, isTemporary: Bool) -> [MPSImage]](mpsnnforwardloss/encodebatch(commandbuffer:sourceimages:labels:weights:outstates:istemporary:).md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnforwardloss)*