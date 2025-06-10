# createCGImage(_:from:format:colorSpace:)

**Framework**: Core Image  
**Kind**: method

Creates a Quartz 2D image from a region of a Core Image image object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func createCGImage(_ image: CIImage, from fromRect: CGRect, format: CIFormat, colorSpace: CGColorSpace?) -> CGImage?
```

#### Return Value

A Quartz 2D image. You are responsible for releasing the returned image when you no longer need it.

#### Discussion

Renders a region of an image into a temporary buffer using the context, and then creates and returns a Quartz 2D image with the results.

## Parameters

- `image`: A Core Image image object.
- `fromRect`: The region of the image to render.
- `format`: The pixel format of the image.
- `colorSpace`: The color space for the output image. This color space must conform to either the   or   model and be compatible with the specified pixel format.

## See Also

- [func createCGImage(CIImage, from: CGRect) -> CGImage?](cicontext/createcgimage(_:from:).md)
  Creates a Quartz 2D image from a region of a Core Image image object.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?, deferred: Bool) -> CGImage?](cicontext/createcgimage(_:from:format:colorspace:deferred:).md)
  Creates a Quartz 2D image from a region of a Core Image image object with deferred rendering.
- [func render(CIImage, toBitmap: UnsafeMutableRawPointer, rowBytes: Int, bounds: CGRect, format: CIFormat, colorSpace: CGColorSpace?)](cicontext/render(_:tobitmap:rowbytes:bounds:format:colorspace:).md)
  Renders to the given bitmap.
- [func render(CIImage, to: CVPixelBuffer)](cicontext/render(_:to:).md)
  Renders an image into a pixel buffer.
- [func render(CIImage, to: CVPixelBuffer, bounds: CGRect, colorSpace: CGColorSpace?)](cicontext/render(_:to:bounds:colorspace:)-2k8l2.md)
  Renders a region of an image into a pixel buffer.
- [func render(CIImage, to: IOSurfaceRef, bounds: CGRect, colorSpace: CGColorSpace?)](cicontext/render(_:to:bounds:colorspace:)-54b9l.md)
  Renders a region of an image into an IOSurface object.
- [func render(CIImage, to: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?, bounds: CGRect, colorSpace: CGColorSpace)](cicontext/render(_:to:commandbuffer:bounds:colorspace:).md)
  Renders a region of an image to a Metal texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/createcgimage(_:from:format:colorspace:))*