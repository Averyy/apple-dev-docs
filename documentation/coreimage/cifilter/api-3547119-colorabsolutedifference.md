# colorAbsoluteDifference()

**Framework**: Core Image  
**Kind**: clm

Calculates the absolute difference between each color component in the input images.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func colorAbsoluteDifference() -> any CIFilter & CIColorAbsoluteDifference
```

#### Return_value

An image containing the absolute color difference between the two input images.

#### Discussion

This method applies the color absolute difference filter to an image. This filter calculates the absolute color difference of the red, green, and blue values between the two input images. The alpha channel is the product of the alpha channels from the two input images.

The absolute difference filter uses the following properties:

The following code creates a filter that results in the color difference between two images:

```swift
func colorAbsolute(inputImage: CIImage, inputImage2: CIImage) -> CIImage {
    let filter = CIFilter.colorAbsoluteDifference()
    filter.inputImage = inputImage
    filter.inputImage2 = inputImage2
    return filter.outputImage!
}
```

![Three images arranged with two images on the left and an image on the right. The top left image is a solid green color, and the bottom left image is a single palm tree with a clear sky. The right image shows the result of applying the color absolute difference filter to the two images on the left. The palm tree is now highlighted against the background.](https://docs-assets.developer.apple.com/published/60f3a89022/rendered2x-1707833975.png)

## See Also

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
- [class func temperatureAndTint() -> any CIFilter & CITemperatureAndTint](cifilter/3228421-temperatureandtint.md)
  Alters an image’s temperature and tint.
- [class func toneCurve() -> any CIFilter & CIToneCurve](cifilter/3228424-tonecurve.md)
  Alters an image’s tone curve according to a series of data points.
- [class func vibrance() -> any CIFilter & CIVibrance](cifilter/3228429-vibrance.md)
  Adjusts an image’s vibrancy.
- [class func whitePointAdjust() -> any CIFilter & CIWhitePointAdjust](cifilter/3228432-whitepointadjust.md)
  Adjusts the image’s white-point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3547119-colorabsolutedifference)*