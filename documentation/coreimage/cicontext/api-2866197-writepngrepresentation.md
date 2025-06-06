# writePNGRepresentation(of:to:format:colorSpace:options:)

**Framework**: Core Image  
**Kind**: instm

Renders the image and exports the resulting image data as a file in PNG format.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func writePNGRepresentation(of image: CIImage, to url: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any] = [:]) throws
```

#### Return_value

If [`true`](https://developer.apple.com/documentation/swift/true), file export succeeded. If [`false`](https://developer.apple.com/documentation/swift/false), examine the `errorPtr` parameter for possible failure reasons.

#### Discussion

To render an image for export, the image’s contents must not be empty and its [`extent`](ciimage/1437996-extent.md) dimensions must be finite. To export after applying a filter whose output has infinite extent, see the [`clampedToExtent()`](ciimage/1437628-clampedtoextent.md) method.

## Parameters

- `image`: The image object to render.
- `url`: The file URL at which to write the output PNG file.
- `format`: The pixel format for the output image.
- `colorSpace`: The color space in which to render the output image. This color space must conform to either the   or   model and must be compatible with the specified pixel format.
- `options`: A dictionary with additional options for export.

## See Also

- [func tiffRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/1642220-tiffrepresentation.md)
  Renders the image and exports the resulting image data in TIFF format.
- [func jpegRepresentation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/1642214-jpegrepresentation.md)
  Renders the image and exports the resulting image data in JPEG format.
- [func pngRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/2866196-pngrepresentation.md)
  Renders the image and exports the resulting image data in PNG format.
- [func heifRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/2902269-heifrepresentation.md)
  Renders the image and exports the resulting image data in HEIF format.
- [func heif10Representation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data](cicontext/3762899-heif10representation.md)
  Renders the image and exports the resulting image data in HEIF10 format.
- [func openEXRRepresentation(of: CIImage, options: [CIImageRepresentationOption : Any]) -> Data](cicontext/4210204-openexrrepresentation.md)
  Renders the image and exports the resulting image data in open EXR format.
- [func writeTIFFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any])](cicontext/1642213-writetiffrepresentation.md)
  Renders the image and exports the resulting image data as a file in TIFF format.
- [func writeJPEGRepresentation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any])](cicontext/1642218-writejpegrepresentation.md)
  Renders the image and exports the resulting image data as a file in JPEG format.
- [func writeHEIFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any])](cicontext/2902266-writeheifrepresentation.md)
  Renders the image and exports the resulting image data as a file in HEIF format.
- [func writeHEIF10Representation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any])](cicontext/3762900-writeheif10representation.md)
  Renders the image and exports the resulting image data as a file in HEIF10 format.
- [func writeOpenEXRRepresentation(of: CIImage, to: URL, options: [CIImageRepresentationOption : Any])](cicontext/4210205-writeopenexrrepresentation.md)
  Renders the image and exports the resulting image data as a file in open EXR format.
- [struct CIImageRepresentationOption](ciimagerepresentationoption.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/2866197-writepngrepresentation)*