# MPSCNNLoss

**Framework**: Metal Performance Shaders  
**Kind**: cl

A kernel that computes the loss and loss gradient between specified predictions and labels.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNLoss : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnloss/2942379-init.md)
- [init(device: any MTLDevice, lossDescriptor: MPSCNNLossDescriptor)](mpscnnloss/2942377-init.md)
### Instance Properties
- [var delta: Float](mpscnnloss/2942360-delta.md)
- [var epsilon: Float](mpscnnloss/2942371-epsilon.md)
- [var labelSmoothing: Float](mpscnnloss/2942358-labelsmoothing.md)
- [var lossType: MPSCNNLossType](mpscnnloss/2942359-losstype.md)
- [var numberOfClasses: Int](mpscnnloss/2942389-numberofclasses.md)
- [var reduceAcrossBatch: Bool](mpscnnloss/3547981-reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](mpscnnloss/2942365-reductiontype.md)
- [var weight: Float](mpscnnloss/2942387-weight.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, labels: MPSCNNLossLabels) -> MPSImage](mpscnnloss/2951838-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, labels: MPSCNNLossLabels, destinationImage: MPSImage)](mpscnnloss/2951843-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSCNNLossLabels]) -> [MPSImage]](mpscnnloss/2951839-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSCNNLossLabels], destinationImages: [MPSImage])](mpscnnloss/2951846-encode.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)

## See Also

- [class MPSCNNLossDataDescriptor](mpscnnlossdatadescriptor.md)
  An object that specifies properties used by a loss data descriptor.
- [class MPSCNNLossDescriptor](mpscnnlossdescriptor.md)
  An object that specifies properties used by a loss kernel.
- [class MPSCNNLossLabels](mpscnnlosslabels.md)
  A class that stores the per-element weight buffer used by loss and gradient loss kernels.
- [class MPSCNNYOLOLoss](mpscnnyololoss.md)
  A kernel that computes the YOLO loss and loss gradient between specified predictions and labels.
- [class MPSCNNYOLOLossDescriptor](mpscnnyololossdescriptor.md)
  An object that specifies properties used by a YOLO loss kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnloss)*