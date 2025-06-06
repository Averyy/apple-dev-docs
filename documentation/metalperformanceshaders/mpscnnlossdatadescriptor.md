# MPSCNNLossDataDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: cl

An object that specifies properties used by a loss data descriptor.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNLossDataDescriptor : NSObject
```

## Topics

### Initializers
- [init?(data: Data, layout: MPSDataLayout, size: MTLSize)](mpscnnlossdatadescriptor/2951840-init.md)
### Instance Properties
- [var bytesPerImage: Int](mpscnnlossdatadescriptor/2951847-bytesperimage.md)
- [var bytesPerRow: Int](mpscnnlossdatadescriptor/2951849-bytesperrow.md)
- [var layout: MPSDataLayout](mpscnnlossdatadescriptor/2951842-layout.md)
- [var size: MTLSize](mpscnnlossdatadescriptor/2951848-size.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)

## See Also

- [class MPSCNNLoss](mpscnnloss.md)
  A kernel that computes the loss and loss gradient between specified predictions and labels.
- [class MPSCNNLossDescriptor](mpscnnlossdescriptor.md)
  An object that specifies properties used by a loss kernel.
- [class MPSCNNLossLabels](mpscnnlosslabels.md)
  A class that stores the per-element weight buffer used by loss and gradient loss kernels.
- [class MPSCNNYOLOLoss](mpscnnyololoss.md)
  A kernel that computes the YOLO loss and loss gradient between specified predictions and labels.
- [class MPSCNNYOLOLossDescriptor](mpscnnyololossdescriptor.md)
  An object that specifies properties used by a YOLO loss kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlossdatadescriptor)*