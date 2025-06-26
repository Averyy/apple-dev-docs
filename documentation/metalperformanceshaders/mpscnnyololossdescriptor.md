# MPSCNNYOLOLossDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class

An object that specifies properties used by a YOLO loss kernel.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNYOLOLossDescriptor
```

## Topics

### Instance Properties
- [var anchorBoxes: Data](mpscnnyololossdescriptor/anchorboxes.md)
- [var classesLossDescriptor: MPSCNNLossDescriptor](mpscnnyololossdescriptor/classeslossdescriptor.md)
- [var confidenceLossDescriptor: MPSCNNLossDescriptor](mpscnnyololossdescriptor/confidencelossdescriptor.md)
- [var maxIOUForObjectAbsence: Float](mpscnnyololossdescriptor/maxiouforobjectabsence.md)
- [var minIOUForObjectPresence: Float](mpscnnyololossdescriptor/miniouforobjectpresence.md)
- [var numberOfAnchorBoxes: Int](mpscnnyololossdescriptor/numberofanchorboxes.md)
- [var reduceAcrossBatch: Bool](mpscnnyololossdescriptor/reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](mpscnnyololossdescriptor/reductiontype.md)
- [var rescore: Bool](mpscnnyololossdescriptor/rescore.md)
- [var scaleClass: Float](mpscnnyololossdescriptor/scaleclass.md)
- [var scaleNoObject: Float](mpscnnyololossdescriptor/scalenoobject.md)
- [var scaleObject: Float](mpscnnyololossdescriptor/scaleobject.md)
- [var scaleWH: Float](mpscnnyololossdescriptor/scalewh.md)
- [var scaleXY: Float](mpscnnyololossdescriptor/scalexy.md)
- [var whLossDescriptor: MPSCNNLossDescriptor](mpscnnyololossdescriptor/whlossdescriptor.md)
- [var xyLossDescriptor: MPSCNNLossDescriptor](mpscnnyololossdescriptor/xylossdescriptor.md)
### Type Methods
- [class func cnnLossDescriptor(withXYLossType: MPSCNNLossType, whLossType: MPSCNNLossType, confidenceLossType: MPSCNNLossType, classesLossType: MPSCNNLossType, reductionType: MPSCNNReductionType, anchorBoxes: Data, numberOfAnchorBoxes: Int) -> MPSCNNYOLOLossDescriptor](mpscnnyololossdescriptor/cnnlossdescriptor(withxylosstype:whlosstype:confidencelosstype:classeslosstype:reductiontype:anchorboxes:numberofanchorboxes:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSCNNLoss](mpscnnloss.md)
  A kernel that computes the loss and loss gradient between specified predictions and labels.
- [class MPSCNNLossDataDescriptor](mpscnnlossdatadescriptor.md)
  An object that specifies properties used by a loss data descriptor.
- [class MPSCNNLossDescriptor](mpscnnlossdescriptor.md)
  An object that specifies properties used by a loss kernel.
- [class MPSCNNLossLabels](mpscnnlosslabels.md)
  A class that stores the per-element weight buffer used by loss and gradient loss kernels.
- [class MPSCNNYOLOLoss](mpscnnyololoss.md)
  A kernel that computes the YOLO loss and loss gradient between specified predictions and labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnyololossdescriptor)*