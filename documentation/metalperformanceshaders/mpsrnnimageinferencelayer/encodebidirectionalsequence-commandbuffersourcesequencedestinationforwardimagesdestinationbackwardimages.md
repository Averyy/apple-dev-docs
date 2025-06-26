# encodeBidirectionalSequence(commandBuffer:sourceSequence:destinationForwardImages:destinationBackwardImages:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func encodeBidirectionalSequence(commandBuffer: any MTLCommandBuffer, sourceSequence: [MPSImage], destinationForwardImages: [MPSImage], destinationBackwardImages: [MPSImage]?)
```

## See Also

- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsrnnimageinferencelayer/copy(with:device:).md)
- [func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationImages: [MPSImage], recurrentInputState: MPSRNNRecurrentImageState?, recurrentOutputStates: NSMutableArray?)](mpsrnnimageinferencelayer/encodesequence(commandbuffer:sourceimages:destinationimages:recurrentinputstate:recurrentoutputstates:).md)
- [class MPSRNNRecurrentImageState](mpsrnnrecurrentimagestate.md)
  A class that holds all the data that’s passed from one sequence iteration of the image-based recurrent neural network layer (stack) to the next.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnimageinferencelayer/encodebidirectionalsequence(commandbuffer:sourcesequence:destinationforwardimages:destinationbackwardimages:))*