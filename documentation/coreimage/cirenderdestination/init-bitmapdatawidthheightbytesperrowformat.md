# init(bitmapData:width:height:bytesPerRow:format:)

**Framework**: Core Image  
**Kind**: init

Creates a render destination based on a client-managed buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(bitmapData data: UnsafeMutableRawPointer, width: Int, height: Int, bytesPerRow: Int, format: CIFormat)
```

#### Return Value

A [`CIRenderDestination`](cirenderdestination.md) object for rendering to a client-managed buffer.

#### Discussion

The destination’s [`colorSpace`](ciimage/colorspace.md) property will default to a [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) created with [`sRGB`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace/sRGB), [`extendedSRGB`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace/extendedSRGB), or [`genericGrayGamma2_2`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace/genericGrayGamma2_2).

## Parameters

- `data`: Pointer to raw bits of a client-managed buffer that is at least (  *  ) bytes in size.
- `width`: Width of the bitmap image in pixels.
- `height`: Height of the bitmap image in pixels.
- `bytesPerRow`: Number of bytes per row of data.
- `format`: Color format specifying how the colors are laid out in memory (for example,  ).

## See Also

- [init(pixelBuffer: CVPixelBuffer)](cirenderdestination/init(pixelbuffer:).md)
  Creates a render destination based on a Core Video pixel buffer.
- [init(ioSurface: IOSurface)](cirenderdestination/init(iosurface:).md)
  Creates a render destination based on an `IOSurface` object.
- [init(mtlTexture: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?)](cirenderdestination/init(mtltexture:commandbuffer:).md)
  Creates a render destination based on a Metal texture.
- [init(width: Int, height: Int, pixelFormat: MTLPixelFormat, commandBuffer: (any MTLCommandBuffer)?, mtlTextureProvider: (() -> any MTLTexture)?)](cirenderdestination/init(width:height:pixelformat:commandbuffer:mtltextureprovider:).md)
  Creates a render destination based on a Metal texture with specified pixel format.
- [init(glTexture: UInt32, target: UInt32, width: Int, height: Int)](cirenderdestination/init(gltexture:target:width:height:).md)
  Creates a render destination based on an OpenGL texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination/init(bitmapdata:width:height:bytesperrow:format:))*