# Metal Performance Shaders

**Framework**: Metal Performance Shaders  
**Kind**: module

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

Apps adopting the Metal Performance Shaders framework achieve great performance without needing to create and maintain hand-written shaders for each GPU family. Metal Performance Shaders can be used along with your app’s existing Metal resources (such as the [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer), [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture), and [`MTLBuffer`](https://developer.apple.com/documentation/Metal/MTLBuffer) objects) and shaders.

The Metal Performance Shaders framework supports the following functionality:

- Apply high-performance filters to, and extract statistical and histogram data from images.
- Implement and run neural networks for machine learning training and inference.
- Solve systems of equations, factorize matrices and multiply matrices and vectors.
- Accelerate ray tracing with high-performance ray-geometry intersection testing.

## Topics

### Fundamentals
- [The MPSKernel Class](the-mpskernel-class.md)
- [Tuning Hints](tuning-hints.md)
### Device Support
- [func MPSSupportsMTLDevice((any MTLDevice)?) -> Bool](mpssupportsmtldevice(_:).md)
  Determines whether the Metal Performance Shaders framework supports a Metal device.
### Image Filters
- [Image Filters](image-filters.md)
  Apply high-performance filters to, and extract statistical and histogram data from images.
### Neural Networks
- [Training a Neural Network with Metal Performance Shaders](training-a-neural-network-with-metal-performance-shaders.md)
  Use an MPS neural network graph to train a simple neural network digit classifier.
- [class MPSImage](mpsimage.md)
  A texture that may have more than four channels for use in convolutional neural networks.
- [class MPSTemporaryImage](mpstemporaryimage.md)
  A texture for use in convolutional neural networks that stores transient data to be used and discarded promptly.
- [Objects that Simplify the Creation of Neural Networks](objects-that-simplify-the-creation-of-neural-networks.md)
  Simplify the creation of neural networks using networks of filter, image, and state nodes.
- [Convolutional Neural Network Kernels](convolutional-neural-network-kernels.md)
  Build neural networks with layers.
- [Recurrent Neural Networks](recurrent-neural-networks.md)
  Create recurrent neural networks.
### Matrices and Vectors
- [Matrices and Vectors](matrices-and-vectors.md)
  Solve systems of equations, factorize matrices and multiply matrices and vectors.
### Kernel Base Classes
- [class MPSKernel](mpskernel.md)
  A standard interface for Metal Performance Shaders kernels.
### Keyed Archivers
- [class NSKeyedArchiver](../Foundation/NSKeyedArchiver.md)
  An encoder that stores an object’s data to an archive referenced by keys.
- [class MPSKeyedUnarchiver](mpskeyedunarchiver.md)
  A keyed archiver that supports Metal Performance Shaders kernel decoding.
- [protocol MPSDeviceProvider](mpsdeviceprovider.md)
  An interface that enables the setting of a Metal device for unarchived objects.
### Ray Tracing
- [Accelerating ray tracing and motion blur using Metal](../Metal/accelerating-ray-tracing-and-motion-blur-using-metal.md)
  Generate ray-traced images with motion blur using GPU-based parallel processing.
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
### Articles
- [MetalPerformanceShaders Constants](metalperformanceshaders-constants.md)
- [MetalPerformanceShaders Data Types](metalperformanceshaders-data-types.md)
- [MetalPerformanceShaders Enumerations](metalperformanceshaders-enumerations.md)
- [MetalPerformanceShaders Functions](metalperformanceshaders-functions.md)
- [MetalPerformanceShaders Structures](metalperformanceshaders-structures.md)
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
### Structures
- [struct MPSAccelerationStructureUsage](mpsaccelerationstructureusage.md)
  Options that describe how an acceleration structure will be used.
- [struct MPSAliasingStrategy](mpsaliasingstrategy.md)
- [struct MPSCNNBatchNormalizationFlags](mpscnnbatchnormalizationflags.md)
  Options that define how statistics are calculated during batch normalization.
- [struct MPSCNNConvolutionGradientOption](mpscnnconvolutiongradientoption.md)
  Options that control which gradient to compute during backward propagation.
- [struct MPSCustomKernelArgumentCount](mpscustomkernelargumentcount.md)
  A structure that contains the number of destination, source, and broadcaset textures used by a custom kernel.
- [struct MPSCustomKernelIndex](mpscustomkernelindex.md)
- [struct MPSCustomKernelInfo](mpscustomkernelinfo.md)
- [struct MPSCustomKernelSourceInfo](mpscustomkernelsourceinfo.md)
- [struct MPSDeviceCapsValues](mpsdevicecapsvalues.md)
- [struct MPSDeviceOptions](mpsdeviceoptions.md)
- [struct MPSDimensionSlice](mpsdimensionslice.md)
- [struct MPSImageCoordinate](mpsimagecoordinate.md)
- [struct MPSImageRegion](mpsimageregion.md)
- [struct MPSImageType](mpsimagetype.md)
  Options that define a Metal Performance Shaders image type.
- [struct MPSIntegerDivisionParams](mpsintegerdivisionparams.md)
  Parameters that define the parts of a division operation.
- [struct MPSIntersectionDistance](mpsintersectiondistance.md)
  An intersection result that contains the distance from the ray origin to the intersection point.
- [struct MPSIntersectionDistancePrimitiveIndex](mpsintersectiondistanceprimitiveindex.md)
  An intersection result that contains the distance from the ray origin to the intersection point, and the index of the intersected primitive.
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndex](mpsintersectiondistanceprimitiveindexbufferindex.md)
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndexCoordinates](mpsintersectiondistanceprimitiveindexbufferindexcoordinates.md)
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndex](mpsintersectiondistanceprimitiveindexbufferindexinstanceindex.md)
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndexCoordinates](mpsintersectiondistanceprimitiveindexbufferindexinstanceindexcoordinates.md)
- [struct MPSIntersectionDistancePrimitiveIndexCoordinates](mpsintersectiondistanceprimitiveindexcoordinates.md)
  An intersection result that contains the origin-intersection distance, intersected primitive index, and intersection point coordinates.
