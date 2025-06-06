# surface

**Framework**: Core Image  
**Kind**: intfp  
**Required**: Yes

An IOSurface object containing the image data to be processed.

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

Do not modify the contents of this surface.

## See Also

- [var baseAddress: UnsafeRawPointer](ciimageprocessorinput/1639645-baseaddress.md)
  A pointer to the image data in CPU memory to be processed.
- [var metalTexture: (any MTLTexture)?](ciimageprocessorinput/1639651-metaltexture.md)
  A Metal texture containing the image data to be processed.
- [var pixelBuffer: CVPixelBuffer?](ciimageprocessorinput/1639649-pixelbuffer.md)
  A CoreVideo pixel buffer containing the image data to be processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/1639657-surface)*