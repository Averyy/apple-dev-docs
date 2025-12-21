# CIPalettize

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a palettize filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIPalettize : CIFilterProtocol
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cipalettize/inputimage.md)
  The image to use as an input image.
- [var paletteImage: CIImage?](cipalettize/paletteimage.md)
  The input color palette, obtained by using a k-means clustering filter.
- [var perceptual: Bool](cipalettize/perceptual.md)
  A Boolean value that specifies whether the filter applies the color palette in a perceptual color space.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func palettize() -> any CIFilter & CIPalettize](cifilter-swift.class/palettize.md)
  Replaces colors with colors from a palette image.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipalettize)*