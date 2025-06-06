# MPSNNLossGradient

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
class MPSNNLossGradient : MPSCNNBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsnnlossgradient/3131816-init.md)
- [init(device: any MTLDevice, lossDescriptor: MPSCNNLossDescriptor)](mpsnnlossgradient/3131817-init.md)
### Instance Properties
- [var computeLabelGradients: Bool](mpsnnlossgradient/3131811-computelabelgradients.md)
- [var delta: Float](mpsnnlossgradient/3131812-delta.md)
- [var epsilon: Float](mpsnnlossgradient/3131815-epsilon.md)
- [var labelSmoothing: Float](mpsnnlossgradient/3131818-labelsmoothing.md)
- [var lossType: MPSCNNLossType](mpsnnlossgradient/3131819-losstype.md)
- [var numberOfClasses: Int](mpsnnlossgradient/3131820-numberofclasses.md)
- [var reduceAcrossBatch: Bool](mpsnnlossgradient/3547986-reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](mpsnnlossgradient/3131821-reductiontype.md)
- [var weight: Float](mpsnnlossgradient/3131822-weight.md)
### Instance Methods
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], labels: [MPSImage], weights: [MPSImage]?, sourceStates: [MPSState]?) -> [MPSImage]](mpsnnlossgradient/3131813-encodebatch.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceGradients: [MPSImage], sourceImages: [MPSImage], labels: [MPSImage], weights: [MPSImage]?, sourceStates: [MPSState]?, destinationGradients: [MPSImage])](mpsnnlossgradient/3131814-encodebatch.md)

## Relationships

### Inherits From
- [MPSCNNBinaryKernel](mpscnnbinarykernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnlossgradient)*