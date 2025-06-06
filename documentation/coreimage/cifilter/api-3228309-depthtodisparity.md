# depthToDisparity()

**Framework**: Core Image  
**Kind**: clm

Converts from an image containing depth data to an image containing disparity data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func depthToDisparity() -> any CIFilter & CIDepthToDisparity
```

#### Return_value

An image containing the disparity data.

#### Discussion

This method applies the depth-to-disparity filter. The filter takes depth data as an input and produces disparity data in the output image. You can use the output of this filter to create a stereo image. 

The depth-to-disparity filter uses the following property:

The following code creates a filter that generates a depth map image:

```swift
func depthToDisparity(inputImage: CIImage) -> CIImage {
    let depthToDisparityFilter = CIFilter.depthToDisparity()
    depthToDisparityFilter.inputImage = inputImage
    return depthToDisparityFilter.outputImage!
}
```

![Two photographs of a small dog sitting on grass. The photo on the left shows the dog in the foreground with good light and a soft blur of the background. In the photo on the right, a depth-to-disparity filter is applied, resulting in a depth map created from the photo on the left. The dog in the photo and the ground are replaced with gray, and the background is replaced with white.](https://docs-assets.developer.apple.com/published/d55e0d1b61/rendered2x-1589928926.png)

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
- [class func temperatureAndTint() -> any CIFilter & CITemperatureAndTint](cifilter/3228421-temperatureandtint.md)
  Alters an image’s temperature and tint.
- [class func toneCurve() -> any CIFilter & CIToneCurve](cifilter/3228424-tonecurve.md)
  Alters an image’s tone curve according to a series of data points.
- [class func vibrance() -> any CIFilter & CIVibrance](cifilter/3228429-vibrance.md)
  Adjusts an image’s vibrancy.
- [class func whitePointAdjust() -> any CIFilter & CIWhitePointAdjust](cifilter/3228432-whitepointadjust.md)
  Adjusts the image’s white-point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228309-depthtodisparity)*