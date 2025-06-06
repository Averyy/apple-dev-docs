# MPSNNImageNode

**Framework**: Metal Performance Shaders  
**Kind**: cl

A placeholder node denoting the position of a neural network image in a graph.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNImageNode : NSObject
```

## Topics

### Initializers
- [init(handle: (any MPSHandle)?)](mpsnnimagenode/2866483-init.md)
### Instance Properties
- [var exportFromGraph: Bool](mpsnnimagenode/2866478-exportfromgraph.md)
- [var format: MPSImageFeatureChannelFormat](mpsnnimagenode/2866498-format.md)
- [enum MPSImageFeatureChannelFormat](mpsimagefeaturechannelformat.md)
  Encodes the representation of a single channel within an image.
- [var handle: (any MPSHandle)?](mpsnnimagenode/2866406-handle.md)
- [var imageAllocator: any MPSImageAllocator](mpsnnimagenode/2866490-imageallocator.md)
- [var stopGradient: Bool](mpsnnimagenode/3020689-stopgradient.md)
- [var synchronizeResource: Bool](mpsnnimagenode/2942638-synchronizeresource.md)
### Type Methods
- [class func exportedNode(with: (any MPSHandle)?) -> Self](mpsnnimagenode/2866440-exportednode.md)
### Supporting Types
- [protocol MPSHandle](mpshandle.md)
  The protocol that provides resource identification.
- [enum MPSImageFeatureChannelFormat](mpsimagefeaturechannelformat.md)
  Encodes the representation of a single channel within an image.
- [protocol MPSImageAllocator](mpsimageallocator.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [class MPSNNGraph](mpsnngraph.md)
  An optimized representation of a graph of neural network image and filter nodes.
- [protocol MPSHandle](mpshandle.md)
  The protocol that provides resource identification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnimagenode)*