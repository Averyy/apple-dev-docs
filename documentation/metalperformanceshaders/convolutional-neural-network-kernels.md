# Convolutional Neural Network Kernels

**Framework**: Metal Performance Shaders

Build neural networks with layers.

#### Overview

- Think carefully about the edge mode requested for pooling layers. The default value is [`MPSImageEdgeMode.zero`](mpsimageedgemode/zero.md), but there are times when a [`MPSImageEdgeMode.clamp`](mpsimageedgemode/clamp.md) value may be better.
- To avoid reading off the edge of an image for filters that have a filter area (convolution, pooling), set `MPSCNNKernel.offset = (MPSOffset){ .x = kernelWidth/2, .y = kernelHeight/2, .z = 0}` and reduce the size of the output image by `{kernelWidth-1, kernelHeight-1, 0}`. The filter area stretches up and to the left of the kernel offset by `{kernelWidth/2, kernelHeight/2}`.
- Always remember the following distinction:
- The [`MPSCNNConvolution`](mpscnnconvolution.md) class takes weights in the order `weight[outputChannels][kernelHeight][kernelWidth][inputChannels/groups]`.
- The [`MPSCNNFullyConnected`](mpscnnfullyconnected.md) class takes weights in the order `weight[outputChannels][sourceWidth][sourceHeight][inputChannels]`.
- Initialize [`MPSCNNKernel`](mpscnnkernel.md) objects once and reuse them.
- You can use [`MPSCNNNeuron`](mpscnnneuron.md) objects and similar to perform pre-processing of images, such as scaling and resizing.
- Specify a neuron filter with an [`MPSCNNConvolutionDescriptor`](mpscnnconvolutiondescriptor.md) object to combine the convolution and neuron operations.
- Use [`MPSTemporaryImage`](mpstemporaryimage.md) objects for intermediate images that live for a short period of time (one [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) object).

[`MPSTemporaryImage`](mpstemporaryimage.md) objects can reduce the amount of memory used by the CNN by several folds, and similarly reduce the amount of CPU time spent allocating storage and latency between the time a command buffer is committed and when it is actually executed on the GPU.

You cannot read or write to a [`MPSTemporaryImage`](mpstemporaryimage.md) object using the CPU. Generally, [`MPSTemporaryImage`](mpstemporaryimage.md) objects should be created as needed and thrown away promptly. Persistent objects should not retain them.

Please be sure to understand the purpose of the [`readCount`](mpstemporaryimage/readcount.md) property.

- Because the Metal Performance Shaders framework encodes its work in place in your command buffer, you always have the option to insert your own code in between [`MPSCNNKernel`](mpscnnkernel.md) encodings as a Metal function for tasks not covered by the framework. You do not need to use the Metal Performance Shaders framework for everything.

## Topics

### Arithmetic Layers
- [class MPSCNNAdd](mpscnnadd.md)
  An addition operator.
- [class MPSCNNAddGradient](mpscnnaddgradient.md)
  A gradient addition operator.
- [class MPSCNNSubtract](mpscnnsubtract.md)
  A subtraction operator.
- [class MPSCNNSubtractGradient](mpscnnsubtractgradient.md)
  A gradient subtraction operator.
- [class MPSCNNMultiply](mpscnnmultiply.md)
  A multiply operator.
- [class MPSCNNMultiplyGradient](mpscnnmultiplygradient.md)
  A gradient multiply operator.
- [class MPSCNNDivide](mpscnndivide.md)
  A division operator.
- [class MPSCNNArithmetic](mpscnnarithmetic.md)
  The base class for arithmetic operators.
- [class MPSCNNArithmeticGradient](mpscnnarithmeticgradient.md)
  The base class for gradient arithmetic operators.
- [class MPSCNNArithmeticGradientState](mpscnnarithmeticgradientstate.md)
  An object that stores the clamp mask used by gradient arithmetic operators.
### Convolution Layers
- [class MPSCNNBinaryConvolution](mpscnnbinaryconvolution.md)
  A convolution kernel with binary weights and an input image using binary approximations.
- [class MPSCNNConvolution](mpscnnconvolution.md)
  A convolution kernel that convolves the input image with a set of filters, with each producing one feature map in the output image.
- [class MPSCNNDepthWiseConvolutionDescriptor](mpscnndepthwiseconvolutiondescriptor.md)
  A description of a convolution object that does depthwise convolution.
- [class MPSCNNSubPixelConvolutionDescriptor](mpscnnsubpixelconvolutiondescriptor.md)
  A description of a convolution object that does subpixel upsampling and reshaping.
- [class MPSCNNConvolutionTranspose](mpscnnconvolutiontranspose.md)
  A transposed convolution kernel.
