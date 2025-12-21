# destinationFeatureChannelOffset

**Framework**: Metal Performance Shaders  
**Kind**: property

The number of channels in the destination image to skip before writing output data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var destinationFeatureChannelOffset: Int { get set }
```

#### Discussion

This is the starting offset in the destination image in the feature channel dimension at which destination output data is written. This allows you to pass a subset of all the channels in an image as the output of a kernel.

For example, suppose a destination image has 24 channels and a kernel outputs 8 channels. If we want channels 8 to 15 of this destination image to be used for the output, we can set the value of the [`destinationFeatureChannelOffset`](mpscnnkernel/destinationfeaturechanneloffset.md) property to 8.

Note that this offset applies independently to each image when the [`MPSImage`](mpsimage.md) object is a container for multiple images and the [`MPSCNNKernel`](mpscnnkernel.md) object is processing multiple images (i.e., `clipRect.size.depth > 1`).

The default value is `0`. Any other value specified must be a multiple of `4`. If the kernel outputs `N` channels, the destination image  have at least `destinationFeatureChannelOffset + N` channels. Using a destination image with an insufficient number of feature channels results in an error.

For example, if a convolution filter outputs 32 channels, and the destination image has 64 channels, then it is an error to set `destinationFeatureChannelOffset > 32`.

## See Also

- [var offset: MPSOffset](mpscnnkernel/offset.md)
  The position of the destination image’s clip rectangle origin, relative to the source image.
- [struct MPSOffset](mpsoffset.md)
  A signed coordinate with x, y, and z components.
- [var clipRect: MTLRegion](mpscnnkernel/cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the clip rectangle will be overwritten.
- [struct MTLRegion](../Metal/MTLRegion.md)
  The bounds for a subset of an instance’s elements.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/destinationfeaturechanneloffset)*