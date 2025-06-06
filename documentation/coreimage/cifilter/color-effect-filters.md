# Color Effect Filters

**Framework**: Core Image

## Topics

### Filters
- [class func colorCrossPolynomial() -> any CIFilter & CIColorCrossPolynomial](cifilter/3228286-colorcrosspolynomial.md)
  Adjusts an image’s color by applying polynomial cross-products.
- [class func colorCube() -> any CIFilter & CIColorCube](cifilter/3228287-colorcube.md)
  Adjusts an image’s pixels using a three-dimensional color table.
- [class func colorCubeWithColorSpace() -> any CIFilter & CIColorCubeWithColorSpace](cifilter/3228288-colorcubewithcolorspace.md)
  Adjusts an image’s pixels using a three-dimensional color table in specified color space.
- [class func colorCubesMixedWithMask() -> any CIFilter & CIColorCubesMixedWithMask](cifilter/3228289-colorcubesmixedwithmask.md)
  Alters an image’s pixels using a three-dimensional color tables and a mask image.
- [class func colorCurves() -> any CIFilter & CIColorCurves](cifilter/3228290-colorcurves.md)
  Adjusts an image’s color curves.
- [class func colorInvert() -> any CIFilter & CIColorInvert](cifilter/3228292-colorinvert.md)
  Inverts an image’s colors.
- [class func colorMap() -> any CIFilter & CIColorMap](cifilter/3228293-colormap.md)
  Performs a transformation of the input image colors to colors from a gradient image.
- [class func colorMonochrome() -> any CIFilter & CIColorMonochrome](cifilter/3228295-colormonochrome.md)
  Adjusts an image’s colors to shades of a single color.
- [class func colorPosterize() -> any CIFilter & CIColorPosterize](cifilter/3228297-colorposterize.md)
  Flattens an image’s colors.
- [class func convertLabToRGB() -> any CIFilter & CIConvertLab](cifilter/4401856-convertlabtorgb.md)
  Converts an image from CIELAB to RGB color space.
- [class func convertRGBtoLab() -> any CIFilter & CIConvertLab](cifilter/4401857-convertrgbtolab.md)
  Converts an image from RGB to CIELAB color space.
- [class func dither() -> any CIFilter & CIDither](cifilter/3228315-dither.md)
  Applies randomized noise to produce a processed look.
- [class func documentEnhancer() -> any CIFilter & CIDocumentEnhancer](cifilter/3228317-documentenhancer.md)
  Adjusts an image’s shadows and contrast.
- [class func falseColor() -> any CIFilter & CIFalseColor](cifilter/3228325-falsecolor.md)
  Replaces an image’s colors with specified colors.
- [class func labDeltaE() -> any CIFilter & CILabDeltaE](cifilter/3228260-labdeltae.md)
  Compares an image’s color values.
- [class func maskToAlpha() -> any CIFilter & CIMaskToAlpha](cifilter/3228354-masktoalpha.md)
  Converts an image to a white image with an alpha component.
- [class func maximumComponent() -> any CIFilter & CIMaximumComponent](cifilter/3228356-maximumcomponent.md)
  Creates a maximum RGB grayscale image.
- [class func minimumComponent() -> any CIFilter & CIMinimumComponent](cifilter/3228360-minimumcomponent.md)
  Creates a minimum RGB grayscale image.
- [class func paletteCentroid() -> any CIFilter & CIPaletteCentroid](cifilter/3228377-palettecentroid.md)
  Calculates the location of an image’s colors.
- [class func palettize() -> any CIFilter & CIPalettize](cifilter/3228378-palettize.md)
  Replaces colors with colors from a palette image.
- [class func photoEffectChrome() -> any CIFilter & CIPhotoEffect](cifilter/3228384-photoeffectchrome.md)
  Exaggerates an image’s colors.
- [class func photoEffectFade() -> any CIFilter & CIPhotoEffect](cifilter/3228385-photoeffectfade.md)
  Diminishes an image’s colors.
