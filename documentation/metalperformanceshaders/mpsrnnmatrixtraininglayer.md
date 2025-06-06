# MPSRNNMatrixTrainingLayer

**Framework**: Metal Performance Shaders  
**Kind**: cl

A layer for training recurrent neural networks on Metal Performance Shaders matrices.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSRNNMatrixTrainingLayer : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsrnnmatrixtraininglayer/2966793-init.md)
- [init(device: any MTLDevice, rnnDescriptor: MPSRNNDescriptor, trainableWeights: NSMutableArray)](mpsrnnmatrixtraininglayer/2966794-init.md)
### Instance Properties
- [var accumulateWeightGradients: Bool](mpsrnnmatrixtraininglayer/2966783-accumulateweightgradients.md)
- [var inputFeatureChannels: Int](mpsrnnmatrixtraininglayer/2966795-inputfeaturechannels.md)
- [var outputFeatureChannels: Int](mpsrnnmatrixtraininglayer/2966796-outputfeaturechannels.md)
- [var recurrentOutputIsTemporary: Bool](mpsrnnmatrixtraininglayer/2966797-recurrentoutputistemporary.md)
- [var storeAllIntermediateStates: Bool](mpsrnnmatrixtraininglayer/2966798-storeallintermediatestates.md)
- [var trainingStateIsTemporary: Bool](mpsrnnmatrixtraininglayer/2966799-trainingstateistemporary.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsrnnmatrixtraininglayer/2966784-copy.md)
- [func createTemporaryWeightGradientMatrices(NSMutableArray, dataType: MPSDataType, commandBuffer: any MTLCommandBuffer)](mpsrnnmatrixtraininglayer/2966785-createtemporaryweightgradientmat.md)
- [func createWeightGradientMatrices(NSMutableArray, dataType: MPSDataType)](mpsrnnmatrixtraininglayer/2966786-createweightgradientmatrices.md)
- [func createWeightMatrices(NSMutableArray)](mpsrnnmatrixtraininglayer/2966787-createweightmatrices.md)
- [func encodeCopyWeights(commandBuffer: any MTLCommandBuffer, weights: [MPSMatrix], matrixId: MPSRNNMatrixId, matrix: MPSMatrix, copyFromWeightsToMatrix: Bool, matrixOffset: MTLOrigin)](mpsrnnmatrixtraininglayer/2966788-encodecopyweights.md)
- [func encodeForwardSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], destinationMatrices: [MPSMatrix], trainingStates: NSMutableArray, weights: [MPSMatrix])](mpsrnnmatrixtraininglayer/2966789-encodeforwardsequence.md)
- [func encodeForwardSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], sourceOffsets: UnsafeMutablePointer<Int>?, destinationMatrices: [MPSMatrix], destinationOffsets: UnsafeMutablePointer<Int>?, trainingStates: NSMutableArray, recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?, weights: [MPSMatrix])](mpsrnnmatrixtraininglayer/2966790-encodeforwardsequence.md)
- [func encodeGradientSequence(commandBuffer: any MTLCommandBuffer, forwardSources: [MPSMatrix], forwardSourceOffsets: UnsafeMutablePointer<Int>?, sourceGradients: [MPSMatrix], sourceOffsets: UnsafeMutablePointer<Int>?, destinationGradients: [MPSMatrix]?, destinationOffsets: UnsafeMutablePointer<Int>?, weightGradients: [MPSMatrix]?, trainingStates: [MPSRNNMatrixTrainingState], recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?, weights: [MPSMatrix])](mpsrnnmatrixtraininglayer/2966791-encodegradientsequence.md)
- [func encodeGradientSequence(commandBuffer: any MTLCommandBuffer, forwardSources: [MPSMatrix], sourceGradients: [MPSMatrix], destinationGradients: [MPSMatrix]?, weightGradients: [MPSMatrix]?, trainingStates: [MPSRNNMatrixTrainingState], weights: [MPSMatrix])](mpsrnnmatrixtraininglayer/2966792-encodegradientsequence.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)

## See Also

- [class MPSRNNImageInferenceLayer](mpsrnnimageinferencelayer.md)
  A recurrent neural network layer for inference on Metal Performance Shaders images.
- [class MPSRNNMatrixInferenceLayer](mpsrnnmatrixinferencelayer.md)
  A recurrent neural network layer for inference on Metal Performance Shaders matrices.
- [class MPSRNNSingleGateDescriptor](mpsrnnsinglegatedescriptor.md)
  A description of a simple recurrent block or layer.
- [class MPSGRUDescriptor](mpsgrudescriptor.md)
  A description of a gated recurrent unit block or layer.
- [class MPSLSTMDescriptor](mpslstmdescriptor.md)
  A description of a long short-term memory block or layer.
- [enum MPSRNNSequenceDirection](mpsrnnsequencedirection.md)
  Directions that a sequence of inputs can be processed by a recurrent neural network layer.
- [class MPSRNNMatrixTrainingState](mpsrnnmatrixtrainingstate.md)
  A class that holds data from a forward pass to be used in a backward pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnmatrixtraininglayer)*