# init(commandBuffer:imageDescriptor:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes a temporary image for use on a command buffer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(commandBuffer: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor)
```

#### Return Value

A valid [`MPSTemporaryImage`](mpstemporaryimage.md) object.

#### Discussion

The temporary image will be released when the command buffer is committed. The underlying texture will become invalid before this time due to the action of the [`readCount`](mpstemporaryimage/readcount.md) property.

## Parameters

- `commandBuffer`: The command buffer on which the temporary image will be exclusively used.
- `imageDescriptor`: An image descriptor that describes the image to create.

## See Also

- [class MPSImageDescriptor](mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](mpsimage.md).
- [convenience init(commandBuffer: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor)](mpstemporaryimage/init(commandbuffer:texturedescriptor:).md)
  Low-level interface for creating a temporary image using a texture descriptor.
- [class MTLTextureDescriptor](../Metal/MTLTextureDescriptor.md)
  An object that you use to configure new Metal texture objects.
- [convenience init(commandBuffer: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor, featureChannels: Int)](mpstemporaryimage/init(commandbuffer:texturedescriptor:featurechannels:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage/init(commandbuffer:imagedescriptor:))*