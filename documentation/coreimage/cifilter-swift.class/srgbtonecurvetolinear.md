# sRGBToneCurveToLinear()

**Framework**: Core Image  
**Kind**: method

Converts the colors in an image from sRGB to linear.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func sRGBToneCurveToLinear() -> any CIFilter & CISRGBToneCurveToLinear
```

#### Return Value

The modified image.

#### Discussion

This method applies the sRGB-tone-curve-to-linear filter to an image. The effect converts an image in sRGB space to linear color space.

The sRGB-tone-curve-to-linear filter uses the following properties:

The following code creates a filter that converts from sRGB to linear color space.

```swift
func sRGBToLinear(inputImage: CIImage) -> CIImage {
    let sRGBToLinearFilter = CIFilter.sRGBToneCurveToLinear()
    sRGBToLinearFilter.inputImage = inputImage
    return sRGBToLinearFilter.outputImage!
}
```

![Two versions of a photograph side by side. The photo on the left shows the Golden Gate Bridge against a clear sky. In the photo on the right, a sRGB-to-linear tone curve filter is applied, and the image is considerably darker.](https://docs-assets.developer.apple.com/published/72ef711ef6c57190f761df92ef484e52/media-4333632%402x.png)

## See Also

- [class func colorAbsoluteDifference() -> any CIFilter & CIColorAbsoluteDifference](cifilter-swift.class/colorabsolutedifference.md)
  Calculates the absolute difference between each color component in the input images.
- [class func colorClamp() -> any CIFilter & CIColorClamp](cifilter-swift.class/colorclamp.md)
  Alters the colors in an image based on color components.
- [class func colorControls() -> any CIFilter & CIColorControls](cifilter-swift.class/colorcontrols.md)
  Alters the brightness, contrast, and saturation of an image’s colors.
- [class func colorMatrix() -> any CIFilter & CIColorMatrix](cifilter-swift.class/colormatrix.md)
  Alters the colors in an image based on vectors provided.
- [class func colorPolynomial() -> any CIFilter & CIColorPolynomial](cifilter-swift.class/colorpolynomial.md)
  Alters an image’s colors.
- [class func colorThreshold() -> any CIFilter & CIColorThreshold](cifilter-swift.class/colorthreshold.md)
  Compares the red, green, and blue components of the input image to a threshold and sets them to 1 or 0.
- [class func colorThresholdOtsu() -> any CIFilter & CIColorThresholdOtsu](cifilter-swift.class/colorthresholdotsu.md)
  Compares the red, green, and blue components of the input image against a threshold calculated using Otsu’s algorithm.
- [class func depthToDisparity() -> any CIFilter & CIDepthToDisparity](cifilter-swift.class/depthtodisparity.md)
  Converts from an image containing depth data to an image containing disparity data.
- [class func disparityToDepth() -> any CIFilter & CIDisparityToDepth](cifilter-swift.class/disparitytodepth.md)
  Creates depth data from an image containing disparity data.
- [class func exposureAdjust() -> any CIFilter & CIExposureAdjust](cifilter-swift.class/exposureadjust.md)
  Adjusts an image’s exposure.
- [class func gammaAdjust() -> any CIFilter & CIGammaAdjust](cifilter-swift.class/gammaadjust.md)
  Alters an image’s transition between black and white.
- [class func hueAdjust() -> any CIFilter & CIHueAdjust](cifilter-swift.class/hueadjust.md)
  Modifies an image’s hue.
- [class func linearToSRGBToneCurve() -> any CIFilter & CILinearToSRGBToneCurve](cifilter-swift.class/lineartosrgbtonecurve.md)
  Alters an image’s color intensity.
- [class func temperatureAndTint() -> any CIFilter & CITemperatureAndTint](cifilter-swift.class/temperatureandtint.md)
  Alters an image’s temperature and tint.
- [class func toneCurve() -> any CIFilter & CIToneCurve](cifilter-swift.class/tonecurve.md)
  Alters an image’s tone curve according to a series of data points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/srgbtonecurvetolinear())*