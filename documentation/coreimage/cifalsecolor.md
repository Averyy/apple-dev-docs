# CIFalseColor

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a false color filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIFalseColor : CIFilterProtocol
```

## Topics

### Instance Properties
- [var color0: CIColor](cifalsecolor/color0.md)
  The first color to use for the color ramp.
- [var color1: CIColor](cifalsecolor/color1.md)
  The second color to use for the color ramp.
- [var inputImage: CIImage?](cifalsecolor/inputimage.md)
  The image to use as an input image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func falseColor() -> any CIFilter & CIFalseColor](cifilter-swift.class/falsecolor.md)
  Replaces an image’s colors with specified colors.
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
- [protocol CILabDeltaE](cilabdeltae.md)
  The properties you use to configure a Lab Delta E filter.
- [protocol CIMaskToAlpha](cimasktoalpha.md)
  The properties you use to configure a mask-to-alpha filter.
- [protocol CIMaximumComponent](cimaximumcomponent.md)
  The properties you use to configure a maximum component filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifalsecolor)*