- [class MPSCNNConvolutionGradient](mpscnnconvolutiongradient.md)
  A gradient convolution kernel.
- [class MPSCNNConvolutionGradientState](mpscnnconvolutiongradientstate.md)
  An object that exposes a gradient convolution kernel’s gradient with respect to weights and biases.
- [protocol MPSImageSizeEncodingState](mpsimagesizeencodingstate.md)
  A protocol for objects that contain information about an image size elsewhere in the graph.
- [class MPSCNNConvolutionWeightsAndBiasesState](mpscnnconvolutionweightsandbiasesstate.md)
  A class that stores weights and biases.
### Pooling Layers
- [class MPSCNNPoolingAverage](mpscnnpoolingaverage.md)
  An average pooling filter.
- [class MPSCNNPoolingAverageGradient](mpscnnpoolingaveragegradient.md)
  A gradient average pooling filter.
- [class MPSCNNPoolingL2Norm](mpscnnpoolingl2norm.md)
  An L2-norm pooling filter.
- [class MPSCNNPoolingMax](mpscnnpoolingmax.md)
  A max pooling filter.
- [class MPSCNNDilatedPoolingMax](mpscnndilatedpoolingmax.md)
  A dilated max pooling filter.
- [class MPSCNNPooling](mpscnnpooling.md)
  A pooling kernel.
- [class MPSCNNPoolingGradient](mpscnnpoolinggradient.md)
  A gradient pooling kernel.
- [class MPSCNNDilatedPoolingMaxGradient](mpscnndilatedpoolingmaxgradient.md)
  A gradient dilated max pooling filter.
- [class MPSCNNPoolingL2NormGradient](mpscnnpoolingl2normgradient.md)
  A gradient L2-norm pooling filter.
- [class MPSCNNPoolingMaxGradient](mpscnnpoolingmaxgradient.md)
  A gradient max pooling filter.
### Fully Connected Layers
- [class MPSCNNBinaryFullyConnected](mpscnnbinaryfullyconnected.md)
  A fully connected convolution layer with binary weights and optionally binarized input image.
- [class MPSCNNFullyConnected](mpscnnfullyconnected.md)
  A fully connected convolution layer, also known as an inner product layer.
- [class MPSCNNFullyConnectedGradient](mpscnnfullyconnectedgradient.md)
  A gradient fully connected convolution layer.
### Neuron Layers
- [class MPSCNNNeuronAbsolute](mpscnnneuronabsolute.md)
  An absolute neuron filter.
- [class MPSCNNNeuronELU](mpscnnneuronelu.md)
  A parametric ELU neuron filter.
- [class MPSCNNNeuronHardSigmoid](mpscnnneuronhardsigmoid.md)
  A hard sigmoid neuron filter.
- [class MPSCNNNeuronLinear](mpscnnneuronlinear.md)
  A linear neuron filter.
- [class MPSCNNNeuronPReLU](mpscnnneuronprelu.md)
  A parametric ReLU (Rectified Linear Unit) neuron filter.
- [class MPSCNNNeuronReLUN](mpscnnneuronrelun.md)
  A ReLUN neuron filter.
- [class MPSCNNNeuronReLU](mpscnnneuronrelu.md)
  A ReLU (Rectified Linear Unit) neuron filter.
- [class MPSCNNNeuronSigmoid](mpscnnneuronsigmoid.md)
  A sigmoid neuron filter.
- [class MPSCNNNeuronSoftPlus](mpscnnneuronsoftplus.md)
  A parametric softplus neuron filter.
- [class MPSCNNNeuronSoftSign](mpscnnneuronsoftsign.md)
  A softsign neuron filter.
- [class MPSCNNNeuronTanH](mpscnnneurontanh.md)
  A hyperbolic tangent neuron filter.
- [class MPSCNNNeuron](mpscnnneuron.md)
  A filter that applies a neuron activation function.
- [class MPSCNNNeuronExponential](mpscnnneuronexponential.md)
  An exponential neuron filter.
- [class MPSCNNNeuronGradient](mpscnnneurongradient.md)
  A gradient neuron filter.
- [class MPSCNNNeuronLogarithm](mpscnnneuronlogarithm.md)
  A logarithm neuron filter.
- [class MPSCNNNeuronPower](mpscnnneuronpower.md)
  A power neuron filter.
- [class MPSNNNeuronDescriptor](mpsnnneurondescriptor.md)
  An object that specifies properties used by a neuron kernel.
### Softmax Layers
- [class MPSCNNSoftMax](mpscnnsoftmax.md)
  A neural transfer function that is useful for classification tasks.
- [class MPSCNNLogSoftMax](mpscnnlogsoftmax.md)
  A neural transfer function that  is useful for constructing a loss function to be minimized when training neural networks.
