# heif10Representation(of:colorSpace:options:)

**Framework**: Core Image  
**Kind**: method

Renders the image and exports the resulting image data in HEIF10 format.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func heif10Representation(of image: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any] = [:]) throws -> Data
```

## Parameters

- `image`: The image object to render.
- `colorSpace`: The color space in which to render the output image.
- `options`: A dictionary with additional options for export.

## See Also

- [func tiffRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/tiffrepresentation(of:format:colorspace:options:).md)
  Renders the image and exports the resulting image data in TIFF format.
- [func jpegRepresentation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/jpegrepresentation(of:colorspace:options:).md)
  Renders the image and exports the resulting image data in JPEG format.
- [func pngRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/pngrepresentation(of:format:colorspace:options:).md)
  Renders the image and exports the resulting image data in PNG format.
- [func heifRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/heifrepresentation(of:format:colorspace:options:).md)
  Renders the image and exports the resulting image data in HEIF format.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/heif10representation(of:colorspace:options:))*