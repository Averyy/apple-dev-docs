# maskToAlpha()

**Framework**: Core Image  
**Kind**: clm

Converts an image to a white image with an alpha component.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func maskToAlpha() -> any CIFilter & CIMaskToAlpha
```

#### Return_value

The modified image.

#### Discussion

This method applies the mask-to-alpha filter to an image. The value of the alpha component is determined by the grayscale value of the input image. Black pixels become completely transparent, white pixels are completely solid.

The mask-to-alpha filter uses the following properties:

The following code creates a filter that makes the input image’s background transparent:

```swift
func maskToAlpha(inputImage: CIImage) -> CIImage {
    let maskToAlphaFilter = CIFilter.maskToAlpha()
    maskToAlphaFilter.inputImage = inputImage
    return maskToAlphaFilter.outputImage!
}
```

![Two photographs of a triangle, hexagon, circle, and a square arranged in the center of the image on a black background. In the photo on the right, a mask-to-alpha filter is applied. The image no longer has a black background and all of the white shapes are now on a transparent layer.](https://docs-assets.developer.apple.com/published/7326ac3aa0/rendered2x-1582935458.png)

## See Also

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
- [class func vignette() -> any CIFilter & CIVignette](cifilter/3228431-vignette.md)
  Gradually darkens an image’s edges.
- [class func vignetteEffect() -> any CIFilter & CIVignetteEffect](cifilter/3228430-vignetteeffect.md)
  Gradually darkens a specified area of an image.
- [class func xRay() -> any CIFilter & CIXRay](cifilter/3228433-xray.md)
  Alters an image to make it look like an X-ray image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228354-masktoalpha)*