- [struct MPSIntersectionDistancePrimitiveIndexInstanceIndex](mpsintersectiondistanceprimitiveindexinstanceindex.md)
  An intersection result that contains the origin-intersection distance, and intersected primitive and instance indices.
- [struct MPSIntersectionDistancePrimitiveIndexInstanceIndexCoordinates](mpsintersectiondistanceprimitiveindexinstanceindexcoordinates.md)
  An intersection result that contains the origin-intersection distance, intersected primitive and instance indices, and intersection point coordinates.
- [struct MPSMatrixCopyOffsets](mpsmatrixcopyoffsets.md)
  A description of matrix copy operations.
- [struct MPSMatrixOffset](mpsmatrixoffset.md)
  A description of row and column offsets into a matrix.
- [struct MPSMatrixRandomDistribution](mpsmatrixrandomdistribution.md)
- [struct MPSNDArrayOffsets](mpsndarrayoffsets.md)
- [struct MPSNDArrayQuantizationScheme](mpsndarrayquantizationscheme.md)
- [struct MPSNDArraySizes](mpsndarraysizes.md)
- [struct MPSNNComparisonType](mpsnncomparisontype.md)
- [struct MPSNNConvolutionAccumulatorPrecisionOption](mpsnnconvolutionaccumulatorprecisionoption.md)
  Options that specify convolution accumulator precision.
- [struct MPSNNTrainingStyle](mpsnntrainingstyle.md)
  Options that control how graph nodes are trained.
- [struct MPSOrigin](mpsorigin.md)
  A position in an image used as the source origin.
- [struct MPSRayMaskOptions](mpsraymaskoptions.md)
  Options for ray intersector mask options.
- [struct MPSRayOriginDirection](mpsrayorigindirection.md)
  A 3D ray with an origin and a direction.
- [struct MPSRayOriginMaskDirectionMaxDistance](mpsrayoriginmaskdirectionmaxdistance.md)
  A 3D ray with an origin, a direction, and a mask to filter out intersections.
- [struct MPSRayOriginMinDistanceDirectionMaxDistance](mpsrayoriginmindistancedirectionmaxdistance.md)
  A 3D ray with an origin, a direction, and an intersection distance range from the origin.
- [struct MPSRayPackedOriginDirection](mpsraypackedorigindirection.md)
- [struct MPSSize](mpssize.md)
  A size of a region in an image.
- [struct MPSStateTextureInfo](mpsstatetextureinfo.md)
  An encapsulation of a texture’s dimensions, format, type, and usage.
