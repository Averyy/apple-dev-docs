# Metal Performance Shaders

**Framework**: Metal Performance Shaders

Optimize graphics and compute performance with kernels that are fine-tuned for the unique characteristics of each Metal GPU family.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

#### Overview

The Metal Performance Shaders framework contains a collection of highly optimized compute and graphics shaders that are designed to integrate easily and efficiently into your Metal app. These data-parallel primitives are specially tuned to take advantage of the unique hardware characteristics of each GPU family to ensure optimal performance.

Apps adopting the Metal Performance Shaders framework achieve great performance without needing to create and maintain hand-written shaders for each GPU family. Metal Performance Shaders can be used along with your app’s existing Metal resources (such as the [`MTLCommandBuffer`](https://developer.apple.com/documentation/metal/mtlcommandbuffer), [`MTLTexture`](https://developer.apple.com/documentation/metal/mtltexture), and [`MTLBuffer`](https://developer.apple.com/documentation/metal/mtlbuffer) objects) and shaders.

The Metal Performance Shaders framework supports the following functionality:

- Apply high-performance filters to, and extract statistical and histogram data from images.
- Implement and run neural networks for machine learning training and inference.
- Solve systems of equations, factorize matrices and multiply matrices and vectors.
- Accelerate ray tracing with high-performance ray-geometry intersection testing.

## Topics

### Fundamentals
- [The MPSKernel Class](the_mpskernel_class.md)
- [Tuning Hints](tuning_hints.md)
### Device Support
- [func MPSSupportsMTLDevice((any MTLDevice)?) -> Bool](1618849-mpssupportsmtldevice.md)
  Determines whether the Metal Performance Shaders framework supports a Metal device.
### Image Filters
- [Image Filters](image_filters.md)
  Apply high-performance filters to, and extract statistical and histogram data from images.
### Neural Networks
- [Training a Neural Network with Metal Performance Shaders](training_a_neural_network_with_metal_performance_shaders.md)
  Use an MPS neural network graph to train a simple neural network digit classifier.
- [class MPSImage](mpsimage.md)
  A texture that may have more than four channels for use in convolutional neural networks.
- [class MPSTemporaryImage](mpstemporaryimage.md)
  A texture for use in convolutional neural networks that stores transient data to be used and discarded promptly.
- [Objects that Simplify the Creation of Neural Networks](objects_that_simplify_the_creation_of_neural_networks.md)
  Simplify the creation of neural networks using networks of filter, image, and state nodes.
- [Convolutional Neural Network Kernels](convolutional_neural_network_kernels.md)
  Build neural networks with layers.
- [Recurrent Neural Networks](recurrent_neural_networks.md)
  Create recurrent neural networks.
### Matrices and Vectors
- [Matrices and Vectors](matrices_and_vectors.md)
  Solve systems of equations, factorize matrices and multiply matrices and vectors.
### Kernel Base Classes
- [class MPSKernel](mpskernel.md)
  A standard interface for Metal Performance Shaders kernels.
### Keyed Archivers
- [class NSKeyedArchiver](../foundation/nskeyedarchiver.md)
  An encoder that stores an object’s data to an archive referenced by keys.
- [class MPSKeyedUnarchiver](mpskeyedunarchiver.md)
  A keyed archiver that supports Metal Performance Shaders kernel decoding.
- [protocol MPSDeviceProvider](mpsdeviceprovider.md)
  An interface that enables the setting of a Metal device for unarchived objects.
### Ray Tracing
- [Animating and Denoising a Raytraced Scene](animating_and_denoising_a_raytraced_scene.md)
  Support dynamic scenes and denoising by extending your ray tracer with Metal Performance Shaders.
- [class MPSRayIntersector](mpsrayintersector.md)
  A kernel that performs intersection tests between rays and geometry.
- [class MPSAccelerationStructureGroup](mpsaccelerationstructuregroup.md)
  A group of acceleration structures.
- [class MPSInstanceAccelerationStructure](mpsinstanceaccelerationstructure.md)
  An acceleration structure built over instances of other acceleration structures.
- [class MPSTriangleAccelerationStructure](mpstriangleaccelerationstructure.md)
  An acceleration structure built over triangles.
- [class MPSAccelerationStructure](mpsaccelerationstructure.md)
  The base class for data structures that are built over geometry and used to accelerate ray tracing.
### Classes
- [class MPSCNNConvolutionTransposeGradient](mpscnnconvolutiontransposegradient.md)
- [class MPSCNNConvolutionTransposeGradientNode](mpscnnconvolutiontransposegradientnode.md)
- [class MPSCNNConvolutionTransposeGradientState](mpscnnconvolutiontransposegradientstate.md)
- [class MPSCNNConvolutionTransposeGradientStateNode](mpscnnconvolutiontransposegradientstatenode.md)
- [class MPSCNNFullyConnectedGradientNode](mpscnnfullyconnectedgradientnode.md)
- [class MPSCNNGroupNormalization](mpscnngroupnormalization.md)
- [class MPSCNNGroupNormalizationGradient](mpscnngroupnormalizationgradient.md)
- [class MPSCNNGroupNormalizationGradientNode](mpscnngroupnormalizationgradientnode.md)
- [class MPSCNNGroupNormalizationGradientState](mpscnngroupnormalizationgradientstate.md)
- [class MPSCNNGroupNormalizationNode](mpscnngroupnormalizationnode.md)
- [class MPSCNNMultiaryKernel](mpscnnmultiarykernel.md)
- [class MPSCNNNeuronGeLUNode](mpscnnneurongelunode.md)
- [class MPSCommandBuffer](mpscommandbuffer.md)
- [class MPSImageCanny](mpsimagecanny.md)
- [class MPSImageEDLines](mpsimageedlines.md)
- [class MPSImageNormalizedHistogram](mpsimagenormalizedhistogram.md)
  A filter that computes the normalized histogram of an image.
- [class MPSMatrixRandom](mpsmatrixrandom.md)
- [class MPSMatrixRandomDistributionDescriptor](mpsmatrixrandomdistributiondescriptor.md)
- [class MPSMatrixRandomMTGP32](mpsmatrixrandommtgp32.md)
- [class MPSMatrixRandomPhilox](mpsmatrixrandomphilox.md)
- [class MPSNDArray](mpsndarray.md)
- [class MPSNDArrayAffineInt4Dequantize](mpsndarrayaffineint4dequantize.md)
- [class MPSNDArrayAffineQuantizationDescriptor](mpsndarrayaffinequantizationdescriptor.md)
- [class MPSNDArrayBinaryKernel](mpsndarraybinarykernel.md)
- [class MPSNDArrayBinaryPrimaryGradientKernel](mpsndarraybinaryprimarygradientkernel.md)
- [class MPSNDArrayBinarySecondaryGradientKernel](mpsndarraybinarysecondarygradientkernel.md)
- [class MPSNDArrayDescriptor](mpsndarraydescriptor.md)
- [class MPSNDArrayGather](mpsndarraygather.md)
- [class MPSNDArrayGatherGradient](mpsndarraygathergradient.md)
- [class MPSNDArrayGatherGradientState](mpsndarraygathergradientstate.md)
- [class MPSNDArrayGradientState](mpsndarraygradientstate.md)
- [class MPSNDArrayIdentity](mpsndarrayidentity.md)
- [class MPSNDArrayLUTDequantize](mpsndarraylutdequantize.md)
- [class MPSNDArrayLUTQuantizationDescriptor](mpsndarraylutquantizationdescriptor.md)
- [class MPSNDArrayMatrixMultiplication](mpsndarraymatrixmultiplication.md)
- [class MPSNDArrayMultiaryBase](mpsndarraymultiarybase.md)
- [class MPSNDArrayMultiaryGradientKernel](mpsndarraymultiarygradientkernel.md)
- [class MPSNDArrayMultiaryKernel](mpsndarraymultiarykernel.md)
- [class MPSNDArrayQuantizationDescriptor](mpsndarrayquantizationdescriptor.md)
- [class MPSNDArrayQuantizedMatrixMultiplication](mpsndarrayquantizedmatrixmultiplication.md)
- [class MPSNDArrayStridedSlice](mpsndarraystridedslice.md)
- [class MPSNDArrayStridedSliceGradient](mpsndarraystridedslicegradient.md)
- [class MPSNDArrayUnaryGradientKernel](mpsndarrayunarygradientkernel.md)
- [class MPSNDArrayUnaryKernel](mpsndarrayunarykernel.md)
- [class MPSNDArrayVectorLUTDequantize](mpsndarrayvectorlutdequantize.md)
- [class MPSNNCompare](mpsnncompare.md)
- [class MPSNNComparisonNode](mpsnncomparisonnode.md)
- [class MPSNNCropAndResizeBilinear](mpsnncropandresizebilinear.md)
  A cropping and bilinear resizing filter.
- [class MPSNNForwardLoss](mpsnnforwardloss.md)
- [class MPSNNForwardLossNode](mpsnnforwardlossnode.md)
- [class MPSNNGramMatrixCalculation](mpsnngrammatrixcalculation.md)
- [class MPSNNGramMatrixCalculationGradient](mpsnngrammatrixcalculationgradient.md)
- [class MPSNNGramMatrixCalculationGradientNode](mpsnngrammatrixcalculationgradientnode.md)
- [class MPSNNGramMatrixCalculationNode](mpsnngrammatrixcalculationnode.md)
- [class MPSNNGridSample](mpsnngridsample.md)
- [class MPSNNInitialGradient](mpsnninitialgradient.md)
- [class MPSNNInitialGradientNode](mpsnninitialgradientnode.md)
- [class MPSNNLocalCorrelation](mpsnnlocalcorrelation.md)
- [class MPSNNLossGradient](mpsnnlossgradient.md)
- [class MPSNNLossGradientNode](mpsnnlossgradientnode.md)
- [class MPSNNMultiaryGradientState](mpsnnmultiarygradientstate.md)
- [class MPSNNMultiaryGradientStateNode](mpsnnmultiarygradientstatenode.md)
- [class MPSNNPad](mpsnnpad.md)
- [class MPSNNPadGradient](mpsnnpadgradient.md)
- [class MPSNNPadGradientNode](mpsnnpadgradientnode.md)
- [class MPSNNPadNode](mpsnnpadnode.md)
- [class MPSNNReductionColumnMaxNode](mpsnnreductioncolumnmaxnode.md)
- [class MPSNNReductionColumnMeanNode](mpsnnreductioncolumnmeannode.md)
- [class MPSNNReductionColumnMinNode](mpsnnreductioncolumnminnode.md)
- [class MPSNNReductionColumnSumNode](mpsnnreductioncolumnsumnode.md)
- [class MPSNNReductionFeatureChannelsArgumentMaxNode](mpsnnreductionfeaturechannelsargumentmaxnode.md)
- [class MPSNNReductionFeatureChannelsArgumentMinNode](mpsnnreductionfeaturechannelsargumentminnode.md)
- [class MPSNNReductionFeatureChannelsMaxNode](mpsnnreductionfeaturechannelsmaxnode.md)
- [class MPSNNReductionFeatureChannelsMeanNode](mpsnnreductionfeaturechannelsmeannode.md)
- [class MPSNNReductionFeatureChannelsMinNode](mpsnnreductionfeaturechannelsminnode.md)
- [class MPSNNReductionFeatureChannelsSumNode](mpsnnreductionfeaturechannelssumnode.md)
- [class MPSNNReductionRowMaxNode](mpsnnreductionrowmaxnode.md)
- [class MPSNNReductionRowMeanNode](mpsnnreductionrowmeannode.md)
- [class MPSNNReductionRowMinNode](mpsnnreductionrowminnode.md)
- [class MPSNNReductionRowSumNode](mpsnnreductionrowsumnode.md)
- [class MPSNNReductionSpatialMeanGradientNode](mpsnnreductionspatialmeangradientnode.md)
- [class MPSNNReductionSpatialMeanNode](mpsnnreductionspatialmeannode.md)
- [class MPSNNReshapeGradient](mpsnnreshapegradient.md)
- [class MPSNNReshapeGradientNode](mpsnnreshapegradientnode.md)
- [class MPSNNReshapeNode](mpsnnreshapenode.md)
- [class MPSNNResizeBilinear](mpsnnresizebilinear.md)
  A bilinear resizing filter.
- [class MPSNNUnaryReductionNode](mpsnnunaryreductionnode.md)
- [class MPSPolygonAccelerationStructure](mpspolygonaccelerationstructure.md)
- [class MPSPolygonBuffer](mpspolygonbuffer.md)
- [class MPSPredicate](mpspredicate.md)
- [class MPSQuadrilateralAccelerationStructure](mpsquadrilateralaccelerationstructure.md)
- [class MPSSVGF](mpssvgf.md)
- [class MPSSVGFDefaultTextureAllocator](mpssvgfdefaulttextureallocator.md)
- [class MPSSVGFDenoiser](mpssvgfdenoiser.md)
- [class MPSStateResourceList](mpsstateresourcelist.md)
  An interface for objects that define resources for Metal Performance Shaders state containers.
- [class MPSTemporalAA](mpstemporalaa.md)
- [class MPSTemporaryNDArray](mpstemporaryndarray.md)
### Protocols
- [protocol MPSCNNGroupNormalizationDataSource](mpscnngroupnormalizationdatasource.md)
- [protocol MPSHeapProvider](mpsheapprovider.md)
- [protocol MPSNDArrayAllocator](mpsndarrayallocator.md)
- [protocol MPSNNGramMatrixCallback](mpsnngrammatrixcallback.md)
- [protocol MPSNNLossCallback](mpsnnlosscallback.md)
- [protocol MPSSVGFTextureAllocator](mpssvgftextureallocator.md)
### Reference
- [MetalPerformanceShaders Structures](metalperformanceshaders_structures.md)
- [MetalPerformanceShaders Enumerations](metalperformanceshaders_enumerations.md)
- [MetalPerformanceShaders Constants](metalperformanceshaders_constants.md)
- [MetalPerformanceShaders Functions](metalperformanceshaders_functions.md)
- [MetalPerformanceShaders Data Types](metalperformanceshaders_data_types.md)

## See Also

- [Metal](../metal/metal.md)
  Render advanced 3D graphics and compute data in parallel with graphics processors.
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders)*