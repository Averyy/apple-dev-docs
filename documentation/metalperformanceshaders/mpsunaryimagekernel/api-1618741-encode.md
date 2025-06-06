# encode(commandBuffer:sourceTexture:destinationTexture:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

Encodes a kernel into a command buffer, out of place.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)
```

## Parameters

- `commandBuffer`: A valid command buffer to receive the encoded kernel.
- `sourceTexture`: A valid texture containing the source image.
- `destinationTexture`: A valid texture to be overwritten by the result image.   may not alias  .

## See Also

- [func encode(commandBuffer: any MTLCommandBuffer, inPlaceTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsunaryimagekernel/1618873-encode.md)
  This method attempts to apply a kernel in place on a texture.
- [typealias MPSCopyAllocator](mpscopyallocator.md)
  A block to make a copy of a source texture for filters that can only execute out of place.
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationImage: MPSImage)](mpsunaryimagekernel/2866328-encode.md)
- [func sourceRegion(destinationSize: MTLSize) -> MPSRegion](mpsunaryimagekernel/1618754-sourceregion.md)
  Determines the region of the source texture that will be read for an encode operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/1618741-encode)*