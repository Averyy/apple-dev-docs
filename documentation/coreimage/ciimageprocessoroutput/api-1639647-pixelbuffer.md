# pixelBuffer

**Framework**: Core Image  
**Kind**: intfp  
**Required**: Yes

A CoreVideo pixel buffer to which you can write output pixel data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var pixelBuffer: CVPixelBuffer? { get }
```

#### Discussion

Use this property to process the image using routines that can make use of memory shared with Core Video. For example, if your image processing technology uses OpenGL or OpenGL ES, you can create a GL texture from a Core Video pixel buffer with the [`CVOpenGLBufferPool`](https://developer.apple.com/documentation/corevideo/cvopenglbufferpool) or [`CVOpenGLESTextureCache`](https://developer.apple.com/documentation/corevideo/cvopenglestexturecache) API.

## See Also

- [var baseAddress: UnsafeMutableRawPointer](ciimageprocessoroutput/1639626-baseaddress.md)
  A pointer to CPU memory at which to write output pixel data.
- [var metalTexture: (any MTLTexture)?](ciimageprocessoroutput/1639631-metaltexture.md)
  A Metal texture to which you can write output pixel data.
- [var surface: IOSurfaceRef](ciimageprocessoroutput/1639627-surface.md)
  An IOSurface object to which you can write output pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/1639647-pixelbuffer)*