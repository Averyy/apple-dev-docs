# init(texture:featureChannels:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes an image from a texture. The user-allocated texture has been created for a specific number of feature channels and number of images.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(texture: any MTLTexture, featureChannels: Int)
```

#### Return Value

A valid [`MPSImage`](mpsimage.md) object or `nil`, if failure.

#### Discussion

In a memory-intensive app, you can save memory (and allocation/deallocation time) by using an [`MPSTemporaryImage`](mpstemporaryimage.md) object, where the framework aggressively reuses underlying texture memory within the same command buffer. However, in certain cases, you may want more control on the allocation, placement, reuse, and recycling of memory-backing textures used in your app by using the Metal Resource Heaps API. In this case, an app can create an [`MPSImage`](mpsimage.md) object from a pre-allocated texture by calling this method.

The [`textureType`](https://developer.apple.com/documentation/Metal/MTLTexture/textureType) property of the given texture can be of type [`MTLTextureType.type2D`](https://developer.apple.com/documentation/Metal/MTLTextureType/type2D)  if `featureChannels<=4` (meaning that `numberOfImages=1`). Otherwise, the texture type should be [`MTLTextureType.type2DArray`](https://developer.apple.com/documentation/Metal/MTLTextureType/type2DArray) with the [`arrayLength`](https://developer.apple.com/documentation/Metal/MTLTexture/arrayLength) property of the given texture being equal to `numberOfImages*((featureChannels+3)/4)`.

For textures containing typical image data, the `featureChannels` parameter should be set to the number of valid color channels (e.g. for RGB data, even though the pixel format is a form of `MTLPixelFormatRGBA`, `featureChannels` should be set to 3.).

## Parameters

- `texture`: The texture allocated by the user to be used as a backing storage for the image.
- `featureChannels`: The number of feature channels the texture contains.

## See Also

- [convenience init(device: any MTLDevice, imageDescriptor: MPSImageDescriptor)](mpsimage/init(device:imagedescriptor:).md)
  Initializes an empty image.
- [class MPSImageDescriptor](mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](mpsimage.md).
- [init(parentImage: MPSImage, sliceRange: NSRange, featureChannels: Int)](mpsimage/init(parentimage:slicerange:featurechannels:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/init(texture:featurechannels:))*