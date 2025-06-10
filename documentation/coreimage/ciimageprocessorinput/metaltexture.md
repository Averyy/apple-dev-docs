# metalTexture

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

A Metal texture containing the image data to be processed.

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

Use this property if you plan to process the image using a Metal shader.

Do not modify the contents of this texture.

## See Also

- [var baseAddress: UnsafeRawPointer](ciimageprocessorinput/baseaddress.md)
  A pointer to the image data in CPU memory to be processed.
- [var pixelBuffer: CVPixelBuffer?](ciimageprocessorinput/pixelbuffer.md)
  A CoreVideo pixel buffer containing the image data to be processed.
- [var surface: IOSurfaceRef](ciimageprocessorinput/surface.md)
  An IOSurface object containing the image data to be processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/metaltexture)*