# baseAddress

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

A pointer to the image data in CPU memory to be processed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var baseAddress: UnsafeRawPointer { get }
```

#### Discussion

Use this property if you plan to process the image using a CPU-based routine that cannot make use of higher-level constructs for sharing memory.

> **Note**:  If your image processing routine is GPU-based, use the the [`pixelBuffer`](ciimageprocessorinput/pixelbuffer.md), [`surface`](ciimageprocessorinput/surface.md), or [`metalTexture`](ciimageprocessorinput/metaltexture.md) property instead.

Do not modify the memory addressed by this pointer.

## See Also

- [var metalTexture: (any MTLTexture)?](ciimageprocessorinput/metaltexture.md)
  A Metal texture containing the image data to be processed.
- [var pixelBuffer: CVPixelBuffer?](ciimageprocessorinput/pixelbuffer.md)
  A CoreVideo pixel buffer containing the image data to be processed.
- [var surface: IOSurfaceRef](ciimageprocessorinput/surface.md)
  An IOSurface object containing the image data to be processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/baseaddress)*