### Variables
- [var MPSBatchSizeIndex: Int32](mpsbatchsizeindex.md)
- [var MPSCustomKernelIndexDestIndex: MPSCustomKernelIndex](mpscustomkernelindexdestindex.md)
- [var MPSCustomKernelIndexSrc0Index: MPSCustomKernelIndex](mpscustomkernelindexsrc0index.md)
- [var MPSCustomKernelIndexSrc1Index: MPSCustomKernelIndex](mpscustomkernelindexsrc1index.md)
- [var MPSCustomKernelIndexSrc2Index: MPSCustomKernelIndex](mpscustomkernelindexsrc2index.md)
- [var MPSCustomKernelIndexSrc3Index: MPSCustomKernelIndex](mpscustomkernelindexsrc3index.md)
- [var MPSCustomKernelIndexSrc4Index: MPSCustomKernelIndex](mpscustomkernelindexsrc4index.md)
- [var MPSCustomKernelIndexUserDataIndex: MPSCustomKernelIndex](mpscustomkernelindexuserdataindex.md)
- [var MPSDeviceCapsIndex: Int32](mpsdevicecapsindex.md)
- [var MPSDeviceCapsLast: MPSDeviceCapsValues](mpsdevicecapslast.md)
- [var MPSDeviceCapsNull: MPSDeviceCapsValues](mpsdevicecapsnull.md)
- [var MPSDeviceIsAppleDevice: MPSDeviceCapsValues](mpsdeviceisappledevice.md)
- [var MPSDeviceSupportsBFloat16Arithmetic: MPSDeviceCapsValues](mpsdevicesupportsbfloat16arithmetic.md)
- [var MPSDeviceSupportsFloat16BicubicFiltering: MPSDeviceCapsValues](mpsdevicesupportsfloat16bicubicfiltering.md)
- [var MPSDeviceSupportsFloat32Filtering: MPSDeviceCapsValues](mpsdevicesupportsfloat32filtering.md)
- [var MPSDeviceSupportsNorm16BicubicFiltering: MPSDeviceCapsValues](mpsdevicesupportsnorm16bicubicfiltering.md)
- [var MPSDeviceSupportsQuadShuffle: MPSDeviceCapsValues](mpsdevicesupportsquadshuffle.md)
- [var MPSDeviceSupportsReadWriteTextures: MPSDeviceCapsValues](mpsdevicesupportsreadwritetextures.md)
- [var MPSDeviceSupportsReadableArrayOfTextures: MPSDeviceCapsValues](mpsdevicesupportsreadablearrayoftextures.md)
- [var MPSDeviceSupportsSimdReduction: MPSDeviceCapsValues](mpsdevicesupportssimdreduction.md)
- [var MPSDeviceSupportsSimdShuffle: MPSDeviceCapsValues](mpsdevicesupportssimdshuffle.md)
- [var MPSDeviceSupportsSimdShuffleAndFill: MPSDeviceCapsValues](mpsdevicesupportssimdshuffleandfill.md)
- [var MPSDeviceSupportsSimdgroupBarrier: MPSDeviceCapsValues](mpsdevicesupportssimdgroupbarrier.md)
- [var MPSDeviceSupportsWritableArrayOfTextures: MPSDeviceCapsValues](mpsdevicesupportswritablearrayoftextures.md)
- [var MPSFunctionConstantIndex: Int32](mpsfunctionconstantindex.md)
- [var MPSFunctionConstantIndexReserved: Int32](mpsfunctionconstantindexreserved.md)
- [let MPSFunctionConstantNone: MPSFunctionConstant](mpsfunctionconstantnone.md)
- [let MPSFunctionConstantNoneArray: (MPSFunctionConstant, MPSFunctionConstant)](mpsfunctionconstantnonearray.md)
- [var MPSImageType2d: MPSImageType](mpsimagetype2d.md)
- [var MPSImageType2d_array: MPSImageType](mpsimagetype2d_array.md)
- [var MPSImageType2d_array_noAlpha: MPSImageType](mpsimagetype2d_array_noalpha.md)
- [var MPSImageType2d_noAlpha: MPSImageType](mpsimagetype2d_noalpha.md)
- [var MPSImageTypeArray2d: MPSImageType](mpsimagetypearray2d.md)
- [var MPSImageTypeArray2d_array: MPSImageType](mpsimagetypearray2d_array.md)
- [var MPSImageTypeArray2d_array_noAlpha: MPSImageType](mpsimagetypearray2d_array_noalpha.md)
- [var MPSImageTypeArray2d_noAlpha: MPSImageType](mpsimagetypearray2d_noalpha.md)
- [var MPSImageType_ArrayMask: MPSImageType](mpsimagetype_arraymask.md)
- [var MPSImageType_BatchMask: MPSImageType](mpsimagetype_batchmask.md)
- [var MPSImageType_bitCount: MPSImageType](mpsimagetype_bitcount.md)
- [var MPSImageType_mask: MPSImageType](mpsimagetype_mask.md)
- [var MPSImageType_noAlpha: MPSImageType](mpsimagetype_noalpha.md)
- [var MPSImageType_texelFormatBFloat16: MPSImageType](mpsimagetype_texelformatbfloat16.md)
- [var MPSImageType_texelFormatFloat16: MPSImageType](mpsimagetype_texelformatfloat16.md)
- [var MPSImageType_texelFormatMask: MPSImageType](mpsimagetype_texelformatmask.md)
- [var MPSImageType_texelFormatShift: MPSImageType](mpsimagetype_texelformatshift.md)
- [var MPSImageType_texelFormatStandard: MPSImageType](mpsimagetype_texelformatstandard.md)
- [var MPSImageType_texelFormatUnorm8: MPSImageType](mpsimagetype_texelformatunorm8.md)
- [var MPSImageType_typeMask: MPSImageType](mpsimagetype_typemask.md)
- [var MPSNDArrayConstantIndex: Int32](mpsndarrayconstantindex.md)
- [var MPSNDArrayConstantMultiDestDstAddressingIndex: Int32](mpsndarrayconstantmultidestdstaddressingindex.md)
- [var MPSNDArrayConstantMultiDestIndex: Int32](mpsndarrayconstantmultidestindex.md)
- [var MPSNDArrayConstantMultiDestIndex0: Int32](mpsndarrayconstantmultidestindex0.md)
- [var MPSNDArrayConstantMultiDestIndex1: Int32](mpsndarrayconstantmultidestindex1.md)
- [var MPSNDArrayConstantMultiDestSrcAddressingIndex: Int32](mpsndarrayconstantmultidestsrcaddressingindex.md)
- [var MPSTextureLinkingConstantIndex: Int32](mpstexturelinkingconstantindex.md)
- [var MPSUserAvailableFunctionConstantStartIndex: Int32](mpsuseravailablefunctionconstantstartindex.md)
- [var MPSUserConstantIndex: Int32](mpsuserconstantindex.md)
### Functions
- [func MPSDataTypeBitsCount(MPSDataType) -> Int](mpsdatatypebitscount(_:).md)
- [func MPSFindIntegerDivisionParams(UInt16) -> MPSIntegerDivisionParams](mpsfindintegerdivisionparams(_:).md)
  Returns the integer division parameters for a specified divisor.
