# MPSNNPadding

**Framework**: Metal Performance Shaders  
**Kind**: protocol

The protocol that provides a description of how kernels should pad images.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol MPSNNPadding : NSSecureCoding, NSObjectProtocol
```

## Topics

### Instance Methods
- [func destinationImageDescriptor(forSourceImages: [MPSImage], sourceStates: [MPSState]?, for: MPSKernel, suggestedDescriptor: MPSImageDescriptor) -> MPSImageDescriptor](mpsnnpadding/destinationimagedescriptor(forsourceimages:sourcestates:for:suggesteddescriptor:).md)
- [class MPSImage](mpsimage.md)
  A texture that may have more than four channels for use in convolutional neural networks.
- [class MPSState](mpsstate.md)
  An opaque data container for large storage in MPS CNN filters.
- [class MPSKernel](mpskernel.md)
  A standard interface for Metal Performance Shaders kernels.
- [class MPSImageDescriptor](mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](mpsimage.md).
- [func paddingMethod() -> MPSNNPaddingMethod](mpsnnpadding/paddingmethod.md)
- [func label() -> String](mpsnnpadding/label.md)
- [func inverse() -> Self?](mpsnnpadding/inverse.md)

## Relationships

### Inherits From
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
### Conforming Types
- [MPSNNDefaultPadding](mpsnndefaultpadding.md)

## See Also

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
- [var destinationImageAllocator: any MPSImageAllocator](mpscnnkernel/destinationimageallocator.md)
- [protocol MPSImageAllocator](mpsimageallocator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnpadding)*