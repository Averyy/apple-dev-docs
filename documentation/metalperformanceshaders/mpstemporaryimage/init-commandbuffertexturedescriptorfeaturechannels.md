# init(commandBuffer:textureDescriptor:featureChannels:)

**Framework**: Metal Performance Shaders  
**Kind**: init

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
convenience init(commandBuffer: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor, featureChannels: Int)
```

## See Also

- [convenience init(commandBuffer: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor)](mpstemporaryimage/init(commandbuffer:imagedescriptor:).md)
  Initializes a temporary image for use on a command buffer.
- [class MPSImageDescriptor](mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](mpsimage.md).
- [convenience init(commandBuffer: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor)](mpstemporaryimage/init(commandbuffer:texturedescriptor:).md)
  Low-level interface for creating a temporary image using a texture descriptor.
- [class MTLTextureDescriptor](../Metal/MTLTextureDescriptor.md)
  An object that you use to configure new Metal texture objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage/init(commandbuffer:texturedescriptor:featurechannels:))*