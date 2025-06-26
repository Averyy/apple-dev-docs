# precision

**Framework**: Metal Performance Shaders  
**Kind**: property

The number of bits of numeric precision available for each feature channel.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var precision: Int { get }
```

#### Discussion

This is precision, not size (float is 24 bits, not 32; half-precision floating-point is 11 bits, not 16; `Snorm` pixel formats have one less bit of precision for the sign bit, etc.). For formats like [`MTLPixelFormat.b5g6r5Unorm`](https://developer.apple.com/documentation/Metal/MTLPixelFormat/b5g6r5Unorm), this value is the precision of the most precise channel (which is 6 in this case). When this information is unavailable, typically for compressed formats, this value is 0.

## See Also

- [var device: any MTLDevice](mpsimage/device.md)
  The device on which the image will be used.
- [var width: Int](mpsimage/width.md)
  The formal width of the image, in pixels.
- [var height: Int](mpsimage/height.md)
  The formal height of the image, in pixels.
- [var featureChannels: Int](mpsimage/featurechannels.md)
  The number of feature channels per pixel.
- [var numberOfImages: Int](mpsimage/numberofimages.md)
  The number of images for batch processing.
- [var textureType: MTLTextureType](mpsimage/texturetype.md)
  The type of the underlying texture.
- [enum MTLTextureType](../Metal/MTLTextureType.md)
  The dimension of each image, including whether multiple images are arranged into an array or a cube.
- [var pixelFormat: MTLPixelFormat](mpsimage/pixelformat.md)
  The pixel format of the underlying texture.
- [enum MTLPixelFormat](../Metal/MTLPixelFormat.md)
  The data formats that describe the organization and characteristics of individual pixels in a texture.
- [var usage: MTLTextureUsage](mpsimage/usage.md)
  The intended usage of the underlying texture.
- [struct MTLTextureUsage](../Metal/MTLTextureUsage.md)
  An enumeration for the various options that determine how you can use a texture.
- [var pixelSize: Int](mpsimage/pixelsize.md)
  The number of bytes from the first byte of one pixel to the first byte of the next pixel, in storage order. (Includes padding.)
- [var texture: any MTLTexture](mpsimage/texture.md)
  The underlying texture.
- [protocol MTLTexture : MTLResource](../Metal/MTLTexture.md)
  A resource that holds formatted image data.
- [var label: String?](mpsimage/label.md)
  A string to help identify this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/precision)*