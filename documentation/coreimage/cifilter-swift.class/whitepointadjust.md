# whitePointAdjust()

**Framework**: Core Image  
**Kind**: method

Adjusts the image’s white-point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func whitePointAdjust() -> any CIFilter & CIWhitePointAdjust
```

#### Return Value

The modified image.

#### Discussion

This method applies the white-point adjust filter to an image. The effect adjusts the white-point of the input image by mapping all shades of gray to shades of the color property.

The white-point adjust filter uses the following properties:

The following code creates a filter that adds a red hue to the input image:

```swift
func whitePoint(inputImage: CIImage) -> CIImage {
    let whitePointFilter = CIFilter.whitePointAdjust()
    whitePointFilter.inputImage = inputImage
    whitePointFilter.color = CIColor(red: 1, green: 0.6, blue: 0.6, alpha: 1)
    return whitePointFilter.outputImage!
}
```

![Two versions of a photograph side by side. The photo on the left shows a small bunch of flowers photographed close up, in focus, with good light and no effects. In the photo on the right, a white point adjust filter is applied, resulting in a pink hue added to the entire image.](https://docs-assets.developer.apple.com/published/ae08a9d52f59be43e7c900861b0c25d8/media-3545004%402x.png)

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
- [class func sRGBToneCurveToLinear() -> any CIFilter & CISRGBToneCurveToLinear](cifilter-swift.class/srgbtonecurvetolinear.md)
  Converts the colors in an image from sRGB to linear.
- [class func temperatureAndTint() -> any CIFilter & CITemperatureAndTint](cifilter-swift.class/temperatureandtint.md)
  Alters an image’s temperature and tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/whitepointadjust())*