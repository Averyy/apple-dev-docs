# Convolution Filters

**Framework**: Core Image

Produce effects such as blurring, sharpening, edge detection, translation, and embossing.

#### Overview

A convolution filter generates each output pixel by summing all elements in the element-wise product of two matrices - the weight matrix and a matrix containing the neighbors of each input pixel. A bias is added to this and the resulting value is clamped to between 0.0 and 1.0. This operation is performed independently for each color component (including the alpha component). You can create many types of image processing effects using different weight matrices, such as blurring, sharpening, edge detection, translation, and embossing.

## Topics

### Filters
- [class func convolution3X3() -> any CIFilter & CIConvolution](cifilter/3228299-convolution3x3.md)
  Applies a convolution 3 x 3 filter to the `RGBA` components of an image.
- [class func convolution5X5() -> any CIFilter & CIConvolution](cifilter/3228300-convolution5x5.md)
  Applies a convolution 5 x 5 filter to the `RGBA` components image.
- [class func convolution7X7() -> any CIFilter & CIConvolution](cifilter/3228301-convolution7x7.md)
  Applies a convolution 7 x 7 filter to the `RGBA` color components of an image.
- [class func convolution9Horizontal() -> any CIFilter & CIConvolution](cifilter/3228302-convolution9horizontal.md)
  Applies a convolution-9 horizontal filter to the `RGBA` components of an image.
- [class func convolution9Vertical() -> any CIFilter & CIConvolution](cifilter/3228303-convolution9vertical.md)
  Applies a convolution-9 vertical filter to the `RGBA` components of an image.
- [class func convolutionRGB3X3() -> any CIFilter & CIConvolution](cifilter/4401858-convolutionrgb3x3.md)
  Applies a convolution 3 x 3 filter to the `RGB` components of an image.
- [class func convolutionRGB5X5() -> any CIFilter & CIConvolution](cifilter/4401859-convolutionrgb5x5.md)
  Applies a convolution 5 x 5 filter to the `RGB` components of an image.
- [class func convolutionRGB7X7() -> any CIFilter & CIConvolution](cifilter/4401860-convolutionrgb7x7.md)
  Applies a convolution 7 x 7 filter to the RGB components of an image.
- [class func convolutionRGB9Horizontal() -> any CIFilter & CIConvolution](cifilter/4401861-convolutionrgb9horizontal.md)
  Applies a convolution 9 x 1 filter to the RGB components of an image.
- [class func convolutionRGB9Vertical() -> any CIFilter & CIConvolution](cifilter/4401862-convolutionrgb9vertical.md)
  Applies a convolution 1 x 9 filter to the RGB components of an image.

## See Also

- [Blur Filters](blur_filters.md)
  Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Adjustment Filters](color_adjustment_filters.md)
  Apply color transformations, including exposure, hue, and tint adjustments.
- [Color Effect Filters](color_effect_filters.md)
  Apply color effects, including photo effects, dithering, and color maps.
- [Composite Operations](composite_operations.md)
  Composite images by using a range of blend modes and compositing operators. 
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/convolution_filters)*