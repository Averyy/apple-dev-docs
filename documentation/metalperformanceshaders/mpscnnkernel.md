# MPSCNNKernel

**Framework**: Metal Performance Shaders  
**Kind**: class

Base class for neural network layers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNKernel
```

#### Overview

An [`MPSCNNKernel`](mpscnnkernel.md) object consumes one [`MPSImage`](mpsimage.md) object and produces one [`MPSImage`](mpsimage.md) object.

The region overwritten in the destination image is described by the [`clipRect`](mpscnnkernel/cliprect.md) property.  The top left corner of the region consumed (ignoring adjustments for filter size—for example, convolution filter size) is given by the [`offset`](mpscnnkernel/offset.md) property. The size of the region consumed is a function of the size of the [`clipRect`](mpscnnkernel/cliprect.md) property and any subsampling caused by pixel strides at work (for example, [`strideInPixelsX`](mpscnnkernel/strideinpixelsx.md)/[`strideInPixelsY`](mpscnnkernel/strideinpixelsy.md) in the [`MPSCNNPooling`](mpscnnpooling.md) class).  Wherever the [`offset`](mpscnnkernel/offset.md) and [`clipRect`](mpscnnkernel/cliprect.md) properties would cause an `{x,y}` pixel address not in the image to be read, the [`edgeMode`](mpscnnkernel/edgemode.md) property is used to determine what value to read there.

The `z` or `depth` component of the [`offset`](mpscnnkernel/offset.md), [`origin`](https://developer.apple.com/documentation/Metal/MTLRegion/origin) and [`size`](mpsregion/size.md) properties indexes which images to use.

- If the [`MPSImage`](mpsimage.md) object contains only a single image, then these values should be `offset.z = 0`, `clipRect.origin.z = 0`, and `clipRect.size.depth = 1`.
- If the [`MPSImage`](mpsimage.md) object contains multiple images, then the value of `clipRect.size.depth` determines the number of images to process. Both the source and destination [`MPSImage`](mpsimage.md) objects must have at least this many images. The value of `offset.z` refers to the starting image index of the source. Thus, the value of `offset.z + clipRect.size.depth` must be `<=source.numberOfImages`. Similarly, the value of `clipRect.origin.z` determines the starting image index of the destination. Thus, the value of `clipRect.origin.z + clipRect.size.depth` must be `<=destination.numberOfImages`.

The [`destinationFeatureChannelOffset`](mpscnnkernel/destinationfeaturechanneloffset.md) property can be used to control where the kernel will start writing in terms of feature channel dimension. For example, if the destination has 64 channels and th[`destinationFeatureChannelOffset`](mpscnnkernel/destinationfeaturechanneloffset.md)e kernel outputs 32 channels, channels 0-31 of the destination will be populated by the kernel (by default). But if you want the kernel to populate channels 32-63 of the destination, you can set the value of [`destinationFeatureChannelOffset`](mpscnnkernel/destinationfeaturechanneloffset.md) to 32. Suppose you have a source of dimensions `w x h x Ni`, where `N` is the number of channels, which goes through a convolution filter `C0` which produces the output `O0 = w x h x N0` and `C`1 which produces the output `O1 = w x h x N1` followed by concatenation which produces `O = w x h x (N0 + N1)`. You can achieve this by creating an [`MPSImage`](mpsimage.md) object with dimensions `w x h x (N0 + N1)` and using this as the destination of both convolutions as follows:

- `C0: destinationFeatureChannelOffset = 0`, this will output `N0` channels starting at channel `0` of destination thus populating `[0,N0-1]` channels.
- `C1: destinationFeatureChannelOffset = N0`, this will output `N1` channels starting at channel `N0` of destination thus populating `[N0,N0+N1-1]` channels.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnkernel/init(coder:device:).md)
- [init(device: any MTLDevice)](mpscnnkernel/init(device:).md)
### Instance Properties
- [var offset: MPSOffset](mpscnnkernel/offset.md)
  The position of the destination image’s clip rectangle origin, relative to the source image.
- [struct MPSOffset](mpsoffset.md)
  A signed coordinate with x, y, and z components.
- [var clipRect: MTLRegion](mpscnnkernel/cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the clip rectangle will be overwritten.
- [struct MTLRegion](../Metal/MTLRegion.md)
  The bounds for a subset of an object’s elements.
- [var destinationFeatureChannelOffset: Int](mpscnnkernel/destinationfeaturechanneloffset.md)
  The number of channels in the destination image to skip before writing output data.
- [var edgeMode: MPSImageEdgeMode](mpscnnkernel/edgemode.md)
  The edge mode to use when texture reads stray off the edge of an image.
- [enum MPSImageEdgeMode](mpsimageedgemode.md)
  The options used to control the edge behavior of an image filter when it reads outside the bounds of a source texture.
- [var kernelHeight: Int](mpscnnkernel/kernelheight.md)
- [var kernelWidth: Int](mpscnnkernel/kernelwidth.md)
- [var strideInPixelsX: Int](mpscnnkernel/strideinpixelsx.md)
- [var strideInPixelsY: Int](mpscnnkernel/strideinpixelsy.md)
- [var isBackwards: Bool](mpscnnkernel/isbackwards.md)
- [var padding: any MPSNNPadding](mpscnnkernel/padding.md)
- [protocol MPSNNPadding](mpsnnpadding.md)
  The protocol that provides a description of how kernels should pad images.
- [var destinationImageAllocator: any MPSImageAllocator](mpscnnkernel/destinationimageallocator.md)
- [protocol MPSImageAllocator](mpsimageallocator.md)
- [var dilationRateX: Int](mpscnnkernel/dilationratex.md)
- [var dilationRateY: Int](mpscnnkernel/dilationratey.md)
- [var isStateModified: Bool](mpscnnkernel/isstatemodified.md)
- [var sourceFeatureChannelMaxCount: Int](mpscnnkernel/sourcefeaturechannelmaxcount.md)
- [var sourceFeatureChannelOffset: Int](mpscnnkernel/sourcefeaturechanneloffset.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage) -> MPSImage](mpscnnkernel/encode(commandbuffer:sourceimage:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationImage: MPSImage)](mpscnnkernel/encode(commandbuffer:sourceimage:destinationimage:).md)
  Encodes a kernel into a command buffer.  The ensuing operation proceeds out-of-place.
- [func appendBatchBarrier() -> Bool](mpscnnkernel/appendbatchbarrier.md)
- [func batchEncodingStorageSize(sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]?) -> Int](mpscnnkernel/batchencodingstoragesize(sourceimage:sourcestates:destinationimage:).md)
- [func destinationImageDescriptor(sourceImages: [MPSImage], sourceStates: [MPSState]?) -> MPSImageDescriptor](mpscnnkernel/destinationimagedescriptor(sourceimages:sourcestates:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationState: MPSState, destinationImage: MPSImage)](mpscnnkernel/encode(commandbuffer:sourceimage:destinationstate:destinationimage:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool) -> MPSImage](mpscnnkernel/encode(commandbuffer:sourceimage:destinationstate:destinationstateistemporary:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage]) -> [MPSImage]](mpscnnkernel/encodebatch(commandbuffer:sourceimages:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationImages: [MPSImage])](mpscnnkernel/encodebatch(commandbuffer:sourceimages:destinationimages:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationStates: [MPSState]?, destinationImages: [MPSImage])](mpscnnkernel/encodebatch(commandbuffer:sourceimages:destinationstates:destinationimages:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool) -> [MPSImage]](mpscnnkernel/encodebatch(commandbuffer:sourceimages:destinationstates:destinationstateistemporary:).md)
- [func encodingStorageSize(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage?) -> Int](mpscnnkernel/encodingstoragesize(sourceimage:sourcestates:destinationimage:).md)
- [func isResultStateReusedAcrossBatch() -> Bool](mpscnnkernel/isresultstatereusedacrossbatch.md)
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnkernel/resultstate(sourceimage:sourcestates:destinationimage:).md)
- [func resultStateBatch(sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnkernel/resultstatebatch(sourceimage:sourcestates:destinationimage:).md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnkernel/temporaryresultstate(commandbuffer:sourceimage:sourcestates:destinationimage:).md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnkernel/temporaryresultstatebatch(commandbuffer:sourceimage:sourcestates:destinationimage:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Inherited By
- [MPSCNNBatchNormalization](mpscnnbatchnormalization.md)
- [MPSCNNBatchNormalizationStatistics](mpscnnbatchnormalizationstatistics.md)
- [MPSCNNBinaryConvolution](mpscnnbinaryconvolution.md)
- [MPSCNNConvolution](mpscnnconvolution.md)
- [MPSCNNConvolutionTranspose](mpscnnconvolutiontranspose.md)
- [MPSCNNCrossChannelNormalization](mpscnncrosschannelnormalization.md)
- [MPSCNNDropout](mpscnndropout.md)
- [MPSCNNGroupNormalization](mpscnngroupnormalization.md)
- [MPSCNNInstanceNormalization](mpscnninstancenormalization.md)
- [MPSCNNLocalContrastNormalization](mpscnnlocalcontrastnormalization.md)
- [MPSCNNLogSoftMax](mpscnnlogsoftmax.md)
- [MPSCNNLoss](mpscnnloss.md)
- [MPSCNNNeuron](mpscnnneuron.md)
- [MPSCNNPooling](mpscnnpooling.md)
- [MPSCNNSoftMax](mpscnnsoftmax.md)
- [MPSCNNSpatialNormalization](mpscnnspatialnormalization.md)
- [MPSCNNUpsampling](mpscnnupsampling.md)
- [MPSCNNYOLOLoss](mpscnnyololoss.md)
- [MPSNNCropAndResizeBilinear](mpsnncropandresizebilinear.md)
- [MPSNNForwardLoss](mpsnnforwardloss.md)
- [MPSNNGramMatrixCalculation](mpsnngrammatrixcalculation.md)
- [MPSNNInitialGradient](mpsnninitialgradient.md)
- [MPSNNPad](mpsnnpad.md)
- [MPSNNReduceUnary](mpsnnreduceunary.md)
- [MPSNNReshape](mpsnnreshape.md)
- [MPSNNResizeBilinear](mpsnnresizebilinear.md)
- [MPSNNSlice](mpsnnslice.md)
- [MPSRNNImageInferenceLayer](mpsrnnimageinferencelayer.md)
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

- [class MPSCNNBinaryKernel](mpscnnbinarykernel.md)
  A convolution neural network kernel.
- [class MPSCNNGradientKernel](mpscnngradientkernel.md)
  The base class for gradient layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel)*