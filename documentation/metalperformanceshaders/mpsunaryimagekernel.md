# MPSUnaryImageKernel

**Framework**: Metal Performance Shaders  
**Kind**: cl

A kernel that consumes one texture and produces one texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSUnaryImageKernel : MPSKernel
```

#### Overview

[`MPSUnaryImageKernel`](mpsunaryimagekernel.md) defines shared behavior for most image processing kernels (filters) such as edging modes, clipping, and tiling support for image operations that consumes a single source textures. It is not meant to be used directly, but provides API abstraction and in some cases may allow some level of polymorphic manipulation of image kernel objects.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsunaryimagekernel/2866329-init.md)
- [init(device: any MTLDevice)](mpsunaryimagekernel/2866332-init.md)
### Methods
- [func encode(commandBuffer: any MTLCommandBuffer, inPlaceTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsunaryimagekernel/1618873-encode.md)
  This method attempts to apply a kernel in place on a texture.
- [typealias MPSCopyAllocator](mpscopyallocator.md)
  A block to make a copy of a source texture for filters that can only execute out of place.
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationImage: MPSImage)](mpsunaryimagekernel/2866328-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)](mpsunaryimagekernel/1618741-encode.md)
  Encodes a kernel into a command buffer, out of place.
- [func sourceRegion(destinationSize: MTLSize) -> MPSRegion](mpsunaryimagekernel/1618754-sourceregion.md)
  Determines the region of the source texture that will be read for an encode operation.
### Properties
- [var offset: MPSOffset](mpsunaryimagekernel/1618884-offset.md)
  The position of the destination clip rectangle origin relative to the source buffer.
- [struct MPSOffset](mpsoffset.md)
  A signed coordinate with x, y, and z components.
- [var clipRect: MTLRegion](mpsunaryimagekernel/1618859-cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the rectangle will be overwritten.
- [struct MPSRegion](mpsregion.md)
  A region of an image.
- [var edgeMode: MPSImageEdgeMode](mpsunaryimagekernel/1618812-edgemode.md)
  The edge mode to use when texture reads stray off the edge of an image.
- [enum MPSImageEdgeMode](mpsimageedgemode.md)
  The options used to control the edge behavior of an image filter when it reads outside the bounds of a source texture.

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)

## See Also

- [class MPSBinaryImageKernel](mpsbinaryimagekernel.md)
  A kernel that consumes two textures and produces one texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel)*