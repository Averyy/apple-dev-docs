# encode(commandBuffer:primaryImage:secondaryImage:destinationImage:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationImage: MPSImage)
```

## See Also

- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, inPlaceSecondaryTexture: UnsafeMutablePointer<any MTLTexture>, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsbinaryimagekernel/1618890-encode.md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, inPlacePrimaryTexture: UnsafeMutablePointer<any MTLTexture>, secondaryTexture: any MTLTexture, fallbackCopyAllocator: MPSCopyAllocator?) -> Bool](mpsbinaryimagekernel/1618771-encode.md)
  This method attempts to apply a kernel in place on a texture.
- [func encode(commandBuffer: any MTLCommandBuffer, primaryTexture: any MTLTexture, secondaryTexture: any MTLTexture, destinationTexture: any MTLTexture)](mpsbinaryimagekernel/1618871-encode.md)
  Encodes a kernel into a command buffer, out-of-place.
- [func primarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](mpsbinaryimagekernel/1618900-primarysourceregion.md)
  Determines the region of the primary source texture that will be read for an encode operation.
- [func secondarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](mpsbinaryimagekernel/1618838-secondarysourceregion.md)
  Determines the region of the secondary source texture that will be read for an encode operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/2866330-encode)*