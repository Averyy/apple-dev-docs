# CIPhotoEffect

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a photo-effect filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIPhotoEffect : CIFilterProtocol
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](ciphotoeffect/inputimage.md)
  The image to use as an input image.
- [var extrapolate: Bool](ciphotoeffect/extrapolate.md)
  Extrapolate for RGB values outside of the range 0.0 to 1.0.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func photoEffectChrome() -> any CIFilter & CIPhotoEffect](cifilter-swift.class/photoeffectchrome.md)
  Exaggerates an image’s colors.
- [class func photoEffectFade() -> any CIFilter & CIPhotoEffect](cifilter-swift.class/photoeffectfade.md)
  Diminishes an image’s colors.
- [class func photoEffectInstant() -> any CIFilter & CIPhotoEffect](cifilter-swift.class/photoeffectinstant.md)
  Desaturates an image’s colors.
- [class func photoEffectMono() -> any CIFilter & CIPhotoEffect](cifilter-swift.class/photoeffectmono.md)
  Adjust an image’s colors to black and white.
- [class func photoEffectNoir() -> any CIFilter & CIPhotoEffect](cifilter-swift.class/photoeffectnoir.md)
  Adjusts an image’s colors to black and white and intensifies the contrast.
- [class func photoEffectProcess() -> any CIFilter & CIPhotoEffect](cifilter-swift.class/photoeffectprocess.md)
  Lowers the contrast of the input image.
- [class func photoEffectTonal() -> any CIFilter & CIPhotoEffect](cifilter-swift.class/photoeffecttonal.md)
  Adjusts an image’s colors to black and white.
- [class func photoEffectTransfer() -> any CIFilter & CIPhotoEffect](cifilter-swift.class/photoeffecttransfer.md)
  Brightens an image’s colors.
- [protocol CIColorCrossPolynomial](cicolorcrosspolynomial.md)
  The properties you use to configure a color cross-polynomial filter.
- [protocol CIColorCube](cicolorcube.md)
  The properties you use to configure a color cube filter.
- [protocol CIColorCubeWithColorSpace](cicolorcubewithcolorspace.md)
  The properties you use to configure a color cube with color space filter.
- [protocol CIColorCubesMixedWithMask](cicolorcubesmixedwithmask.md)
  The properties you use to configure a color cube mixed with mask filter.
- [protocol CIColorCurves](cicolorcurves.md)
  The properties you use to configure a color curves filter.
- [protocol CIColorInvert](cicolorinvert.md)
  The properties you use to configure a color invert filter.
- [protocol CIColorMap](cicolormap.md)
  The properties you use to configure a color map filter.
- [protocol CIColorMonochrome](cicolormonochrome.md)
  The properties you use to configure a color monochrome filter.
- [protocol CIConvertLab](ciconvertlab.md)
- [protocol CIDither](cidither.md)
  The properties you use to configure a dither filter.
- [protocol CIColorPosterize](cicolorposterize.md)
  The properties you use to configure a color posterize filter.
- [protocol CIDocumentEnhancer](cidocumentenhancer.md)
  The properties you use to configure a document enhancer filter.
- [protocol CIFalseColor](cifalsecolor.md)
  The properties you use to configure a false color filter.
- [protocol CILabDeltaE](cilabdeltae.md)
  The properties you use to configure a Lab Delta E filter.
- [protocol CIMaskToAlpha](cimasktoalpha.md)
  The properties you use to configure a mask-to-alpha filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciphotoeffect)*