- [func MPSGetCustomKernelBatchedDestinationIndex(MPSCustomKernelArgumentCount) -> UInt](mpsgetcustomkernelbatcheddestinationindex(_:).md)
  Returns the index of the first destination texture argument.
- [func MPSGetCustomKernelBatchedSourceIndex(MPSCustomKernelArgumentCount, UInt, UInt) -> UInt](mpsgetcustomkernelbatchedsourceindex(_:_:_:).md)
  Returns the index of the specified batched source texture argument.
- [func MPSGetCustomKernelBroadcastSourceIndex(MPSCustomKernelArgumentCount, UInt, UInt) -> UInt](mpsgetcustomkernelbroadcastsourceindex(_:_:_:).md)
  Returns the index of the specified nonbatched source texture argument.
- [func MPSGetCustomKernelMaxBatchSize(MPSCustomKernelArgumentCount, UInt) -> UInt](mpsgetcustomkernelmaxbatchsize(_:_:).md)
  Returns the maximum allowed batch size.
- [func MPSGetImageType(MPSImage) -> MPSImageType](mpsgetimagetype(_:).md)
- [func MPSGetPreferredDevice(MPSDeviceOptions) -> (any MTLDevice)?](mpsgetpreferreddevice(_:).md)
- [func MPSHintTemporaryMemoryHighWaterMark(any MTLCommandBuffer, Int)](mpshinttemporarymemoryhighwatermark(_:_:).md)
  Triggers Metal Performance Shaders to prefetch a Metal heap of the indicated size into its internal cache.
- [func MPSImageBatchIncrementReadCount([MPSImage], Int) -> Int](mpsimagebatchincrementreadcount(_:_:).md)
  Increments or decrements the read count of an image batch by a specified amount.
- [func MPSImageBatchIterate([MPSImage], (MPSImage, Int) -> Int) -> Int](mpsimagebatchiterate(_:_:).md)
  Executes a callback block once for each unique image in a batch.
