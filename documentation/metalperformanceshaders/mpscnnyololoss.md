# MPSCNNYOLOLoss

**Framework**: Metal Performance Shaders  
**Kind**: cl

A kernel that computes the YOLO loss and loss gradient between specified predictions and labels.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNYOLOLoss : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnyololoss/2976480-init.md)
- [init(device: any MTLDevice, lossDescriptor: MPSCNNYOLOLossDescriptor)](mpscnnyololoss/2976481-init.md)
### Instance Properties
- [var anchorBoxes: Data](mpscnnyololoss/2976475-anchorboxes.md)
- [var lossClasses: MPSCNNLoss](mpscnnyololoss/2976482-lossclasses.md)
- [var lossConfidence: MPSCNNLoss](mpscnnyololoss/2976483-lossconfidence.md)
- [var lossWH: MPSCNNLoss](mpscnnyololoss/2976484-losswh.md)
- [var lossXY: MPSCNNLoss](mpscnnyololoss/2976485-lossxy.md)
- [var maxIOUForObjectAbsence: Float](mpscnnyololoss/2976486-maxiouforobjectabsence.md)
- [var minIOUForObjectPresence: Float](mpscnnyololoss/2976487-miniouforobjectpresence.md)
- [var numberOfAnchorBoxes: Int](mpscnnyololoss/2976488-numberofanchorboxes.md)
- [var reduceAcrossBatch: Bool](mpscnnyololoss/3547983-reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](mpscnnyololoss/2976489-reductiontype.md)
- [var scaleClass: Float](mpscnnyololoss/2976490-scaleclass.md)
- [var scaleNoObject: Float](mpscnnyololoss/2976491-scalenoobject.md)
- [var scaleObject: Float](mpscnnyololoss/2976492-scaleobject.md)
- [var scaleWH: Float](mpscnnyololoss/2976493-scalewh.md)
- [var scaleXY: Float](mpscnnyololoss/2976494-scalexy.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, labels: MPSCNNLossLabels) -> MPSImage](mpscnnyololoss/2976478-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, labels: MPSCNNLossLabels, destinationImage: MPSImage)](mpscnnyololoss/2976479-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSCNNLossLabels]) -> [MPSImage]](mpscnnyololoss/2976476-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSCNNLossLabels], destinationImages: [MPSImage])](mpscnnyololoss/2976477-encode.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)

## See Also

- [class MPSCNNLoss](mpscnnloss.md)
  A kernel that computes the loss and loss gradient between specified predictions and labels.
- [class MPSCNNLossDataDescriptor](mpscnnlossdatadescriptor.md)
  An object that specifies properties used by a loss data descriptor.
- [class MPSCNNLossDescriptor](mpscnnlossdescriptor.md)
  An object that specifies properties used by a loss kernel.
- [class MPSCNNLossLabels](mpscnnlosslabels.md)
  A class that stores the per-element weight buffer used by loss and gradient loss kernels.
- [class MPSCNNYOLOLossDescriptor](mpscnnyololossdescriptor.md)
  An object that specifies properties used by a YOLO loss kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnyololoss)*