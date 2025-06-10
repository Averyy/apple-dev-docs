# pngRepresentation(of:format:colorSpace:options:)

**Framework**: Core Image  
**Kind**: method

Renders the image and exports the resulting image data in PNG format.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func pngRepresentation(of image: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any] = [:]) -> Data?
```

#### Return Value

A data representation of the rendered image in PNG format, or `nil` if the image could not be rendered.

#### Discussion

To render an image for export, the image’s contents must not be empty and its [`extent`](ciimage/extent.md) dimensions must be finite. To export after applying a filter whose output has infinite extent, see the [`clampedToExtent()`](ciimage/clampedtoextent().md) method.

## Parameters

- `image`: The image object to render.
- `format`: The pixel format for the output image.
- `colorSpace`: The color space in which to render the output image. This color space must conform to either the   or   model and must be compatible with the specified pixel format.
- `options`: No options keys are supported at this time.

## See Also

- [func tiffRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/tiffrepresentation(of:format:colorspace:options:).md)
  Renders the image and exports the resulting image data in TIFF format.
- [func jpegRepresentation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/jpegrepresentation(of:colorspace:options:).md)
  Renders the image and exports the resulting image data in JPEG format.
- [func heifRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/heifrepresentation(of:format:colorspace:options:).md)
  Renders the image and exports the resulting image data in HEIF format.
- [func heif10Representation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws -> Data](cicontext/heif10representation(of:colorspace:options:).md)
  Renders the image and exports the resulting image data in HEIF10 format.
- [func openEXRRepresentation(of: CIImage, options: [CIImageRepresentationOption : Any]) throws -> Data](cicontext/openexrrepresentation(of:options:).md)
  Renders the image and exports the resulting image data in open EXR format.
- [func writeTIFFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writetiffrepresentation(of:to:format:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in TIFF format.
- [func writeJPEGRepresentation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writejpegrepresentation(of:to:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in JPEG format.
- [func writePNGRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writepngrepresentation(of:to:format:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in PNG format.
- [func writeHEIFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writeheifrepresentation(of:to:format:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in HEIF format.
- [func writeHEIF10Representation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writeheif10representation(of:to:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in HEIF10 format.
- [func writeOpenEXRRepresentation(of: CIImage, to: URL, options: [CIImageRepresentationOption : Any]) throws](cicontext/writeopenexrrepresentation(of:to:options:).md)
  Renders the image and exports the resulting image data as a file in open EXR format.
- [struct CIImageRepresentationOption](ciimagerepresentationoption.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/pngrepresentation(of:format:colorspace:options:))*