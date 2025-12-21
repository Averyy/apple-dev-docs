# colorPolynomial()

**Framework**: Core Image  
**Kind**: method

Alters an image’s colors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func colorPolynomial() -> any CIFilter & CIColorPolynomial
```

#### Return Value

The modified image.

#### Discussion

This method applies the color polynomial filter to an image. The effect calculates the sum of each pixel’s color component value and the coefficient properties together to produce the output image.

The color polynomial filter uses the following properties:

The following code creates a filter that adds a lighter contrast to the input image:

```swift
func colorPolynomial(inputImage: CIImage) -> CIImage {
    let colorPolynomialFilter = CIFilter.colorPolynomial()
    colorPolynomialFilter.alphaCoefficients = CIVector (x: 0, y: 0.6, z: 0, w: 0)
    colorPolynomialFilter.redCoefficients = CIVector (x: 0, y: 1, z: 0.1, w: 0)
    colorPolynomialFilter.greenCoefficients = CIVector(x: 0, y: 1, z: 0, w: 0)
    colorPolynomialFilter.blueCoefficients = CIVector(x: 0, y: 1, z: 0, w: 0)
    colorPolynomialFilter.inputImage = inputImage
    return colorPolynomialFilter.outputImage!
}
```

![Two versions of a photograph side by side. The photo on the left shows a small bunch of flowers photographed close up, in focus, with good light and no effects. In the photo on the right, a color polynomial filter is applied, resulting in less contrast.](https://docs-assets.developer.apple.com/published/3b329edd727be8386d5fe2011d5713fa/media-3545009%402x.png)

## See Also

- [class func colorAbsoluteDifference() -> any CIFilter & CIColorAbsoluteDifference](cifilter-swift.class/colorabsolutedifference.md)
  Calculates the absolute difference between each color component in the input images.
- [class func colorClamp() -> any CIFilter & CIColorClamp](cifilter-swift.class/colorclamp.md)
  Alters the colors in an image based on color components.
- [class func colorControls() -> any CIFilter & CIColorControls](cifilter-swift.class/colorcontrols.md)
  Alters the brightness, contrast, and saturation of an image’s colors.
- [class func colorMatrix() -> any CIFilter & CIColorMatrix](cifilter-swift.class/colormatrix.md)
  Alters the colors in an image based on vectors provided.
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
- [class func sRGBToneCurveToLinear() -> any CIFilter & CISRGBToneCurveToLinear](cifilter-swift.class/srgbtonecurvetolinear.md)
  Converts the colors in an image from sRGB to linear.
- [class func temperatureAndTint() -> any CIFilter & CITemperatureAndTint](cifilter-swift.class/temperatureandtint.md)
  Alters an image’s temperature and tint.
- [class func toneCurve() -> any CIFilter & CIToneCurve](cifilter-swift.class/tonecurve.md)
  Alters an image’s tone curve according to a series of data points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/colorpolynomial())*