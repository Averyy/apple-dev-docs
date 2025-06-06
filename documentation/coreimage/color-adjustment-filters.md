# Color Adjustment Filters

**Framework**: Core Image

Apply color transformations, including exposure, hue, and tint adjustments.

## Topics

### Filters
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
- [class func temperatureAndTint() -> any CIFilter & CITemperatureAndTint](cifilter/3228421-temperatureandtint.md)
  Alters an image’s temperature and tint.
- [class func toneCurve() -> any CIFilter & CIToneCurve](cifilter/3228424-tonecurve.md)
  Alters an image’s tone curve according to a series of data points.
- [class func vibrance() -> any CIFilter & CIVibrance](cifilter/3228429-vibrance.md)
  Adjusts an image’s vibrancy.
- [class func whitePointAdjust() -> any CIFilter & CIWhitePointAdjust](cifilter/3228432-whitepointadjust.md)
  Adjusts the image’s white-point.

## See Also

- [Blur Filters](blur_filters.md)
  Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Effect Filters](color_effect_filters.md)
  Apply color effects, including photo effects, dithering, and color maps.
- [Composite Operations](composite_operations.md)
  Composite images by using a range of blend modes and compositing operators. 
- [Convolution Filters](convolution_filters.md)
  Produce effects such as blurring, sharpening, edge detection, translation, and embossing.
- [Distortion Filters](distortion_filters.md)
  Apply distortion to images.
- [Generator Filters](generator_filters.md)
  Generate barcode, geometric, and special-effect images.
- [Geometry Adjustment Filters](geometry_adjustment_filters.md)
  Translate, scale, and rotate images in 2D and 3D.
- [Gradient Filters](gradient_filters.md)
  Generate linear and radial gradients.
- [Halftone Effect Filters](halftone_effect_filters.md)
  Simulate monochrome and CMYK halftone screens.
- [Reduction Filters](reduction_filters.md)
  Create statistical information about an image.
- [Sharpening Filters](sharpening_filters.md)
  Apply sharpening to images.
- [Stylizing Filters](stylizing_filters.md)
  Create stylized versions of images by applying effects including pixelation and line overlays.
- [Tile Effect Filters](tile_effect_filters.md)
  Produce tiled images from source images.
- [Transition Filters](transition_filters.md)
  Transition between two images by using effects including page curl and swipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/color_adjustment_filters)*