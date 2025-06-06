# MPSCNNLossDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: cl

An object that specifies properties used by a loss kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNLossDescriptor : NSObject
```

## Topics

### Initializers
- [init(type: MPSCNNLossType, reductionType: MPSCNNReductionType)](mpscnnlossdescriptor/2942373-init.md)
### Instance Properties
- [var delta: Float](mpscnnlossdescriptor/2942378-delta.md)
- [var epsilon: Float](mpscnnlossdescriptor/2942362-epsilon.md)
- [var labelSmoothing: Float](mpscnnlossdescriptor/2942369-labelsmoothing.md)
- [var lossType: MPSCNNLossType](mpscnnlossdescriptor/2942381-losstype.md)
- [var numberOfClasses: Int](mpscnnlossdescriptor/2942382-numberofclasses.md)
- [var reduceAcrossBatch: Bool](mpscnnlossdescriptor/3547982-reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](mpscnnlossdescriptor/2942388-reductiontype.md)
- [var weight: Float](mpscnnlossdescriptor/2942367-weight.md)

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
- [class MPSCNNLossLabels](mpscnnlosslabels.md)
  A class that stores the per-element weight buffer used by loss and gradient loss kernels.
- [class MPSCNNYOLOLoss](mpscnnyololoss.md)
  A kernel that computes the YOLO loss and loss gradient between specified predictions and labels.
- [class MPSCNNYOLOLossDescriptor](mpscnnyololossdescriptor.md)
  An object that specifies properties used by a YOLO loss kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlossdescriptor)*