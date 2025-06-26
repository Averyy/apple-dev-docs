# encodeSequence(commandBuffer:sourceMatrices:destinationMatrices:recurrentInputState:recurrentOutputStates:)

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
func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], destinationMatrices: [MPSMatrix], recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?)
```

## See Also

- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsrnnmatrixinferencelayer/copy(with:device:).md)
- [func encodeBidirectionalSequence(commandBuffer: any MTLCommandBuffer, sourceSequence: [MPSMatrix], destinationForwardMatrices: [MPSMatrix], destinationBackwardMatrices: [MPSMatrix]?)](mpsrnnmatrixinferencelayer/encodebidirectionalsequence(commandbuffer:sourcesequence:destinationforwardmatrices:destinationbackwardmatrices:).md)
- [class MPSRNNRecurrentMatrixState](mpsrnnrecurrentmatrixstate.md)
  A class holds all the data that’s passed from one sequence iteration of the matrix-based recurrent neural network layer to the next.
- [func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], sourceOffsets: UnsafeMutablePointer<Int>?, destinationMatrices: [MPSMatrix], destinationOffsets: UnsafeMutablePointer<Int>?, recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?)](mpsrnnmatrixinferencelayer/encodesequence(commandbuffer:sourcematrices:sourceoffsets:destinationmatrices:destinationoffsets:recurrentinputstate:recurrentoutputstates:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnmatrixinferencelayer/encodesequence(commandbuffer:sourcematrices:destinationmatrices:recurrentinputstate:recurrentoutputstates:))*