- [class MPSCNNLogSoftMaxGradient](mpscnnlogsoftmaxgradient.md)
  A gradient logarithmic softmax filter.
- [class MPSCNNSoftMaxGradient](mpscnnsoftmaxgradient.md)
  A gradient softmax filter.
### Normalization Layers
- [class MPSCNNCrossChannelNormalization](mpscnncrosschannelnormalization.md)
  A normalization kernel applied across feature channels.
- [class MPSCNNCrossChannelNormalizationGradient](mpscnncrosschannelnormalizationgradient.md)
  A gradient normalization kernel applied across feature channels.
- [class MPSCNNLocalContrastNormalization](mpscnnlocalcontrastnormalization.md)
  A local-contrast normalization kernel.
- [class MPSCNNLocalContrastNormalizationGradient](mpscnnlocalcontrastnormalizationgradient.md)
  A gradient local-contrast normalization kernel.
- [class MPSCNNSpatialNormalization](mpscnnspatialnormalization.md)
  A spatial normalization kernel.
- [class MPSCNNSpatialNormalizationGradient](mpscnnspatialnormalizationgradient.md)
  A gradient spatial normalization kernel.
- [class MPSCNNBatchNormalization](mpscnnbatchnormalization.md)
  A batch normalization kernel.
- [class MPSCNNBatchNormalizationGradient](mpscnnbatchnormalizationgradient.md)
  A gradient batch normalization kernel.
- [class MPSCNNBatchNormalizationState](mpscnnbatchnormalizationstate.md)
  An object that stores data required to execute batch normalization.
- [class MPSCNNNormalizationMeanAndVarianceState](mpscnnnormalizationmeanandvariancestate.md)
  An object that stores mean and variance terms used to execute batch normalization.
- [class MPSCNNBatchNormalizationStatistics](mpscnnbatchnormalizationstatistics.md)
  An object that stores statistics required to execute batch normalization.
- [class MPSCNNBatchNormalizationStatisticsGradient](mpscnnbatchnormalizationstatisticsgradient.md)
  An object that stores the gradient of the loss function with respect to the batch statistics and batch normalization weights.
- [class MPSCNNInstanceNormalization](mpscnninstancenormalization.md)
  An instance normalization kernel.
- [class MPSCNNInstanceNormalizationGradient](mpscnninstancenormalizationgradient.md)
  A gradient instance normalization kernel.
- [class MPSCNNInstanceNormalizationGradientState](mpscnninstancenormalizationgradientstate.md)
  An object that stores information required to execute a gradient pass for instance normalization.
- [class MPSCNNNormalizationGammaAndBetaState](mpscnnnormalizationgammaandbetastate.md)
  An object that stores gamma and beta terms used to apply a scale and bias in instance- or batch-normalization operations.
### Upsampling Layers
- [class MPSCNNUpsampling](mpscnnupsampling.md)
  A filter that resamples an existing MPS image.
- [class MPSCNNUpsamplingBilinear](mpscnnupsamplingbilinear.md)
  A bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingNearest](mpscnnupsamplingnearest.md)
  A nearest spatial upsampling filter.
- [class MPSCNNUpsamplingBilinearGradient](mpscnnupsamplingbilineargradient.md)
  A gradient bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingGradient](mpscnnupsamplinggradient.md)
  A gradient filter that upsamples an existing Metal Performance Shaders image.
- [class MPSCNNUpsamplingNearestGradient](mpscnnupsamplingnearestgradient.md)
  A gradient upsampling filter that samples the pixel nearest to the source when upsampling to the destination pixel.
### Dropout Layers
- [class MPSCNNDropout](mpscnndropout.md)
  A dropout filter.
- [class MPSCNNDropoutGradient](mpscnndropoutgradient.md)
  A gradient dropout filter.
- [class MPSCNNDropoutGradientState](mpscnndropoutgradientstate.md)
  A class that stores the mask used by dropout and gradient dropout filters.
### Loss Layers
- [class MPSCNNLoss](mpscnnloss.md)
  A kernel that computes the loss and loss gradient between specified predictions and labels.
- [class MPSCNNLossDataDescriptor](mpscnnlossdatadescriptor.md)
  An object that specifies properties used by a loss data descriptor.
- [class MPSCNNLossDescriptor](mpscnnlossdescriptor.md)
  An object that specifies properties used by a loss kernel.
- [class MPSCNNLossLabels](mpscnnlosslabels.md)
  A class that stores the per-element weight buffer used by loss and gradient loss kernels.
- [class MPSCNNYOLOLoss](mpscnnyololoss.md)
  A kernel that computes the YOLO loss and loss gradient between specified predictions and labels.
