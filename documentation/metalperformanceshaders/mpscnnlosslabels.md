# MPSCNNLossLabels

**Framework**: Metal Performance Shaders  
**Kind**: cl

A class that stores the per-element weight buffer used by loss and gradient loss kernels.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNLossLabels : MPSState
```

## Topics

### Initializers
- [init(device: any MTLDevice, labelsDescriptor: MPSCNNLossDataDescriptor)](mpscnnlosslabels/2951850-init.md)
- [init(device: any MTLDevice, lossImageSize: MTLSize, labelsDescriptor: MPSCNNLossDataDescriptor, weightsDescriptor: MPSCNNLossDataDescriptor?)](mpscnnlosslabels/2951841-init.md)
- [init(device: any MTLDevice, lossImageSize: MTLSize, labelsImage: MPSImage, weightsImage: MPSImage?)](mpscnnlosslabels/3114086-init.md)
### Instance Methods
- [func labelsImage() -> MPSImage](mpscnnlosslabels/2976472-labelsimage.md)
- [func lossImage() -> MPSImage](mpscnnlosslabels/2951845-lossimage.md)
- [func weightsImage() -> MPSImage](mpscnnlosslabels/2976473-weightsimage.md)

## Relationships

### Inherits From
- [MPSState](mpsstate.md)

## See Also

- [class MPSCNNLoss](mpscnnloss.md)
  A kernel that computes the loss and loss gradient between specified predictions and labels.
- [class MPSCNNLossDataDescriptor](mpscnnlossdatadescriptor.md)
  An object that specifies properties used by a loss data descriptor.
- [class MPSCNNLossDescriptor](mpscnnlossdescriptor.md)
  An object that specifies properties used by a loss kernel.
- [class MPSCNNYOLOLoss](mpscnnyololoss.md)
  A kernel that computes the YOLO loss and loss gradient between specified predictions and labels.
- [class MPSCNNYOLOLossDescriptor](mpscnnyololossdescriptor.md)
  An object that specifies properties used by a YOLO loss kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlosslabels)*