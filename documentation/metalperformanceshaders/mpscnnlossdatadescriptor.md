# MPSCNNLossDataDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSCNNLossDataDescriptor
```

## Topics

### Initializers
- [init?(data: Data, layout: MPSDataLayout, size: MTLSize)](mpscnnlossdatadescriptor/init(data:layout:size:).md)
### Instance Properties
- [var bytesPerImage: Int](mpscnnlossdatadescriptor/bytesperimage.md)
- [var bytesPerRow: Int](mpscnnlossdatadescriptor/bytesperrow.md)
- [var layout: MPSDataLayout](mpscnnlossdatadescriptor/layout.md)
- [var size: MTLSize](mpscnnlossdatadescriptor/size.md)

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