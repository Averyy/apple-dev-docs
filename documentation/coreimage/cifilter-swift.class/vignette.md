# vignette()

**Framework**: Core Image  
**Kind**: method

Gradually darkens an image’s edges.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func vignette() -> any CIFilter & CIVignette
```

#### Return Value

The modified image.

#### Discussion

This method applies the vignette filter to an image. This is a preconfigured effect that reduces brightness of the image at the periphery.

The vignette filter uses the following properties:

The following code creates a filter that darkens the edges of the input image:

```swift
func vignette(inputImage: CIImage ) -> CIImage {
    let vignetteFilter = CIFilter.vignette()
    vignetteFilter.inputImage = inputImage
    vignetteFilter.intensity = 4
    vignetteFilter.radius = 10
    return vignetteFilter.outputImage!
}
```

![Two pictures of a pink flower surrounded by foliage. The photo on the left shows a single flower photographed close-up, in focus, with good light and no effects. In the photo on the right, a vignette filter is applied, resulting in a gradual reduction of an image’s brightness and reduction of saturation in the periphery. ](https://docs-assets.developer.apple.com/published/4d8fc4e34d77f0640e1d618ee6f839d0/media-3545014%402x.png)

## See Also

- [class func colorCrossPolynomial() -> any CIFilter & CIColorCrossPolynomial](cifilter-swift.class/colorcrosspolynomial.md)
  Adjusts an image’s color by applying polynomial cross-products.
- [class func colorCube() -> any CIFilter & CIColorCube](cifilter-swift.class/colorcube.md)
  Adjusts an image’s pixels using a three-dimensional color table.
- [class func colorCubeWithColorSpace() -> any CIFilter & CIColorCubeWithColorSpace](cifilter-swift.class/colorcubewithcolorspace.md)
  Adjusts an image’s pixels using a three-dimensional color table in specified color space.
- [class func colorCubesMixedWithMask() -> any CIFilter & CIColorCubesMixedWithMask](cifilter-swift.class/colorcubesmixedwithmask.md)
  Alters an image’s pixels using a three-dimensional color tables and a mask image.
- [class func colorCurves() -> any CIFilter & CIColorCurves](cifilter-swift.class/colorcurves.md)
  Adjusts an image’s color curves.
- [class func colorInvert() -> any CIFilter & CIColorInvert](cifilter-swift.class/colorinvert.md)
  Inverts an image’s colors.
- [class func colorMap() -> any CIFilter & CIColorMap](cifilter-swift.class/colormap.md)
  Performs a transformation of the input image colors to colors from a gradient image.
- [class func colorMonochrome() -> any CIFilter & CIColorMonochrome](cifilter-swift.class/colormonochrome.md)
  Adjusts an image’s colors to shades of a single color.
- [class func colorPosterize() -> any CIFilter & CIColorPosterize](cifilter-swift.class/colorposterize.md)
  Flattens an image’s colors.
- [class func convertLabToRGB() -> any CIFilter & CIConvertLab](cifilter-swift.class/convertlabtorgb.md)
  Converts an image from CIELAB to RGB color space.
- [class func convertRGBtoLab() -> any CIFilter & CIConvertLab](cifilter-swift.class/convertrgbtolab.md)
  Converts an image from RGB to CIELAB color space.
- [class func dither() -> any CIFilter & CIDither](cifilter-swift.class/dither.md)
  Applies randomized noise to produce a processed look.
- [class func documentEnhancer() -> any CIFilter & CIDocumentEnhancer](cifilter-swift.class/documentenhancer.md)
  Adjusts an image’s shadows and contrast.
- [class func falseColor() -> any CIFilter & CIFalseColor](cifilter-swift.class/falsecolor.md)
  Replaces an image’s colors with specified colors.
- [class func labDeltaE() -> any CIFilter & CILabDeltaE](cifilter-swift.class/labdeltae.md)
  Compares an image’s color values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/vignette())*