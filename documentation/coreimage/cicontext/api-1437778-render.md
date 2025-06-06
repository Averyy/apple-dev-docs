# render(_:to:bounds:colorSpace:)

**Framework**: Core Image  
**Kind**: instm

Renders a region of an image into an IOSurface object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func render(_ image: CIImage, to surface: IOSurfaceRef, bounds: CGRect, colorSpace: CGColorSpace?)
```

## Parameters

- `image`: A Core Image image object.
- `surface`: The destination IOSurface object.
- `r`: The rectangle in the destination IOSurface object to draw into.
- `cs`: The color space of the destination IOSurface object.

## See Also

- [func createCGImage(CIImage, from: CGRect) -> CGImage?](cicontext/1437784-createcgimage.md)
  Creates a Quartz 2D image from a region of a Core Image image object.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?) -> CGImage?](cicontext/1437978-createcgimage.md)
  Creates a Quartz 2D image from a region of a Core Image image object.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?, deferred: Bool) -> CGImage?](cicontext/1642211-createcgimage.md)
  Creates a Quartz 2D image from a region of a Core Image image object with deferred rendering.
- [func render(CIImage, toBitmap: UnsafeMutableRawPointer, rowBytes: Int, bounds: CGRect, format: CIFormat, colorSpace: CGColorSpace?)](cicontext/1437897-render.md)
  Renders to the given bitmap. 
- [func render(CIImage, to: CVPixelBuffer)](cicontext/1437853-render.md)
  Renders an image into a pixel buffer.
- [func render(CIImage, to: CVPixelBuffer, bounds: CGRect, colorSpace: CGColorSpace?)](cicontext/1437835-render.md)
  Renders a region of an image into a pixel buffer.
- [func render(CIImage, to: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?, bounds: CGRect, colorSpace: CGColorSpace)](cicontext/1438026-render.md)
  Renders a region of an image to a Metal texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/1437778-render)*