# temperatureAndTint()

**Framework**: Core Image  
**Kind**: clm

Alters an image’s temperature and tint.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func temperatureAndTint() -> any CIFilter & CITemperatureAndTint
```

#### Return_value

The modified image.

#### Discussion

This method applies the image temperature and tint filter to an image. The effect adjusts the white balance of the input image to match the `targetNeutral` property, resulting in a cooler or warmer tone image.

The temperature and tint filter uses the following properties:

The following code creates a filter that adds an orange hue to the input image:

```swift
func tempatureAndTint(inputImage: CIImage) -> CIImage {
    let tempatureAndTintFilter = CIFilter.temperatureAndTint()
    tempatureAndTintFilter.inputImage = inputImage
    tempatureAndTintFilter.neutral = CIVector(x: 11500, y: 10)
    tempatureAndTintFilter.targetNeutral = CIVector(x: 4000, y: 0)
    return tempatureAndTintFilter.outputImage!
}
```

![Two versions of a photograph side by side. The photo on the left shows a small bunch of flowers photographed close up, in focus, with good light and no effects. In the photo on the right, a temperature and tint filter is applied, resulting in a orange hue applied to the image.](https://docs-assets.developer.apple.com/published/56810f936f/rendered2x-1582929816.png)

## See Also

- [class func colorAbsoluteDifference() -> any CIFilter & CIColorAbsoluteDifference](cifilter/3547119-colorabsolutedifference.md)
  Calculates the absolute difference between each color component in the input images.
- [class func colorClamp() -> any CIFilter & CIColorClamp](cifilter/3228284-colorclamp.md)
  Alters the colors in an image based on color components.
- [class func colorControls() -> any CIFilter & CIColorControls](cifilter/3228285-colorcontrols.md)
  Alters the brightness, contrast, and saturation of an image’s colors.
- [class func colorMatrix() -> any CIFilter & CIColorMatrix](cifilter/3228294-colormatrix.md)
  Alters the colors in an image based on vectors provided.
- [class func colorPolynomial() -> any CIFilter & CIColorPolynomial](cifilter/3228296-colorpolynomial.md)
  Alters an image’s colors.
- [class func colorThreshold() -> any CIFilter & CIColorThreshold](cifilter/3547120-colorthreshold.md)
  Compares the red, green, and blue components of the input image to a threshold and sets them to 1 or 0.
- [class func colorThresholdOtsu() -> any CIFilter & CIColorThresholdOtsu](cifilter/4401855-colorthresholdotsu.md)
  Compares the red, green, and blue components of the input image against a threshold calculated using Otsu’s algorithm.
- [class func depthToDisparity() -> any CIFilter & CIDepthToDisparity](cifilter/3228309-depthtodisparity.md)
  Converts from an image containing depth data to an image containing disparity data.
- [class func disparityToDepth() -> any CIFilter & CIDisparityToDepth](cifilter/3228313-disparitytodepth.md)
  Creates depth data from an image containing disparity data.
- [class func exposureAdjust() -> any CIFilter & CIExposureAdjust](cifilter/3228324-exposureadjust.md)
  Adjusts an image’s exposure.
- [class func gammaAdjust() -> any CIFilter & CIGammaAdjust](cifilter/3228330-gammaadjust.md)
  Alters an image’s transition between black and white.
- [class func hueAdjust() -> any CIFilter & CIHueAdjust](cifilter/3228340-hueadjust.md)
  Modifies an image’s hue.
- [class func linearToSRGBToneCurve() -> any CIFilter & CILinearToSRGBToneCurve](cifilter/3228352-lineartosrgbtonecurve.md)
  Alters an image’s color intensity.
- [class func sRGBToneCurveToLinear() -> any CIFilter & CISRGBToneCurveToLinear](cifilter/3228398-srgbtonecurvetolinear.md)
  Converts the colors in an image from sRGB to linear.
- [class func toneCurve() -> any CIFilter & CIToneCurve](cifilter/3228424-tonecurve.md)
  Alters an image’s tone curve according to a series of data points.
- [class func vibrance() -> any CIFilter & CIVibrance](cifilter/3228429-vibrance.md)
  Adjusts an image’s vibrancy.
- [class func whitePointAdjust() -> any CIFilter & CIWhitePointAdjust](cifilter/3228432-whitepointadjust.md)
  Adjusts the image’s white-point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228421-temperatureandtint)*