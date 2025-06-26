# MPSCNNYOLOLoss

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSCNNYOLOLoss
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnyololoss/init(coder:device:).md)
- [init(device: any MTLDevice, lossDescriptor: MPSCNNYOLOLossDescriptor)](mpscnnyololoss/init(device:lossdescriptor:).md)
### Instance Properties
- [var anchorBoxes: Data](mpscnnyololoss/anchorboxes.md)
- [var lossClasses: MPSCNNLoss](mpscnnyololoss/lossclasses.md)
- [var lossConfidence: MPSCNNLoss](mpscnnyololoss/lossconfidence.md)
- [var lossWH: MPSCNNLoss](mpscnnyololoss/losswh.md)
- [var lossXY: MPSCNNLoss](mpscnnyololoss/lossxy.md)
- [var maxIOUForObjectAbsence: Float](mpscnnyololoss/maxiouforobjectabsence.md)
- [var minIOUForObjectPresence: Float](mpscnnyololoss/miniouforobjectpresence.md)
- [var numberOfAnchorBoxes: Int](mpscnnyololoss/numberofanchorboxes.md)
- [var reduceAcrossBatch: Bool](mpscnnyololoss/reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](mpscnnyololoss/reductiontype.md)
- [var scaleClass: Float](mpscnnyololoss/scaleclass.md)
- [var scaleNoObject: Float](mpscnnyololoss/scalenoobject.md)
- [var scaleObject: Float](mpscnnyololoss/scaleobject.md)
- [var scaleWH: Float](mpscnnyololoss/scalewh.md)
- [var scaleXY: Float](mpscnnyololoss/scalexy.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, labels: MPSCNNLossLabels) -> MPSImage](mpscnnyololoss/encode(commandbuffer:sourceimage:labels:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, labels: MPSCNNLossLabels, destinationImage: MPSImage)](mpscnnyololoss/encode(commandbuffer:sourceimage:labels:destinationimage:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSCNNLossLabels]) -> [MPSImage]](mpscnnyololoss/encode(commandbuffer:sourceimages:labels:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], labels: [MPSCNNLossLabels], destinationImages: [MPSImage])](mpscnnyololoss/encode(commandbuffer:sourceimages:labels:destinationimages:).md)

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