- [class func photoEffectInstant() -> any CIFilter & CIPhotoEffect](cifilter/3228386-photoeffectinstant.md)
  Desaturates an image’s colors.
- [class func photoEffectMono() -> any CIFilter & CIPhotoEffect](cifilter/3228387-photoeffectmono.md)
  Adjust an image’s colors to black and white.
- [class func photoEffectNoir() -> any CIFilter & CIPhotoEffect](cifilter/3228388-photoeffectnoir.md)
  Adjusts an image’s colors to black and white and intensifies the contrast.
- [class func photoEffectProcess() -> any CIFilter & CIPhotoEffect](cifilter/3228389-photoeffectprocess.md)
  Lowers the contrast of the input image.
- [class func photoEffectTonal() -> any CIFilter & CIPhotoEffect](cifilter/3228390-photoeffecttonal.md)
  Adjusts an image’s colors to black and white.
- [class func photoEffectTransfer() -> any CIFilter & CIPhotoEffect](cifilter/3228391-photoeffecttransfer.md)
  Brightens an image’s colors.
- [class func sepiaTone() -> any CIFilter & CISepiaTone](cifilter/3228402-sepiatone.md)
  Adjusts an image’s colors to shades of brown.
- [class func thermal() -> any CIFilter & CIThermal](cifilter/3228423-thermal.md)
  Alters the image to make it look like it was taken by a thermal camera.
- [class func vignetteEffect() -> any CIFilter & CIVignetteEffect](cifilter/3228430-vignetteeffect.md)
  Gradually darkens a specified area of an image.
- [class func vignette() -> any CIFilter & CIVignette](cifilter/3228431-vignette.md)
  Gradually darkens an image’s edges.
- [class func xRay() -> any CIFilter & CIXRay](cifilter/3228433-xray.md)
  Alters an image to make it look like an X-ray image.
### Protocols
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
- [protocol CIMaximumComponent](cimaximumcomponent.md)
  The properties you use to configure a maximum component filter.
- [protocol CIMinimumComponent](ciminimumcomponent.md)
  The properties you use to configure a minimum component filter.
- [protocol CIPaletteCentroid](cipalettecentroid.md)
  The properties you use to configure a palette centroid filter.
- [protocol CIPalettize](cipalettize.md)
  The properties you use to configure a palettize filter.
- [protocol CIPhotoEffect](ciphotoeffect.md)
  The properties you use to configure a photo-effect filter.
- [protocol CISepiaTone](cisepiatone.md)
  The properties you use to configure a sepia-tone filter.
- [protocol CIThermal](cithermal.md)
  The properties you use to configure a thermal filter.
- [protocol CIVignette](civignette.md)
  The properties you use to configure a vignette filter.
- [protocol CIVignetteEffect](civignetteeffect.md)
  The properties you use to configure a vignette-effect filter.
- [protocol CIXRay](cixray.md)
  The properties you use to configure an X-ray filter.

## See Also

- [protocol CIFilterProtocol](cifilterprotocol.md)
  The properties you use to configure a Core Image filter.
- [Blur Filters](cifilter/blur_filters.md)
- [Color Adjustment Filters](cifilter/color_adjustment_filters.md)
- [Composite Operations](cifilter/composite_operations.md)
- [Convolution Filters](cifilter/convolution_filters.md)
- [Distortion Filters](cifilter/distortion_filters.md)
- [Generator Filters](cifilter/generator_filters.md)
- [Geometry Adjustment Filters](cifilter/geometry_adjustment_filters.md)
- [Gradient Filters](cifilter/gradient_filters.md)
- [Halftone Effect Filters](cifilter/halftone_effect_filters.md)
- [Reduction Filters](cifilter/reduction_filters.md)
- [Sharpening Filters](cifilter/sharpening_filters.md)
- [Stylizing Filters](cifilter/stylizing_filters.md)
- [Tile Effect Filters](cifilter/tile_effect_filters.md)
- [Transition Filters](cifilter/transition_filters.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/color_effect_filters)*