# MPSCopyAllocator

**Framework**: Metal Performance Shaders  
**Kind**: tdef

A block to make a copy of a source texture for filters that can only execute out of place.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias MPSCopyAllocator = (MPSKernel, any MTLCommandBuffer, any MTLTexture) -> any MTLTexture
```

#### Discussion

The block takes the following parameters:

The copy allocator returns a new valid texture to use as the destination for the kernel operation. If the calling function succeeds, its texture parameter will be overwritten with a pointer to this texture. If the calling function fails, then the texture will be released before the calling function returns.

Allocating a new texture each time is slow (they take up to 1 ms each). You can recycle old textures (or buffers and make texture from them) and reuse the memory inside the copy allocator block.

If there is any metadata associated with the source texture, such as colorspace information, resource label, CPU cache mode, purgeable state, etc., it may need to be similarly associated with the new texture to avoid losing your metadata.

If the kernel’s [`clipRect`](mpsunaryimagekernel/1618859-cliprect.md) property doesn’t cover the entire image, you may need to copy pixels from the source texture to the new texture, or regions of the next texture will be uninitialized. You can make a command encoder to encode work on the command buffer here, if necessary. It will be scheduled to run immediately before the kernel work. You may call any of the [`enqueue()`](https://developer.apple.com/documentation/metal/mtlcommandbuffer/enqueue()), [`commit()`](https://developer.apple.com/documentation/metal/mtlcommandbuffer/commit()), [`waitUntilCompleted()`](https://developer.apple.com/documentation/metal/mtlcommandbuffer/waituntilcompleted()), or [`waitUntilScheduled()`](https://developer.apple.com/documentation/metal/mtlcommandbuffer/waituntilscheduled()) methods inside the copy allocator block. Make sure to call [`endEncoding()`](https://developer.apple.com/documentation/metal/mtlcommandencoder/endencoding()) on the command encoder so that the command buffer has no active encoder before returning.

> **Note**: The next command placed on the command buffer after the copy allocator returns is almost assuredly going to be encoded with a compute command encoder. Creating any other type of encoder in the copy allocator will probably cost an additional 0.5 ms of both CPU  GPU time (or more!) due to a double mode switch penalty.

[`Listing 1`](mpscopyallocator#1942956.md) shows a minimal copy allocator implementation.

```swift
let copyAllocator: MPSCopyAllocator =
{
    (kernel: MPSKernel, buffer: MTLCommandBuffer, texture: MTLTexture) -> MTLTexture in
    
    let descriptor = MTLTextureDescriptor.texture2DDescriptor(
        pixelFormat: texture.pixelFormat,
        width: texture.width,
        height: texture.height,
        mipmapped: false)
    
    return buffer.device.makeTexture(descriptor: descriptor)
}

```

## See Also

- [func encode(commandBuffer: any MTLCommandBuffer, inPlaceTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsunaryimagekernel/1618873-encode.md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationImage: MPSImage)](mpsunaryimagekernel/2866328-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)](mpsunaryimagekernel/1618741-encode.md)
  Encodes a kernel into a command buffer, out of place.
- [func sourceRegion(destinationSize: MTLSize) -> MPSRegion](mpsunaryimagekernel/1618754-sourceregion.md)
  Determines the region of the source texture that will be read for an encode operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscopyallocator)*