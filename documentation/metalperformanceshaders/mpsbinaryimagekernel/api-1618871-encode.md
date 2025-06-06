# encode(commandBuffer:primaryTexture:secondaryTexture:destinationTexture:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

Encodes a kernel into a command buffer, out-of-place.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, secondaryTexture: any MTLTexture, destinationTexture: any MTLTexture)
```

## Parameters

- `commandBuffer`: A valid command buffer to receive the encoded kernel.
- `primaryTexture`: A valid texture containing the primary source image.
- `secondaryTexture`: A valid texture containing the secondary source image.
- `destinationTexture`: A valid texture to be overwritten by the result image.   may not alias   nor  .

## See Also

- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, inPlaceSecondaryTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsbinaryimagekernel/1618890-encode.md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, inPlacePrimaryTexture: UnsafeMutablePointer<any MTLTexture>, secondaryTexture: any MTLTexture, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsbinaryimagekernel/1618771-encode.md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationImage: MPSImage)](mpsbinaryimagekernel/2866330-encode.md)
- [func primarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](mpsbinaryimagekernel/1618900-primarysourceregion.md)
  Determines the region of the primary source texture that will be read for an encode operation.
- [func secondarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](mpsbinaryimagekernel/1618838-secondarysourceregion.md)
  Determines the region of the secondary source texture that will be read for an encode operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618871-encode)*