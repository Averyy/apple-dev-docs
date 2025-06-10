# metalTexture

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

A Metal texture to which you can write output pixel data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var metalTexture: (any MTLTexture)? { get }
```

#### Discussion

For image processing using a Metal shader, bind this texture as an attachment in a render pass or as an output texture in a compute pass.

## See Also

- [var baseAddress: UnsafeMutableRawPointer](ciimageprocessoroutput/baseaddress.md)
  A pointer to CPU memory at which to write output pixel data.
- [var pixelBuffer: CVPixelBuffer?](ciimageprocessoroutput/pixelbuffer.md)
  A CoreVideo pixel buffer to which you can write output pixel data.
- [var surface: IOSurfaceRef](ciimageprocessoroutput/surface.md)
  An IOSurface object to which you can write output pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/metaltexture)*