# MPSNNForwardLoss

**Framework**: Metal Performance Shaders  
**Kind**: cl

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNForwardLoss : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsnnforwardloss/3131801-init.md)
- [init(device: any MTLDevice, lossDescriptor: MPSCNNLossDescriptor)](mpsnnforwardloss/3131802-init.md)
### Instance Properties
- [var delta: Float](mpsnnforwardloss/3131797-delta.md)
- [var epsilon: Float](mpsnnforwardloss/3131800-epsilon.md)
- [var labelSmoothing: Float](mpsnnforwardloss/3131803-labelsmoothing.md)
- [var lossType: MPSCNNLossType](mpsnnforwardloss/3131804-losstype.md)
- [var numberOfClasses: Int](mpsnnforwardloss/3131805-numberofclasses.md)
- [var reduceAcrossBatch: Bool](mpsnnforwardloss/3547985-reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](mpsnnforwardloss/3131806-reductiontype.md)
- [var weight: Float](mpsnnforwardloss/3131807-weight.md)
### Instance Methods
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSImage], weights: [MPSImage]?, destinationStates: [MPSState]?, destinationImages: [MPSImage])](mpsnnforwardloss/3131798-encodebatch.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSImage], weights: [MPSImage]?, outStates: AutoreleasingUnsafeMutablePointer<NSArray?>?, isTemporary: Bool) -> [MPSImage]](mpsnnforwardloss/3131799-encodebatch.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnforwardloss)*