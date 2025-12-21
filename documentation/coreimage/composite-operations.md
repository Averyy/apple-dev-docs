# Composite Operations

**Framework**: Core Image

Composite images by using a range of blend modes and compositing operators.

## Topics

### Filters
- [class func additionCompositing() -> any CIFilter & CICompositeOperation](cifilter-swift.class/additioncompositing.md)
  Blends colors from two images by addition.
- [class func colorBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/colorblendmode.md)
  Blends color from two images using the luminance values from the background image and the hue and saturation values from the input image.
- [class func colorBurnBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/colorburnblendmode.md)
  Blends color from two images while darkening the image.
- [class func colorDodgeBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/colordodgeblendmode.md)
  Blends color from two images using dodging.
- [class func darkenBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/darkenblendmode.md)
  Blends colors from two images while darkening lighter pixels.
- [class func differenceBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/differenceblendmode.md)
  Subtracts color values to blend colors.
- [class func divideBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/divideblendmode.md)
  Divides color values to blend colors.
- [class func exclusionBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/exclusionblendmode.md)
  Subtracts color values to blend colors with less contrast.
- [class func hardLightBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/hardlightblendmode.md)
  Blends colors of two images by screening and multiplying.
- [class func hueBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/hueblendmode.md)
  Blends colors of two images by computing the sum of image color values.
- [class func lightenBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/lightenblendmode.md)
  Blends colors from two images by brightening colors.
- [class func linearBurnBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/linearburnblendmode.md)
  Blends color from two images while increasing contrast.
- [class func linearDodgeBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/lineardodgeblendmode.md)
  Blends colors of two images with dodging.
- [class func linearLightBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/linearlightblendmode.md)
  A combination of linear burn and linear dodge blend modes.
- [class func luminosityBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/luminosityblendmode.md)
  Blends color from two images by calculating the color, hue, and saturation.
- [class func minimumCompositing() -> any CIFilter & CICompositeOperation](cifilter-swift.class/minimumcompositing.md)
  Blends colors from two images by computing minimum values.
- [class func maximumCompositing() -> any CIFilter & CICompositeOperation](cifilter-swift.class/maximumcompositing.md)
  Applies a maximum compositing filter to an image.
- [class func multiplyBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/multiplyblendmode.md)
  Blends colors from two images by multiplying color components.
- [class func multiplyCompositing() -> any CIFilter & CICompositeOperation](cifilter-swift.class/multiplycompositing.md)
  Blurs the colors of two images by multiplying color components.
- [class func overlayBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/overlayblendmode.md)
  Blends colors by overlaying images.
- [class func pinLightBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/pinlightblendmode.md)
  Blends colors of two images by replacing brighter colors.
- [class func saturationBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/saturationblendmode.md)
  Blends the colors and saturation values of two images.
- [class func screenBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/screenblendmode.md)
  Blends colors of two images by multiplying colors.
- [class func softLightBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/softlightblendmode.md)
  Blurs the colors of two images by calculating luminance.
- [class func sourceAtopCompositing() -> any CIFilter & CICompositeOperation](cifilter-swift.class/sourceatopcompositing.md)
  Overlaps two images to create one cropped image.
- [class func sourceInCompositing() -> any CIFilter & CICompositeOperation](cifilter-swift.class/sourceincompositing.md)
  Subtracts non-overlapping areas of two images, resulting in one image.
- [class func sourceOutCompositing() -> any CIFilter & CICompositeOperation](cifilter-swift.class/sourceoutcompositing.md)
  Subtracts overlapping area of two images to create the output image.
- [class func sourceOverCompositing() -> any CIFilter & CICompositeOperation](cifilter-swift.class/sourceovercompositing.md)
  Places one image over a second image.
- [class func subtractBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/subtractblendmode.md)
  Blends colors by subtracting color values from two images.
- [class func vividLightBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/vividlightblendmode.md)
  A combination of color-burn and color-dodge blend modes.
### Protocols
- [protocol CICompositeOperation](cicompositeoperation.md)
  The properties you use to configure a composite operation filter.

## See Also

- [Blur Filters](blur-filters.md)
  Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Adjustment Filters](color-adjustment-filters.md)
  Apply color transformations, including exposure, hue, and tint adjustments.
- [Color Effect Filters](color-effect-filters.md)
  Apply color effects, including photo effects, dithering, and color maps.
- [Convolution Filters](convolution-filters.md)
  Produce effects such as blurring, sharpening, edge detection, translation, and embossing.
- [Distortion Filters](distortion-filters.md)
  Apply distortion to images.
- [Generator Filters](generator-filters.md)
  Generate barcode, geometric, and special-effect images.
- [Geometry Adjustment Filters](geometry-adjustment-filters.md)
  Translate, scale, and rotate images in 2D and 3D.
- [Gradient Filters](gradient-filters.md)
  Generate linear and radial gradients.
- [Halftone Effect Filters](halftone-effect-filters.md)
  Simulate monochrome and CMYK halftone screens.
- [Reduction Filters](reduction-filters.md)
  Create statistical information about an image.
- [Sharpening Filters](sharpening-filters.md)
  Apply sharpening to images.
- [Stylizing Filters](stylizing-filters.md)
  Create stylized versions of images by applying effects including pixelation and line overlays.
- [Tile Effect Filters](tile-effect-filters.md)
  Produce tiled images from source images.
- [Transition Filters](transition-filters.md)
  Transition between two images by using effects including page curl and swipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/composite-operations)*