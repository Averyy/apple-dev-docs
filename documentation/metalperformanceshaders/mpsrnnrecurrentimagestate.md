# MPSRNNRecurrentImageState

**Framework**: Metal Performance Shaders  
**Kind**: class

A class that holds all the data that’s passed from one sequence iteration of the image-based recurrent neural network layer (stack) to the next.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSRNNRecurrentImageState
```

## Topics

### Instance Methods
- [func getMemoryCellImage(forLayerIndex: Int) -> MPSImage?](mpsrnnrecurrentimagestate/getmemorycellimage(forlayerindex:).md)
- [func getRecurrentOutputImage(forLayerIndex: Int) -> MPSImage?](mpsrnnrecurrentimagestate/getrecurrentoutputimage(forlayerindex:).md)

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

- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsrnnimageinferencelayer/copy(with:device:).md)
- [func encodeBidirectionalSequence(commandBuffer: any MTLCommandBuffer, sourceSequence: [MPSImage], destinationForwardImages: [MPSImage], destinationBackwardImages: [MPSImage]?)](mpsrnnimageinferencelayer/encodebidirectionalsequence(commandbuffer:sourcesequence:destinationforwardimages:destinationbackwardimages:).md)
- [func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationImages: [MPSImage], recurrentInputState: MPSRNNRecurrentImageState?, recurrentOutputStates: NSMutableArray?)](mpsrnnimageinferencelayer/encodesequence(commandbuffer:sourceimages:destinationimages:recurrentinputstate:recurrentoutputstates:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnrecurrentimagestate)*