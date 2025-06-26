# MPSRNNSingleGateDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class

A description of a simple recurrent block or layer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSRNNSingleGateDescriptor
```

#### Overview

The recurrent neural network (RNN) layer initialized with a [`MPSRNNSingleGateDescriptor`](mpsrnnsinglegatedescriptor.md) transforms the input data (image or matrix) and previous output with a set of filters. Each produces one feature map in the new output data.

You may provide the RNN unit with a single input or a sequence of inputs.

##### Description of Operation

1. Let `x_j` be the input data (at time index `t` of sequence, `j` index containing quadruplet: batch index, `x,y` and feature index (`x = y = 0` for matrices)).
2. Let `h0_j` be the recurrent input (previous output) data from previous time step (at time index `t-1` of sequence).
3. Let `h1_i` be the output data produced at this time step.
4. Let `W_ij, U_ij` be the weights for input and recurrent input data, respectively.
5. Let `b_i` be a bias term.
6. Let `gi(x)` be a neuron activation function.

The new output image `h1_i` data is computed as follows:

```other
h1_i = gi( W_ij * x_j + U_ij * h0_j  + b_i )
```

The `*` stands for convolution (see [`MPSRNNImageInferenceLayer`](mpsrnnimageinferencelayer.md)) or matrix-vector/matrix multiplication (see [`MPSRNNMatrixInferenceLayer`](mpsrnnmatrixinferencelayer.md)).

Summation is over index `j` (except for the batch index), but there’s no summation over repeated index `i` (the output index).

Note that for validity, all intermediate images must be of same size, and the `U` matrix must be square (that is, [`outputFeatureChannels`](mpsrnndescriptor/outputfeaturechannels.md) `==` [`inputFeatureChannels`](mpsrnndescriptor/inputfeaturechannels.md)). Also, the bias terms are scalars with regard to spatial dimensions.

## Topics

### Instance Properties
- [var inputWeights: (any MPSCNNConvolutionDataSource)?](mpsrnnsinglegatedescriptor/inputweights.md)
- [var recurrentWeights: (any MPSCNNConvolutionDataSource)?](mpsrnnsinglegatedescriptor/recurrentweights.md)
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
### Type Methods
- [class func createRNNSingleGateDescriptor(withInputFeatureChannels: Int, outputFeatureChannels: Int) -> Self](mpsrnnsinglegatedescriptor/creaternnsinglegatedescriptor(withinputfeaturechannels:outputfeaturechannels:).md)

## Relationships

### Inherits From
- [MPSRNNDescriptor](mpsrnndescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSRNNImageInferenceLayer](mpsrnnimageinferencelayer.md)
  A recurrent neural network layer for inference on Metal Performance Shaders images.
- [class MPSRNNMatrixInferenceLayer](mpsrnnmatrixinferencelayer.md)
  A recurrent neural network layer for inference on Metal Performance Shaders matrices.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnsinglegatedescriptor)*