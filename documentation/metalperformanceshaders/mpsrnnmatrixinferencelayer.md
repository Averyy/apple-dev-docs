# MPSRNNMatrixInferenceLayer

**Framework**: Metal Performance Shaders  
**Kind**: class

A recurrent neural network layer for inference on Metal Performance Shaders matrices.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSRNNMatrixInferenceLayer
```

#### Overview

The [`MPSRNNMatrixInferenceLayer`](mpsrnnmatrixinferencelayer.md) specifies a recurrent neural network layer for inference on [`MPSMatrix`](mpsmatrix.md) objects. Two types of recurrent layers are supported:

- [`MPSRNNImageInferenceLayer`](mpsrnnimageinferencelayer.md)—Operates with convolutions on images.
- [`MPSRNNMatrixInferenceLayer`](mpsrnnmatrixinferencelayer.md)—Operates on matrices.

You can use [`MPSRNNImageInferenceLayer`](mpsrnnimageinferencelayer.md) to implement the latter by using 1 x 1 images, but due to image size restrictions and performance, [`MPSRNNMatrixInferenceLayer`](mpsrnnmatrixinferencelayer.md) is the better choice for linear recurrent layers.

[`MPSRNNMatrixInferenceLayer`](mpsrnnmatrixinferencelayer.md) is initialized using either of the following:

- A single [`MPSRNNDescriptor`](mpsrnndescriptor.md) instance, which further specifies the recurrent network layer.
- An array of [`MPSRNNDescriptor`](mpsrnndescriptor.md) instances, which specifies a stack of recurrent layers that can operate in parallel a subset of the inputs in a sequence of inputs and recurrent outputs.

Stacks with bidirectionally traversing encode functions don’t support starting from a previous set of recurrent states. However, you can achieve this effect by defining two separate unidirectional stacks of layers, running the same input sequence on them separately (one forward and one backward), and ultimately combining the two result sequences.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsrnnmatrixinferencelayer/init(coder:device:).md)
- [init(device: any MTLDevice, rnnDescriptor: MPSRNNDescriptor)](mpsrnnmatrixinferencelayer/init(device:rnndescriptor:).md)
- [init(device: any MTLDevice, rnnDescriptors: [MPSRNNDescriptor])](mpsrnnmatrixinferencelayer/init(device:rnndescriptors:).md)
- [class MPSRNNDescriptor](mpsrnndescriptor.md)
  A description of a recursive neural network block or layer.
### Instance Properties
- [var bidirectionalCombineMode: MPSRNNBidirectionalCombineMode](mpsrnnmatrixinferencelayer/bidirectionalcombinemode.md)
- [enum MPSRNNBidirectionalCombineMode](mpsrnnbidirectionalcombinemode.md)
  Modes that define how two images or matrices are combined.
- [var inputFeatureChannels: Int](mpsrnnmatrixinferencelayer/inputfeaturechannels.md)
- [var numberOfLayers: Int](mpsrnnmatrixinferencelayer/numberoflayers.md)
- [var outputFeatureChannels: Int](mpsrnnmatrixinferencelayer/outputfeaturechannels.md)
- [var recurrentOutputIsTemporary: Bool](mpsrnnmatrixinferencelayer/recurrentoutputistemporary.md)
- [var storeAllIntermediateStates: Bool](mpsrnnmatrixinferencelayer/storeallintermediatestates.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsrnnmatrixinferencelayer/copy(with:device:).md)
- [func encodeBidirectionalSequence(commandBuffer: any MTLCommandBuffer, sourceSequence: [MPSMatrix], destinationForwardMatrices: [MPSMatrix], destinationBackwardMatrices: [MPSMatrix]?)](mpsrnnmatrixinferencelayer/encodebidirectionalsequence(commandbuffer:sourcesequence:destinationforwardmatrices:destinationbackwardmatrices:).md)
- [func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], destinationMatrices: [MPSMatrix], recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?)](mpsrnnmatrixinferencelayer/encodesequence(commandbuffer:sourcematrices:destinationmatrices:recurrentinputstate:recurrentoutputstates:).md)
- [class MPSRNNRecurrentMatrixState](mpsrnnrecurrentmatrixstate.md)
  A class holds all the data that’s passed from one sequence iteration of the matrix-based recurrent neural network layer to the next.
- [func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], sourceOffsets: UnsafeMutablePointer<Int>?, destinationMatrices: [MPSMatrix], destinationOffsets: UnsafeMutablePointer<Int>?, recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?)](mpsrnnmatrixinferencelayer/encodesequence(commandbuffer:sourcematrices:sourceoffsets:destinationmatrices:destinationoffsets:recurrentinputstate:recurrentoutputstates:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSRNNImageInferenceLayer](mpsrnnimageinferencelayer.md)
  A recurrent neural network layer for inference on Metal Performance Shaders images.
- [class MPSRNNSingleGateDescriptor](mpsrnnsinglegatedescriptor.md)
  A description of a simple recurrent block or layer.
- [class MPSGRUDescriptor](mpsgrudescriptor.md)
  A description of a gated recurrent unit block or layer.
- [class MPSLSTMDescriptor](mpslstmdescriptor.md)
  A description of a long short-term memory block or layer.
- [enum MPSRNNSequenceDirection](mpsrnnsequencedirection.md)
  Directions that a sequence of inputs can be processed by a recurrent neural network layer.
- [class MPSRNNMatrixTrainingLayer](mpsrnnmatrixtraininglayer.md)
  A layer for training recurrent neural networks on Metal Performance Shaders matrices.
- [class MPSRNNMatrixTrainingState](mpsrnnmatrixtrainingstate.md)
  A class that holds data from a forward pass to be used in a backward pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnmatrixinferencelayer)*