# pixelBuffer

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

A CoreVideo pixel buffer containing the image data to be processed.

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

Use this property if you plan to process the image using routines that can make use of memory shared with Core Video. For example, if your image processing technology uses OpenGL or OpenGL ES, you can create a GL texture from a Core Video pixel buffer with the [`CVOpenGLBufferPool`](https://developer.apple.com/documentation/CoreVideo/CVOpenGLBufferPool) or [`CVOpenGLESTextureCache`](https://developer.apple.com/documentation/CoreVideo/CVOpenGLESTextureCache) API.

Do not modify the contents of this buffer.

## See Also

- [var baseAddress: UnsafeRawPointer](ciimageprocessorinput/baseaddress.md)
  A pointer to the image data in CPU memory to be processed.
- [var metalTexture: (any MTLTexture)?](ciimageprocessorinput/metaltexture.md)
  A Metal texture containing the image data to be processed.
- [var surface: IOSurfaceRef](ciimageprocessorinput/surface.md)
  An IOSurface object containing the image data to be processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/pixelbuffer)*