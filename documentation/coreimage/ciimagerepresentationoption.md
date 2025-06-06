# CIImageRepresentationOption

**Framework**: Core Image  
**Kind**: struct

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct CIImageRepresentationOption
```

## Topics

### Initializers
- [init(rawValue: String)](ciimagerepresentationoption/3002367-init.md)
### Type Properties
- [static let avDepthData: CIImageRepresentationOption](ciimagerepresentationoption/2902265-avdepthdata.md)
  `options` dictionary key for image export methods to represent data as [`AVDepthData`](https://developer.apple.com/documentation/avfoundation/avdepthdata).
- [static let avPortraitEffectsMatte: CIImageRepresentationOption](ciimagerepresentationoption/2990467-avportraiteffectsmatte.md)
- [static let avSemanticSegmentationMattes: CIImageRepresentationOption](ciimagerepresentationoption/3325504-avsemanticsegmentationmattes.md)
- [static let depthImage: CIImageRepresentationOption](ciimagerepresentationoption/2902268-depthimage.md)
  `options` dictionary key for image export methods to output depth data.
- [static let disparityImage: CIImageRepresentationOption](ciimagerepresentationoption/2902267-disparityimage.md)
  `options` dictionary key for image export methods to output disparity data.
- [static let portraitEffectsMatteImage: CIImageRepresentationOption](ciimagerepresentationoption/2990468-portraiteffectsmatteimage.md)
- [static let semanticSegmentationGlassesMatteImage: CIImageRepresentationOption](ciimagerepresentationoption/3547088-semanticsegmentationglassesmatte.md)
- [static let semanticSegmentationHairMatteImage: CIImageRepresentationOption](ciimagerepresentationoption/3325505-semanticsegmentationhairmatteima.md)
- [static let semanticSegmentationSkinMatteImage: CIImageRepresentationOption](ciimagerepresentationoption/3325506-semanticsegmentationskinmatteima.md)
- [static let semanticSegmentationSkyMatteImage: CIImageRepresentationOption](ciimagerepresentationoption/3547089-semanticsegmentationskymatteimag.md)
- [static let semanticSegmentationTeethMatteImage: CIImageRepresentationOption](ciimagerepresentationoption/3325507-semanticsegmentationteethmatteim.md)
- [static let hdrGainMapImage: CIImageRepresentationOption](ciimagerepresentationoption/4472767-hdrgainmapimage.md)
- [static let hdrImage: CIImageRepresentationOption](ciimagerepresentationoption/4430012-hdrimage.md)

## Relationships

### Conforms To
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)

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
- [func writePNGRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any])](cicontext/2866197-writepngrepresentation.md)
  Renders the image and exports the resulting image data as a file in PNG format.
- [func writeHEIFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any])](cicontext/2902266-writeheifrepresentation.md)
  Renders the image and exports the resulting image data as a file in HEIF format.
- [func writeHEIF10Representation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any])](cicontext/3762900-writeheif10representation.md)
  Renders the image and exports the resulting image data as a file in HEIF10 format.
- [func writeOpenEXRRepresentation(of: CIImage, to: URL, options: [CIImageRepresentationOption : Any])](cicontext/4210205-writeopenexrrepresentation.md)
  Renders the image and exports the resulting image data as a file in open EXR format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimagerepresentationoption)*