- [func MPSImageBatchResourceSize([MPSImage]) -> Int](mpsimagebatchresourcesize(_:).md)
  Returns the number of bytes used to allocate the specified image batch.
- [func MPSImageBatchSynchronize([MPSImage], any MTLCommandBuffer)](mpsimagebatchsynchronize(_:_:).md)
  Removes any copy of the specified image batch from the device’s caches, and, if needed, invalidates any CPU caches.
- [func MPSSetHeapCacheDuration(any MTLCommandBuffer, Double)](mpssetheapcacheduration(_:_:).md)
  Sets the timeout after which unused cached Metal heaps are released.
- [func MPSSizeofMPSDataType(MPSDataType) -> Int](mpssizeofmpsdatatype(_:).md)
- [func MPSStateBatchIncrementReadCount([MPSState]?, Int) -> Int](mpsstatebatchincrementreadcount(_:_:).md)
  Increments or decrements the read count of a state batch by a specified amount.
- [func MPSStateBatchResourceSize([MPSState]?) -> Int](mpsstatebatchresourcesize(_:).md)
  Returns the number of bytes used to allocate the specified state batch.
- [func MPSStateBatchSynchronize([MPSState], any MTLCommandBuffer)](mpsstatebatchsynchronize(_:_:).md)
  Removes any copy of the specified state batch from the device’s caches, and, if needed, invalidates any CPU caches.
### Type Aliases
- [typealias MPSAccelerationStructureCompletionHandler](mpsaccelerationstructurecompletionhandler.md)
  A block of code that’s invoked when an operation on an acceleration structure has completed.
- [typealias MPSAxisAlignedBoundingBox](mpsaxisalignedboundingbox-swift.typealias.md)
  An axis-aligned bounding box.
- [typealias MPSDeviceCaps](mpsdevicecaps.md)
- [typealias MPSFunctionConstant](mpsfunctionconstant.md)
- [typealias MPSFunctionConstantInMetal](mpsfunctionconstantinmetal.md)
- [typealias MPSGradientNodeBlock](mpsgradientnodeblock.md)
- [typealias MPSPackedFloat3](mpspackedfloat3-swift.typealias.md)
  A packed three-element vector.
### Enumerations
- [enum MPSAccelerationStructureStatus](mpsaccelerationstructurestatus.md)
  Constants that indicate an acceleration structure build state.
- [enum MPSBoundingBoxIntersectionTestType](mpsboundingboxintersectiontesttype.md)
  Options for the intersection test type for a ray intersector bounding box.
- [enum MPSCNNConvolutionWeightsLayout](mpscnnconvolutionweightslayout.md)
- [enum MPSCNNLossType](mpscnnlosstype.md)
  Constants that indicate supported loss filter types.
- [enum MPSCNNReductionType](mpscnnreductiontype.md)
  Constants that indicate supported reduction types.
- [enum MPSCNNWeightsQuantizationType](mpscnnweightsquantizationtype.md)
  Options that specify the type of quantization used to generate unsigned integer weights.
- [enum MPSFloatDataTypeBit](mpsfloatdatatypebit.md)
- [enum MPSFloatDataTypeShift](mpsfloatdatatypeshift.md)
- [enum MPSIntersectionDataType](mpsintersectiondatatype.md)
  Options that determine the data contained in an intersection result.
- [enum MPSIntersectionType](mpsintersectiontype.md)
  Options that determine an intersection type for a ray intersector.
- [enum MPSNNRegularizationType](mpsnnregularizationtype.md)
- [enum MPSPolygonType](mpspolygontype.md)
- [enum MPSRNNMatrixId](mpsrnnmatrixid.md)
  Options that define which matrix is copied in or out of a trainable RNN layer.
- [enum MPSRayDataType](mpsraydatatype.md)
  Options for the data type for an intersector ray.
- [enum MPSRayMaskOperator](mpsraymaskoperator.md)
- [enum MPSStateResourceType](mpsstateresourcetype.md)
  Options for the underlying resource type for a state object.
- [enum MPSTemporalWeighting](mpstemporalweighting.md)
- [enum MPSTransformType](mpstransformtype.md)
  Constants that indicate instance transformation types.
- [enum MPSTriangleIntersectionTestType](mpstriangleintersectiontesttype.md)
  Options for the ray-triangle intersection test.

## See Also

- [Metal](../Metal/Metal.md)
  Render advanced 3D graphics and compute data in parallel with graphics processors.
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders)*