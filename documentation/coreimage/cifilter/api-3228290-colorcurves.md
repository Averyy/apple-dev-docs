# colorCurves()

**Framework**: Core Image  
**Kind**: clm

Adjusts an image’s color curves.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func colorCurves() -> any CIFilter & CIColorCurves
```

#### Return_value

The modified image.

#### Discussion

This method applies the color curves filter to an image. The effect uses a three-channel one-dimensional color table to transform the source image pixels. The color table must be comprised of floating-point RGB value.

The color curves filter uses the following properties:

The following code creates a filter that adds brightness to the input image:

```swift
func colorCurves(inputImage: CIImage) -> CIImage {
    let colorCurvesEffect = CIFilter.colorCurves()
    colorCurvesEffect.inputImage = inputImage
    colorCurvesEffect.curvesDomain = CIVector(x: 0, y: 1)
    colorCurvesEffect.curvesData = Data(
        bytes: [Float32]([
            0.0,0.0,0.0,
            0.8,0.8,0.8,
            1.0,1.0,1.0
        ]), count: 36)
    colorCurvesEffect.colorSpace = CGColorSpaceCreateDeviceRGB()
    return colorCurvesEffect.outputImage!
}
```

![Two pictures of a pink flower surrounded by foliage. The photo on the left shows a single flower photographed close-up, in focus, with good light and no effects. In the photo on the right, a color curves filter is applied, resulting in the photo becoming brighter.](https://docs-assets.developer.apple.com/published/fd664835dc/rendered2x-1582930199.png)

## See Also

- [class func colorCrossPolynomial() -> any CIFilter & CIColorCrossPolynomial](cifilter/3228286-colorcrosspolynomial.md)
  Adjusts an image’s color by applying polynomial cross-products.
- [class func colorCube() -> any CIFilter & CIColorCube](cifilter/3228287-colorcube.md)
  Adjusts an image’s pixels using a three-dimensional color table.
- [class func colorCubeWithColorSpace() -> any CIFilter & CIColorCubeWithColorSpace](cifilter/3228288-colorcubewithcolorspace.md)
  Adjusts an image’s pixels using a three-dimensional color table in specified color space.
- [class func colorCubesMixedWithMask() -> any CIFilter & CIColorCubesMixedWithMask](cifilter/3228289-colorcubesmixedwithmask.md)
  Alters an image’s pixels using a three-dimensional color tables and a mask image.
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
- [class func vignette() -> any CIFilter & CIVignette](cifilter/3228431-vignette.md)
  Gradually darkens an image’s edges.
- [class func vignetteEffect() -> any CIFilter & CIVignetteEffect](cifilter/3228430-vignetteeffect.md)
  Gradually darkens a specified area of an image.
- [class func xRay() -> any CIFilter & CIXRay](cifilter/3228433-xray.md)
  Alters an image to make it look like an X-ray image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228290-colorcurves)*