# metalTexture(for:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Retrieve a Metal texture from the IOSurface for rendering on the passed-in device. The returned texture is autoreleased.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func metalTexture(for metalDevice: (any MTLDevice)!) -> (any MTLTexture)!
```

```objc
- (id<MTLTexture>) metalTextureForDevice:(id<MTLDevice>) metalDevice;
```

## See Also

### Instance Methods
- [func openGLTexture(forContext: CGLContextObj!) -> GLuint](./opengltexture%28forcontext%29.md)
  Retrieve an OpenGL texture from the [`ioSurface`](./iosurface.md) for rendering with the passed-in context. You are responsible for deleting this texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fximagetile/metaltexture(for:))*