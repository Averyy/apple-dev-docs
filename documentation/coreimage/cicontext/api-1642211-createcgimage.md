# createCGImage(_:from:format:colorSpace:deferred:)

**Framework**: Core Image  
**Kind**: instm

Creates a Quartz 2D image from a region of a Core Image image object with deferred rendering.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func createCGImage(_ image: CIImage, from fromRect: CGRect, format: CIFormat, colorSpace: CGColorSpace?, deferred: Bool) -> CGImage?
```

#### Return_value

A Quartz 2D image. You are responsible for releasing the returned image when you no longer need it.

#### Discussion

Renders a region of an image into a temporary buffer using the context, and then creates and returns a Quartz 2D image with the results.

## Parameters

- `image`: A Core Image image object.
- `fromRect`: The region of the image to render.
- `format`: The pixel format of the image.
- `colorSpace`: The color space for the output image. This color space must conform to either the   or   model and be compatible with the specified pixel format.
- `deferred`: If  , Core Image delays rendering until the output Quartz 2D image is itself to be rendered. If  , Core Image renders to the output Quartz 2D image immediately.

## See Also

- [func createCGImage(CIImage, from: CGRect) -> CGImage?](cicontext/1437784-createcgimage.md)
  Creates a Quartz 2D image from a region of a Core Image image object.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?) -> CGImage?](cicontext/1437978-createcgimage.md)
  Creates a Quartz 2D image from a region of a Core Image image object.
- [func render(CIImage, toBitmap: UnsafeMutableRawPointer, rowBytes: Int, bounds: CGRect, format: CIFormat, colorSpace: CGColorSpace?)](cicontext/1437897-render.md)
  Renders to the given bitmap. 
- [func render(CIImage, to: CVPixelBuffer)](cicontext/1437853-render.md)
  Renders an image into a pixel buffer.
- [func render(CIImage, to: CVPixelBuffer, bounds: CGRect, colorSpace: CGColorSpace?)](cicontext/1437835-render.md)
  Renders a region of an image into a pixel buffer.
- [func render(CIImage, to: IOSurfaceRef, bounds: CGRect, colorSpace: CGColorSpace?)](cicontext/1437778-render.md)
  Renders a region of an image into an IOSurface object.
- [func render(CIImage, to: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?, bounds: CGRect, colorSpace: CGColorSpace)](cicontext/1438026-render.md)
  Renders a region of an image to a Metal texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/1642211-createcgimage)*