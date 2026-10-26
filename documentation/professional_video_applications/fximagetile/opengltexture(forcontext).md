# openGLTexture(forContext:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Retrieve an OpenGL texture from the [`ioSurface`](./iosurface.md) for rendering with the passed-in context. You are responsible for deleting this texture.

**Availability**:
- FxPlug 4.0+ - Deprecated in 4.3.3

> **Deprecated**: Call `CGLTexImageIOSurface2D()` to convert from IOSurface to OpenGL Texture manually.

## Declaration

```swift
func openGLTexture(forContext openGLContext: CGLContextObj!) -> GLuint
```

```objc
- (GLuint) openGLTextureForContext:(CGLContextObj) openGLContext;
```

## See Also

### Instance Methods
- [func metalTexture(for: (any MTLDevice)!) -> (any MTLTexture)!](./metaltexture%28for%29.md)
  Retrieve a Metal texture from the IOSurface for rendering on the passed-in device. The returned texture is autoreleased.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fximagetile/opengltexture(forcontext:))*