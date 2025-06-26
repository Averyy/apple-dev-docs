# encodeSequence(commandBuffer:sourceMatrices:sourceOffsets:destinationMatrices:destinationOffsets:recurrentInputState:recurrentOutputStates:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], sourceOffsets: UnsafeMutablePointer<Int>?, destinationMatrices: [MPSMatrix], destinationOffsets: UnsafeMutablePointer<Int>?, recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?)
```

## See Also

- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsrnnmatrixinferencelayer/copy(with:device:).md)
- [func encodeBidirectionalSequence(commandBuffer: any MTLCommandBuffer, sourceSequence: [MPSMatrix], destinationForwardMatrices: [MPSMatrix], destinationBackwardMatrices: [MPSMatrix]?)](mpsrnnmatrixinferencelayer/encodebidirectionalsequence(commandbuffer:sourcesequence:destinationforwardmatrices:destinationbackwardmatrices:).md)
- [func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], destinationMatrices: [MPSMatrix], recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?)](mpsrnnmatrixinferencelayer/encodesequence(commandbuffer:sourcematrices:destinationmatrices:recurrentinputstate:recurrentoutputstates:).md)
- [class MPSRNNRecurrentMatrixState](mpsrnnrecurrentmatrixstate.md)
  A class holds all the data that’s passed from one sequence iteration of the matrix-based recurrent neural network layer to the next.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnmatrixinferencelayer/encodesequence(commandbuffer:sourcematrices:sourceoffsets:destinationmatrices:destinationoffsets:recurrentinputstate:recurrentoutputstates:))*