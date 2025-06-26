# MPSCNNLossLabels

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSCNNLossLabels
```

## Topics

### Initializers
- [convenience init(device: any MTLDevice, labelsDescriptor: MPSCNNLossDataDescriptor)](mpscnnlosslabels/init(device:labelsdescriptor:).md)
- [init(device: any MTLDevice, lossImageSize: MTLSize, labelsDescriptor: MPSCNNLossDataDescriptor, weightsDescriptor: MPSCNNLossDataDescriptor?)](mpscnnlosslabels/init(device:lossimagesize:labelsdescriptor:weightsdescriptor:).md)
- [init(device: any MTLDevice, lossImageSize: MTLSize, labelsImage: MPSImage, weightsImage: MPSImage?)](mpscnnlosslabels/init(device:lossimagesize:labelsimage:weightsimage:).md)
### Instance Methods
- [func labelsImage() -> MPSImage](mpscnnlosslabels/labelsimage.md)
- [func lossImage() -> MPSImage](mpscnnlosslabels/lossimage.md)
- [func weightsImage() -> MPSImage](mpscnnlosslabels/weightsimage.md)

## Relationships

### Inherits From
- [MPSState](mpsstate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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