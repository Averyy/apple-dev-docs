# CIImageRepresentationOption

**Framework**: Core Image  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct CIImageRepresentationOption
```

## Topics

### Initializers
- [init(rawValue: String)](ciimagerepresentationoption/init(rawvalue:).md)
### Type Properties
- [static let avDepthData: CIImageRepresentationOption](ciimagerepresentationoption/avdepthdata.md)
  The depth data representation of an image.
- [static let avPortraitEffectsMatte: CIImageRepresentationOption](ciimagerepresentationoption/avportraiteffectsmatte.md)
- [static let avSemanticSegmentationMattes: CIImageRepresentationOption](ciimagerepresentationoption/avsemanticsegmentationmattes.md)
- [static let depthImage: CIImageRepresentationOption](ciimagerepresentationoption/depthimage.md)
  `options` dictionary key for image export methods to output depth data.
- [static let disparityImage: CIImageRepresentationOption](ciimagerepresentationoption/disparityimage.md)
  `options` dictionary key for image export methods to output disparity data.
- [static let portraitEffectsMatteImage: CIImageRepresentationOption](ciimagerepresentationoption/portraiteffectsmatteimage.md)
- [static let semanticSegmentationGlassesMatteImage: CIImageRepresentationOption](ciimagerepresentationoption/semanticsegmentationglassesmatteimage.md)
- [static let semanticSegmentationHairMatteImage: CIImageRepresentationOption](ciimagerepresentationoption/semanticsegmentationhairmatteimage.md)
- [static let semanticSegmentationSkinMatteImage: CIImageRepresentationOption](ciimagerepresentationoption/semanticsegmentationskinmatteimage.md)
- [static let semanticSegmentationSkyMatteImage: CIImageRepresentationOption](ciimagerepresentationoption/semanticsegmentationskymatteimage.md)
- [static let semanticSegmentationTeethMatteImage: CIImageRepresentationOption](ciimagerepresentationoption/semanticsegmentationteethmatteimage.md)
- [static let hdrImage: CIImageRepresentationOption](ciimagerepresentationoption/hdrimage.md)
- [static let hdrGainMapAsRGB: CIImageRepresentationOption](ciimagerepresentationoption/hdrgainmapasrgb.md)
  An optional key and value to request the gain map channel to be color instead of monochrome.
- [static let hdrGainMapImage: CIImageRepresentationOption](ciimagerepresentationoption/hdrgainmapimage.md)
  An optional key and value to save a gain map channel to a JPEG or HEIF.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func tiffRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/tiffrepresentation(of:format:colorspace:options:).md)
  Renders the image and exports the resulting image data in TIFF format.
- [func jpegRepresentation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/jpegrepresentation(of:colorspace:options:).md)
  Renders the image and exports the resulting image data in JPEG format.
- [func pngRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/pngrepresentation(of:format:colorspace:options:).md)
  Renders the image and exports the resulting image data in PNG format.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimagerepresentationoption)*