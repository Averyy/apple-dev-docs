# surface

**Framework**: Core Image  
**Kind**: intfp  
**Required**: Yes

An IOSurface object to which you can write output pixel data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var surface: IOSurfaceRef { get }
```

#### Discussion

Use this property if you plan to process the image using routines that can make use of memory shared with other processes or technologies.

## See Also

- [var baseAddress: UnsafeMutableRawPointer](ciimageprocessoroutput/1639626-baseaddress.md)
  A pointer to CPU memory at which to write output pixel data.
- [var metalTexture: (any MTLTexture)?](ciimageprocessoroutput/1639631-metaltexture.md)
  A Metal texture to which you can write output pixel data.
- [var pixelBuffer: CVPixelBuffer?](ciimageprocessoroutput/1639647-pixelbuffer.md)
  A CoreVideo pixel buffer to which you can write output pixel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/1639627-surface)*