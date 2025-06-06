# MPSGRUDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: cl

A description of a gated recurrent unit block or layer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGRUDescriptor : MPSRNNDescriptor
```

#### Overview

The recurrent neural network (RNN) layer initialized with a [`MPSGRUDescriptor`](mpsgrudescriptor.md) transforms the input data (image or matrix) and previous output with a set of filters. Each produces one feature map in the output data according to the gated recurrent unit (GRU) unit formula detailed below. 

You may provide the GRU unit with a single input or a sequence of inputs. The layer also supports p-norm gating.

##### 2888086

1. Let `x_j` be the input data (at time index `t` of sequence, `j` index containing quadruplet: batch index, `x,y` and feature index (`x = y = 0` for matrices)).
2. Let `h0_`j be the recurrent input (previous output) data from previous time step (at time index `t-1` of sequence).
3. Let `h_i` be the proposed new output.
4. Let `h1_i` be the output data produced at this time step.
5. Let `Wz_ij`, `Uz_ij` be the input gate weights for input and recurrent input data, respectively.
6. Let `bi_i` be the bias for the input gate.
7. Let `Wr_ij`, `Ur_ij` be the recurrent gate weights for input and recurrent input data, respectively.
8. Let `br_i` be the bias for the recurrent gate.
9. Let `Wh_ij`, `Uh_ij`, `Vh_ij` be the output gate weights for input, recurrent gate, and input gate, respectively.
10. Let `bh_i` be the bias for the output gate.
11. Let `gz(x``)`, `gr(x)`, `gh(x)` be the neuron activation function for the input, recurrent, and output gates.
12. Let `p > 0` be a scalar variable (typical `p >= 1.0`) that defines the p-norm gating norm value.

The output of the GRU layer is computed as follows:

```other
z_i = gz(  Wz_ij * x_j  +  Uz_ij * h0_j  +  bz_i  )
r_i = gr(  Wr_ij * x_j  +  Ur_ij * h0_j  +  br_i  )
c_i =      Uh_ij * (r_j h0_j)  +  Vh_ij * (z_j h0_j)
h_i = gh(  Wh_ij * x_j  + c_i + bh_i  )

h1_i = ( 1 - z_i ^ p)^(1/p) h0_i + z_i h_i
```

The `*` stands for convolution (see [`MPSRNNImageInferenceLayer`](mpsrnnimageinferencelayer.md)) or matrix-vector/matrix multiplication (see [`MPSRNNMatrixInferenceLayer`](mpsrnnmatrixinferencelayer.md)).

Summation is over index `j` (except for the batch index), but there's no summation over repeated index `i`,` `the output index.

Note that for validity, all intermediate images must be of same size, and all `U` and `V` matrices must be square (that is, [`outputFeatureChannels`](mpsrnndescriptor/2865702-outputfeaturechannels.md)` ==` [`inputFeatureChannels`](mpsrnndescriptor/2865707-inputfeaturechannels.md)). Also, the bias terms are scalars with regard to spatial dimensions. The conventional GRU block is achieved by setting `Vh = 0` (nil), and the Minimal Gated Unit is achieved with `Uh = 0`.

## Topics

### Instance Properties
- [var flipOutputGates: Bool](mpsgrudescriptor/2878271-flipoutputgates.md)
- [var gatePnormValue: Float](mpsgrudescriptor/2873332-gatepnormvalue.md)
- [var inputGateInputWeights: (any MPSCNNConvolutionDataSource)?](mpsgrudescriptor/2865690-inputgateinputweights.md)
- [var inputGateRecurrentWeights: (any MPSCNNConvolutionDataSource)?](mpsgrudescriptor/2865724-inputgaterecurrentweights.md)
- [var outputGateInputGateWeights: (any MPSCNNConvolutionDataSource)?](mpsgrudescriptor/2878270-outputgateinputgateweights.md)
- [var outputGateInputWeights: (any MPSCNNConvolutionDataSource)?](mpsgrudescriptor/2865722-outputgateinputweights.md)
- [var outputGateRecurrentWeights: (any MPSCNNConvolutionDataSource)?](mpsgrudescriptor/2865699-outputgaterecurrentweights.md)
- [var recurrentGateInputWeights: (any MPSCNNConvolutionDataSource)?](mpsgrudescriptor/2865719-recurrentgateinputweights.md)
- [var recurrentGateRecurrentWeights: (any MPSCNNConvolutionDataSource)?](mpsgrudescriptor/2865695-recurrentgaterecurrentweights.md)
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
### Type Methods
- [class func createGRUDescriptor(withInputFeatureChannels: Int, outputFeatureChannels: Int) -> Self](mpsgrudescriptor/2865715-creategrudescriptor.md)

## Relationships

### Inherits From
- [MPSRNNDescriptor](mpsrnndescriptor.md)

## See Also

- [class MPSRNNImageInferenceLayer](mpsrnnimageinferencelayer.md)
  A recurrent neural network layer for inference on Metal Performance Shaders images.
- [class MPSRNNMatrixInferenceLayer](mpsrnnmatrixinferencelayer.md)
  A recurrent neural network layer for inference on Metal Performance Shaders matrices.
- [class MPSRNNSingleGateDescriptor](mpsrnnsinglegatedescriptor.md)
  A description of a simple recurrent block or layer.
- [class MPSLSTMDescriptor](mpslstmdescriptor.md)
  A description of a long short-term memory block or layer.
- [enum MPSRNNSequenceDirection](mpsrnnsequencedirection.md)
  Directions that a sequence of inputs can be processed by a recurrent neural network layer.
- [class MPSRNNMatrixTrainingLayer](mpsrnnmatrixtraininglayer.md)
  A layer for training recurrent neural networks on Metal Performance Shaders matrices.
- [class MPSRNNMatrixTrainingState](mpsrnnmatrixtrainingstate.md)
  A class that holds data from a forward pass to be used in a backward pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsgrudescriptor)*