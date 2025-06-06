# pixelFormat

**Framework**: Metal Performance Shaders  
**Kind**: instp

The pixel format of the underlying texture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var pixelFormat: MTLPixelFormat { get }
```

## See Also

- [var device: any MTLDevice](mpsimage/1648857-device.md)
  The device on which the image will be used.
- [var width: Int](mpsimage/1648884-width.md)
  The formal width of the image, in pixels.
- [var height: Int](mpsimage/1648952-height.md)
  The formal height of the image, in pixels.
- [var featureChannels: Int](mpsimage/1648901-featurechannels.md)
  The number of feature channels per pixel.
- [var numberOfImages: Int](mpsimage/1648900-numberofimages.md)
  The number of images for batch processing.
- [var textureType: MTLTextureType](mpsimage/1648948-texturetype.md)
  The type of the underlying texture, typically [`MTLTextureType.type2D`](https://developer.apple.com/documentation/metal/mtltexturetype/type2d) or [`MTLTextureType.type2DArray`](https://developer.apple.com/documentation/metal/mtltexturetype/type2darray).
- [enum MTLTextureType](../metal/mtltexturetype.md)
  The dimension of each image, including whether multiple images are arranged into an array or a cube.
- [enum MTLPixelFormat](../metal/mtlpixelformat.md)
  The data formats that describe the organization and characteristics of individual pixels in a texture.
- [var precision: Int](mpsimage/1648880-precision.md)
  The number of bits of numeric precision available for each feature channel.
- [var usage: MTLTextureUsage](mpsimage/1648828-usage.md)
  The intended usage of the underlying texture.
- [struct MTLTextureUsage](../metal/mtltextureusage.md)
  An enumeration for the various options that determine how you can use a texture.
- [var pixelSize: Int](mpsimage/1648854-pixelsize.md)
  The number of bytes from the first byte of one pixel to the first byte of the next pixel, in storage order. (Includes padding.)
- [var texture: any MTLTexture](mpsimage/1648903-texture.md)
  The underlying texture.
- [protocol MTLTexture](../metal/mtltexture.md)
  A resource that holds formatted image data.
- [var label: String?](mpsimage/1648899-label.md)
  A string to help identify this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648844-pixelformat)*