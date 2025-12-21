# CIColorMonochrome

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a color monochrome filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIColorMonochrome : CIFilterProtocol
```

## Topics

### Instance Properties
- [var color: CIColor](cicolormonochrome/color.md)
  The monochrome color to apply to the image.
- [var inputImage: CIImage?](cicolormonochrome/inputimage.md)
  The image to use as an input image.
- [var intensity: Float](cicolormonochrome/intensity.md)
  The intensity of the monochrome effect.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorMonochrome() -> any CIFilter & CIColorMonochrome](cifilter-swift.class/colormonochrome.md)
  Adjusts an image’s colors to shades of a single color.
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
- [protocol CIMaximumComponent](cimaximumcomponent.md)
  The properties you use to configure a maximum component filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolormonochrome)*