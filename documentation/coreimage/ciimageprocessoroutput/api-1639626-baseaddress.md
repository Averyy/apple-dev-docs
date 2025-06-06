# baseAddress

**Framework**: Core Image  
**Kind**: intfp  
**Required**: Yes

A pointer to CPU memory at which to write output pixel data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var baseAddress: UnsafeMutableRawPointer { get }
```

#### Discussion

Use this property if you process the image using a CPU-based routine that cannot make use of higher-level constructs for sharing memory.

> **Note**: If your image processing routine is GPU-based, use the the [`pixelBuffer`](ciimageprocessoroutput/1639647-pixelbuffer.md), [`surface`](ciimageprocessoroutput/1639627-surface.md), or [`metalTexture`](ciimageprocessoroutput/1639631-metaltexture.md) property instead.

If your image processing routine is GPU-based, use the the [`pixelBuffer`](ciimageprocessoroutput/1639647-pixelbuffer.md), [`surface`](ciimageprocessoroutput/1639627-surface.md), or [`metalTexture`](ciimageprocessoroutput/1639631-metaltexture.md) property instead.

## See Also

- [var metalTexture: (any MTLTexture)?](ciimageprocessoroutput/1639631-metaltexture.md)
  A Metal texture to which you can write output pixel data.
- [var pixelBuffer: CVPixelBuffer?](ciimageprocessoroutput/1639647-pixelbuffer.md)
  A CoreVideo pixel buffer to which you can write output pixel data.
- [var surface: IOSurfaceRef](ciimageprocessoroutput/1639627-surface.md)
  An IOSurface object to which you can write output pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/1639626-baseaddress)*