# MPSCNNYOLOLossDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: cl

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
class MPSCNNYOLOLossDescriptor : NSObject
```

## Topics

### Instance Properties
- [var anchorBoxes: Data](mpscnnyololossdescriptor/2976498-anchorboxes.md)
- [var classesLossDescriptor: MPSCNNLossDescriptor](mpscnnyololossdescriptor/2976499-classeslossdescriptor.md)
- [var confidenceLossDescriptor: MPSCNNLossDescriptor](mpscnnyololossdescriptor/2976501-confidencelossdescriptor.md)
- [var maxIOUForObjectAbsence: Float](mpscnnyololossdescriptor/2976502-maxiouforobjectabsence.md)
- [var minIOUForObjectPresence: Float](mpscnnyololossdescriptor/2976503-miniouforobjectpresence.md)
- [var numberOfAnchorBoxes: Int](mpscnnyololossdescriptor/2976504-numberofanchorboxes.md)
- [var reduceAcrossBatch: Bool](mpscnnyololossdescriptor/3547984-reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](mpscnnyololossdescriptor/2976505-reductiontype.md)
- [var rescore: Bool](mpscnnyololossdescriptor/2976506-rescore.md)
- [var scaleClass: Float](mpscnnyololossdescriptor/2976507-scaleclass.md)
- [var scaleNoObject: Float](mpscnnyololossdescriptor/2976508-scalenoobject.md)
- [var scaleObject: Float](mpscnnyololossdescriptor/2976509-scaleobject.md)
- [var scaleWH: Float](mpscnnyololossdescriptor/2976510-scalewh.md)
- [var scaleXY: Float](mpscnnyololossdescriptor/2976511-scalexy.md)
- [var whLossDescriptor: MPSCNNLossDescriptor](mpscnnyololossdescriptor/2976496-whlossdescriptor.md)
- [var xyLossDescriptor: MPSCNNLossDescriptor](mpscnnyololossdescriptor/2976497-xylossdescriptor.md)
### Type Methods
- [class func cnnLossDescriptor(withXYLossType: MPSCNNLossType, whLossType: MPSCNNLossType, confidenceLossType: MPSCNNLossType, classesLossType: MPSCNNLossType, reductionType: MPSCNNReductionType, anchorBoxes: Data, numberOfAnchorBoxes: Int) -> MPSCNNYOLOLossDescriptor](mpscnnyololossdescriptor/2976500-cnnlossdescriptor.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)

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