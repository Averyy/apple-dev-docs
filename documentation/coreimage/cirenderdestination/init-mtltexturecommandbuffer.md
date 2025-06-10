# init(mtlTexture:commandBuffer:)

**Framework**: Core Image  
**Kind**: init

Creates a render destination based on a Metal texture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(mtlTexture texture: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?)
```

#### Return Value

A [`CIRenderDestination`](cirenderdestination.md) object for rendering to a Metal buffer.

#### Discussion

Rendering to a [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture)-backed [`CIRenderDestination`](cirenderdestination.md) is supported by only [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture)-backed [`CIContext`](cicontext.md) objects.  The texture must have [`MTLTextureType`](https://developer.apple.com/documentation/Metal/MTLTextureType) of [`MTLTextureType.type2D`](https://developer.apple.com/documentation/Metal/MTLTextureType/type2D).

The destination’s [`colorSpace`](cirenderdestination/colorspace.md) property will default to a [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) created with [`sRGB`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace/sRGB), [`extendedSRGB`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace/extendedSRGB), or [`genericGrayGamma2_2`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace/genericGrayGamma2_2).

## Parameters

- `texture`: The   object for rendering with   of  .
- `commandBuffer`: An optional   to use for rendering to the   destination.

## See Also

- [init(pixelBuffer: CVPixelBuffer)](cirenderdestination/init(pixelbuffer:).md)
  Creates a render destination based on a Core Video pixel buffer.
- [init(ioSurface: IOSurface)](cirenderdestination/init(iosurface:).md)
  Creates a render destination based on an `IOSurface` object.
- [init(width: Int, height: Int, pixelFormat: MTLPixelFormat, commandBuffer: (any MTLCommandBuffer)?, mtlTextureProvider: (() -> any MTLTexture)?)](cirenderdestination/init(width:height:pixelformat:commandbuffer:mtltextureprovider:).md)
  Creates a render destination based on a Metal texture with specified pixel format.
- [init(glTexture: UInt32, target: UInt32, width: Int, height: Int)](cirenderdestination/init(gltexture:target:width:height:).md)
  Creates a render destination based on an OpenGL texture.
- [init(bitmapData: UnsafeMutableRawPointer, width: Int, height: Int, bytesPerRow: Int, format: CIFormat)](cirenderdestination/init(bitmapdata:width:height:bytesperrow:format:).md)
  Creates a render destination based on a client-managed buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination/init(mtltexture:commandbuffer:))*