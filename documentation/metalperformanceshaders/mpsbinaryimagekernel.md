# MPSBinaryImageKernel

**Framework**: Metal Performance Shaders  
**Kind**: cl

A kernel that consumes two textures and produces one texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSBinaryImageKernel : MPSKernel
```

#### Overview

[`MPSBinaryImageKernel`](mpsbinaryimagekernel.md) defines shared behavior for most image processing kernels (filters) such as edging modes, clipping, and tiling support for image operations that consume two source textures. It is not meant to be used directly, but provides API abstraction and in some cases may allow some level of polymorphic manipulation of image kernel objects.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsbinaryimagekernel/2866333-init.md)
- [init(device: any MTLDevice)](mpsbinaryimagekernel/2866331-init.md)
### Methods
- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, inPlaceSecondaryTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsbinaryimagekernel/1618890-encode.md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, inPlacePrimaryTexture: UnsafeMutablePointer<any MTLTexture>, secondaryTexture: any MTLTexture, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsbinaryimagekernel/1618771-encode.md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, secondaryTexture: any MTLTexture, destinationTexture: any MTLTexture)](mpsbinaryimagekernel/1618871-encode.md)
  Encodes a kernel into a command buffer, out-of-place.
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationImage: MPSImage)](mpsbinaryimagekernel/2866330-encode.md)
- [func primarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](mpsbinaryimagekernel/1618900-primarysourceregion.md)
  Determines the region of the primary source texture that will be read for an encode operation.
- [func secondarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](mpsbinaryimagekernel/1618838-secondarysourceregion.md)
  Determines the region of the secondary source texture that will be read for an encode operation.
### Properties
- [var primaryOffset: MPSOffset](mpsbinaryimagekernel/1618880-primaryoffset.md)
  The position of the destination clip rectangle origin relative to the primary source buffer.
- [var secondaryOffset: MPSOffset](mpsbinaryimagekernel/1618755-secondaryoffset.md)
  The position of the destination clip rectangle origin relative to the secondary source buffer.
- [var primaryEdgeMode: MPSImageEdgeMode](mpsbinaryimagekernel/1618782-primaryedgemode.md)
  The edge mode to use when texture reads stray off the edge of the primary source image.
- [var secondaryEdgeMode: MPSImageEdgeMode](mpsbinaryimagekernel/1618848-secondaryedgemode.md)
  The edge mode to use when texture reads stray off the edge of the secondary source image.
- [var clipRect: MTLRegion](mpsbinaryimagekernel/1618879-cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the rectangle will be overwritten.

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)

## See Also

- [class MPSUnaryImageKernel](mpsunaryimagekernel.md)
  A kernel that consumes one texture and produces one texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel)*