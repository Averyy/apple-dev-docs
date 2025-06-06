# MPSCNNKernel

**Framework**: Metal Performance Shaders  
**Kind**: cl

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
class MPSCNNKernel : MPSKernel
```

#### Overview

An [`MPSCNNKernel`](mpscnnkernel.md) object consumes one [`MPSImage`](mpsimage.md) object and produces one [`MPSImage`](mpsimage.md) object.

The region overwritten in the destination image is described by the [`clipRect`](mpscnnkernel/1648911-cliprect.md)` `property.  The top left corner of the region consumed (ignoring adjustments for filter size—for example, convolution filter size) is given by the [`offset`](mpscnnkernel/1648835-offset.md) property. The size of the region consumed is a function of the size of the [`clipRect`](mpscnnkernel/1648911-cliprect.md) property and any subsampling caused by pixel strides at work (for example, `strideInPixelsX``/``strideInPixelsY` in the [`MPSCNNPooling`](mpscnnpooling.md) class).  Wherever the [`offset`](mpscnnkernel/1648835-offset.md) and [`clipRect`](mpscnnkernel/1648911-cliprect.md) properties would cause an `{x,y}` pixel address not in the image to be read, the [`edgeMode`](mpscnnkernel/1648826-edgemode.md) property is used to determine what value to read there.

The `z` or `depth` component of the [`offset`](mpscnnkernel/1648835-offset.md), [`origin`](https://developer.apple.com/documentation/metal/mtlregion/origin) and [`size`](mpsregion/1618858-size.md) properties indexes which images to use.

- If the [`MPSImage`](mpsimage.md) object contains only a single image, then these values should be `offset.z = 0`, `clipRect.origin.z = 0`, and `clipRect.size.depth = 1`.
- If the [`MPSImage`](mpsimage.md) object contains multiple images, then the value of `clipRect.size.depth` determines the number of images to process. Both the source and destination [`MPSImage`](mpsimage.md) objects must have at least this many images. The value of `offset.z` refers to the starting image index of the source. Thus, the value of `offset.z + clipRect.size.depth` must be `<=source.numberOfImages`. Similarly, the value of `clipRect.origin.z` determines the starting image index of the destination. Thus, the value of `clipRect.origin.z + clipRect.size.depth` must be `<=destination.numberOfImages`.

The [`destinationFeatureChannelOffset`](mpscnnkernel/2097550-destinationfeaturechanneloffset.md) property can be used to control where the kernel will start writing in terms of feature channel dimension. For example, if the destination has 64 channels and th[`destinationFeatureChannelOffset`](mpscnnkernel/2097550-destinationfeaturechanneloffset.md)e kernel outputs 32 channels, channels 0-31 of the destination will be populated by the kernel (by default). But if you want the kernel to populate channels 32-63 of the destination, you can set the value of [`destinationFeatureChannelOffset`](mpscnnkernel/2097550-destinationfeaturechanneloffset.md) to 32. Suppose you have a source of dimensions `w x h x Ni`, where `N` is the number of channels, which goes through a convolution filter `C0` which produces the output` O0 = w x h x N0` and `C`1 which produces the output `O1 = w x h x N1` followed by concatenation which produces `O = w x h x (N0 + N1)`. You can achieve this by creating an [`MPSImage`](mpsimage.md) object with dimensions `w x h x (N0 + N1)` and using this as the destination of both convolutions as follows:

- `C0: destinationFeatureChannelOffset = 0`, this will output `N0` channels starting at channel `0` of destination thus populating `[0,N0-1]` channels.
- `C1: destinationFeatureChannelOffset = N0`, this will output `N1` channels starting at channel `N0` of destination thus populating `[N0,N0+N1-1]` channels.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnkernel/2865655-init.md)
- [init(device: any MTLDevice)](mpscnnkernel/2865653-init.md)
### Instance Properties
- [var offset: MPSOffset](mpscnnkernel/1648835-offset.md)
  The position of the destination image's clip rectangle origin, relative to the source image.
- [struct MPSOffset](mpsoffset.md)
  A signed coordinate with x, y, and z components.
- [var clipRect: MTLRegion](mpscnnkernel/1648911-cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the clip rectangle will be overwritten.
- [struct MTLRegion](../metal/mtlregion.md)
  The bounds for a subset of an object’s elements.
- [var destinationFeatureChannelOffset: Int](mpscnnkernel/2097550-destinationfeaturechanneloffset.md)
  The number of channels in the destination image to skip before writing output data.
- [var edgeMode: MPSImageEdgeMode](mpscnnkernel/1648826-edgemode.md)
  The edge mode to use when texture reads stray off the edge of an image.
- [enum MPSImageEdgeMode](mpsimageedgemode.md)
  The options used to control the edge behavior of an image filter when it reads outside the bounds of a source texture.
- [var kernelHeight: Int](mpscnnkernel/2865648-kernelheight.md)
- [var kernelWidth: Int](mpscnnkernel/2865637-kernelwidth.md)
- [var strideInPixelsX: Int](mpscnnkernel/2865654-strideinpixelsx.md)
- [var strideInPixelsY: Int](mpscnnkernel/2865644-strideinpixelsy.md)
- [var isBackwards: Bool](mpscnnkernel/2865634-isbackwards.md)
- [var padding: any MPSNNPadding](mpscnnkernel/2865657-padding.md)
- [protocol MPSNNPadding](mpsnnpadding.md)
  The protocol that provides a description of how kernels should pad images.
- [var destinationImageAllocator: any MPSImageAllocator](mpscnnkernel/2865650-destinationimageallocator.md)
- [protocol MPSImageAllocator](mpsimageallocator.md)
- [var dilationRateX: Int](mpscnnkernel/2942669-dilationratex.md)
- [var dilationRateY: Int](mpscnnkernel/2942679-dilationratey.md)
- [var isStateModified: Bool](mpscnnkernel/2942673-isstatemodified.md)
- [var sourceFeatureChannelMaxCount: Int](mpscnnkernel/2951917-sourcefeaturechannelmaxcount.md)
- [var sourceFeatureChannelOffset: Int](mpscnnkernel/2942682-sourcefeaturechanneloffset.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage) -> MPSImage](mpscnnkernel/2865642-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationImage: MPSImage)](mpscnnkernel/1648919-encode.md)
  Encodes a kernel into a command buffer.  The ensuing operation proceeds out-of-place.
- [func appendBatchBarrier() -> Bool](mpscnnkernel/2942671-appendbatchbarrier.md)
- [func batchEncodingStorageSize(sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]?) -> Int](mpscnnkernel/3237263-batchencodingstoragesize.md)
- [func destinationImageDescriptor(sourceImages: [MPSImage], sourceStates: [MPSState]?) -> MPSImageDescriptor](mpscnnkernel/2942661-destinationimagedescriptor.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationState: MPSState, destinationImage: MPSImage)](mpscnnkernel/2942672-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary: Bool) -> MPSImage](mpscnnkernel/2942680-encode.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage]) -> [MPSImage]](mpscnnkernel/2942651-encodebatch.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationImages: [MPSImage])](mpscnnkernel/2942681-encodebatch.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationStates: [MPSState]?, destinationImages: [MPSImage])](mpscnnkernel/2942649-encodebatch.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationStates: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary: Bool) -> [MPSImage]](mpscnnkernel/2942646-encodebatch.md)
- [func encodingStorageSize(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage?) -> Int](mpscnnkernel/3237264-encodingstoragesize.md)
- [func isResultStateReusedAcrossBatch() -> Bool](mpscnnkernel/2942665-isresultstatereusedacrossbatch.md)
- [func resultState(sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnkernel/2947932-resultstate.md)
- [func resultStateBatch(sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnkernel/2947931-resultstatebatch.md)
- [func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?](mpscnnkernel/2947937-temporaryresultstate.md)
- [func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?](mpscnnkernel/2947939-temporaryresultstatebatch.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)

## See Also

- [class MPSCNNBinaryKernel](mpscnnbinarykernel.md)
  A convolution neural network kernel.
- [class MPSCNNGradientKernel](mpscnngradientkernel.md)
  The base class for gradient layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel)*