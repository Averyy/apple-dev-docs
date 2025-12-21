# encode(commandBuffer:inPlaceTexture:fallbackCopyAllocator:)

**Framework**: Metal Performance Shaders  
**Kind**: method

This method attempts to apply a kernel in place on a texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, inPlaceTexture texture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator copyAllocator: MPSCopyAllocator? = nil) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the operation succeeded (the texture may have been replaced with a new texture if a copy allocator was provided). [`false`](https://developer.apple.com/documentation/Swift/false) if the operation failed (the texture is unmodified).

#### Discussion

This method attempts to apply the kernel in place on a texture. In-place operation means that the same texture is used both to hold the input image and the results. Operating in-place can be an excellent way to reduce resource utilization, and save time and energy. While simple Metal kernels can not operate in place because textures can not be readable and writable at the same time, some Metal Performance Shaders kernels can operate in place because they use multi-pass algorithms. Whether a kernel can operate in-place can depend on current hardware, OS version, and the parameters and properties passed to it. You should never assume that a kernel will continue to work in place, even if you have observed it doing so before.

If the in-place operation succeeds, this method returns [`true`](https://developer.apple.com/documentation/Swift/true).  If the in-place operation fails and no copy allocator is provided, then this method returns [`false`](https://developer.apple.com/documentation/Swift/false). Without a fallback copy allocator, in neither case is the pointer held at `texture` modified.

Failure during in-place operation is very common and will occur inconsistently across different hardware platforms and OS versions. Without a fallback copy allocator, operating in place may require significant error handling code to accompany each call to this method, further complicating your code.

You may find it simplifies your code to provide a fallback copy allocator so that the operation can proceed reliably even when it can not complete in-place. When an in-place filter fails, the copy allocator will be invoked to create a new texture in which to write the results, allowing the filter to proceed reliably out-of-place. The original texture will be released, replaced with a pointer to the new texture and [`true`](https://developer.apple.com/documentation/Swift/true) will be returned. If the copy allocator returns an invalid texture, it is released, `texture` remains unmodified, and [`false`](https://developer.apple.com/documentation/Swift/false) is returned.

Listing 1. In-Place Operation Example

```objc
id <MTLTexture> inPlaceTex = ...;
MPSImageSobel *sobelFiler = [[MPSImageSobel alloc] initWithDevice: my_device];
 
// With a fallback MPSCopyAllocator, failure should only occur in exceptional conditions such as MTLTexture allocation failure or programmer error.
// That is, the operation is roughly as robust as the MPSCopyAllocator.
// Depending on the quality of that, we might decide we are justified here in not checking the return value.
[sobelFilter encodeToCommandBuffer: my_command_buffer inPlaceTexture: &inPlaceTex fallbackCopyAllocator: myAllocator];
// inPlaceTex may be replaced!
 
// If myAllocator was not called:
//      inPlaceTex holds the original texture with the result pixels in it.
// Else:
//      1) myAllocator creates a new texture.
//      2) The new texture pixel data is overwritten by MPSUnaryImageKernel.
//      3) The old texture passed in *inPlaceTex is released once.
//      4) *inPlaceTex = the new texture
//
// In either case, the caller should now hold one reference to the texture now held in inPlaceTex, whether it was replaced or not. Most of the time that means that nothing further needs to be done here, and you can proceed to the next image encoding operation. However, if other agents held references to the original texture, they still hold them and may need to be alerted that the texture has been replaced so that they can retain the new texture and release the old one.
 
[sobelFilter release];  // if not ARC, clean up the MPSImageSobel object
```

## Parameters

- `commandBuffer`: A valid command buffer to receive the encoded kernel.
- `texture`: A pointer to a valid texture containing the source image. On success, the image contents and possibly the texture itself will be replaced with the result image.
- `copyAllocator`: An optional block to allocate a new texture to hold the operation results, in case in-place operation is not possible. The allocator may use a different pixel format or size than the original texture. You may enqueue operations on the provided command buffer using the provided compute command encoder to initialize the texture contents.

## See Also

- [typealias MPSCopyAllocator](mpscopyallocator.md)
  A block to make a copy of a source texture for filters that can only execute out of place.
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationImage: MPSImage)](mpsunaryimagekernel/encode(commandbuffer:sourceimage:destinationimage:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)](mpsunaryimagekernel/encode(commandbuffer:sourcetexture:destinationtexture:).md)
  Encodes a kernel into a command buffer, out of place.
- [func sourceRegion(destinationSize: MTLSize) -> MPSRegion](mpsunaryimagekernel/sourceregion(destinationsize:).md)
  Determines the region of the source texture that will be read for an encode operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/encode(commandbuffer:inplacetexture:fallbackcopyallocator:))*