- [class MPSCNNYOLOLossDescriptor](mpscnnyololossdescriptor.md)
  An object that specifies properties used by a YOLO loss kernel.
### Reduction Layers
- [class MPSNNReduceRowMax](mpsnnreducerowmax.md)
  A reduction filter that returns the maximum value for each row in an image.
- [class MPSNNReduceRowMin](mpsnnreducerowmin.md)
  A reduction filter that returns the minimum value for each row in an image.
- [class MPSNNReduceRowSum](mpsnnreducerowsum.md)
  A reduction filter that returns the sum of all values for each row in an image.
- [class MPSNNReduceRowMean](mpsnnreducerowmean.md)
  A reduction filter that returns the mean value for each row in an image.
- [class MPSNNReduceColumnMax](mpsnnreducecolumnmax.md)
  A reduction filter that returns the maximum value for each column in an image.
- [class MPSNNReduceColumnMin](mpsnnreducecolumnmin.md)
  A reduction filter that returns the minimum value for each column in an image.
- [class MPSNNReduceColumnSum](mpsnnreducecolumnsum.md)
  A reduction filter that returns the sum of all values for each column in an image.
- [class MPSNNReduceColumnMean](mpsnnreducecolumnmean.md)
  A reduction filter that returns the mean value for each column in an image.
- [class MPSNNReduceFeatureChannelsMax](mpsnnreducefeaturechannelsmax.md)
  A reduction filter that returns the maximum value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsMin](mpsnnreducefeaturechannelsmin.md)
  A reduction filter that returns the minimum value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsSum](mpsnnreducefeaturechannelssum.md)
  A reduction filter that returns the sum of all values for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsMean](mpsnnreducefeaturechannelsmean.md)
  A reduction filter that returns the mean value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsArgumentMax](mpsnnreducefeaturechannelsargumentmax.md)
  A reduction filter that returns the index of the location of the maximum value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsArgumentMin](mpsnnreducefeaturechannelsargumentmin.md)
  A reduction filter that returns the index of the location of the minimum value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsAndWeightsSum](mpsnnreducefeaturechannelsandweightssum.md)
  A reduction filter that returns the weighted sum of all values for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsAndWeightsMean](mpsnnreducefeaturechannelsandweightsmean.md)
  A reduction filter that returns the weighted sum for each feature channel in an image.
- [class MPSNNReduceUnary](mpsnnreduceunary.md)
  The base class for unary reduction filters.
- [class MPSNNReduceBinary](mpsnnreducebinary.md)
  The base class for binary reduction filters.
### Reshape Layer
- [class MPSNNReshape](mpsnnreshape.md)
  The base class for reshape operations.
### Slice Layer
- [class MPSNNSlice](mpsnnslice.md)
  A kernel that extracts a slice from an image.
### Optimization Layers
- [class MPSNNOptimizerAdam](mpsnnoptimizeradam.md)
  An optimization layer that performs an Adam pdate.
- [class MPSNNOptimizerRMSProp](mpsnnoptimizerrmsprop.md)
  An optimization layer that performs a root mean square propagation update.
- [class MPSNNOptimizerStochasticGradientDescent](mpsnnoptimizerstochasticgradientdescent.md)
  An optimization layer that performs a gradient descent with an optional momentum update.
- [class MPSNNOptimizer](mpsnnoptimizer.md)
  The base class for optimization layers.
- [class MPSNNOptimizerDescriptor](mpsnnoptimizerdescriptor.md)
  An object that specifies properties used by an optimizer kernel.
### Layer Base Classes
- [class MPSCNNKernel](mpscnnkernel.md)
  Base class for neural network layers.
- [class MPSCNNBinaryKernel](mpscnnbinarykernel.md)
  A convolution neural network kernel.
- [class MPSCNNGradientKernel](mpscnngradientkernel.md)
  The base class for gradient layers.
### Predefined Padding Policies
- [class MPSNNDefaultPadding](mpsnndefaultpadding.md)
  A class that provides predefined padding policies for common tasks.

## See Also

- [Training a Neural Network with Metal Performance Shaders](training-a-neural-network-with-metal-performance-shaders.md)
  Use an MPS neural network graph to train a simple neural network digit classifier.
- [class MPSImage](mpsimage.md)
  A texture that may have more than four channels for use in convolutional neural networks.
- [class MPSTemporaryImage](mpstemporaryimage.md)
  A texture for use in convolutional neural networks that stores transient data to be used and discarded promptly.
- [Objects that Simplify the Creation of Neural Networks](objects-that-simplify-the-creation-of-neural-networks.md)
  Simplify the creation of neural networks using networks of filter, image, and state nodes.
- [Recurrent Neural Networks](recurrent-neural-networks.md)
  Create recurrent neural networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/convolutional-neural-network-kernels)*