# init(commandBuffer:textureDescriptor:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Low-level interface for creating a temporary image using a texture descriptor.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(commandBuffer: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor)
```

#### Return Value

A valid [`MPSTemporaryImage`](mpstemporaryimage.md) object.

#### Discussion

The temporary image will be released when the command buffer is committed. The underlying texture will become invalid before this time due to the action of the [`readCount`](mpstemporaryimage/readcount.md) property.

This function provides access to pixel formats not typically covered by the [`init(commandBuffer:imageDescriptor:)`](mpstemporaryimage/init(commandbuffer:imagedescriptor:).md) method. The feature channels will be inferred from the pixel format without changing the width. The following restrictions apply:

- The texture type must be [`MTLTextureType.type2D`](https://developer.apple.com/documentation/Metal/MTLTextureType/type2D) or [`MTLTextureType.type2DArray`](https://developer.apple.com/documentation/Metal/MTLTextureType/type2DArray).
- The texture usage must contain at least one of [`shaderRead`](https://developer.apple.com/documentation/Metal/MTLTextureUsage/shaderRead) or [`shaderWrite`](https://developer.apple.com/documentation/Metal/MTLTextureUsage/shaderWrite).
- The storage mode must be [`MTLStorageMode.private`](https://developer.apple.com/documentation/Metal/MTLStorageMode/private).
- The depth must be 1.

## Parameters

- `commandBuffer`: The command buffer on which the temporary image will be exclusively used.
- `textureDescriptor`: A texture descriptor that describes the temporary image texture to create.

## See Also

- [convenience init(commandBuffer: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor)](mpstemporaryimage/init(commandbuffer:imagedescriptor:).md)
  Initializes a temporary image for use on a command buffer.
- [class MPSImageDescriptor](mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](mpsimage.md).
- [class MTLTextureDescriptor](../Metal/MTLTextureDescriptor.md)
  An instance that you use to configure new Metal texture instances.
- [convenience init(commandBuffer: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor, featureChannels: Int)](mpstemporaryimage/init(commandbuffer:texturedescriptor:featurechannels:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage/init(commandbuffer:texturedescriptor:))*