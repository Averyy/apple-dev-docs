# Blur Filters

**Framework**: Core Image

Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.

## Topics

### Filters
- [class func bokehBlur() -> any CIFilter & CIBokehBlur](cifilter-swift.class/bokehblur.md)
  Applies a bokeh effect to an image.
- [class func boxBlur() -> any CIFilter & CIBoxBlur](cifilter-swift.class/boxblur.md)
  Applies a square-shaped blur to an area of an image.
- [class func discBlur() -> any CIFilter & CIDiscBlur](cifilter-swift.class/discblur.md)
  Applies a circle-shaped blur to an area of an image.
- [class func gaussianBlur() -> any CIFilter & CIGaussianBlur](cifilter-swift.class/gaussianblur.md)
  Blurs an image with a Gaussian distribution pattern.
- [class func maskedVariableBlur() -> any CIFilter & CIMaskedVariableBlur](cifilter-swift.class/maskedvariableblur.md)
  Blurs a specified portion of an image.
- [class func median() -> any CIFilter & CIMedian](cifilter-swift.class/median.md)
  Calculates the median of an image to refine detail.
- [class func morphologyGradient() -> any CIFilter & CIMorphologyGradient](cifilter-swift.class/morphologygradient.md)
  Detects and highlights edges of objects.
- [class func morphologyMaximum() -> any CIFilter & CIMorphologyMaximum](cifilter-swift.class/morphologymaximum.md)
  Blurs a circular area by enlarging contrasting pixels.
- [class func morphologyMinimum() -> any CIFilter & CIMorphologyMinimum](cifilter-swift.class/morphologyminimum.md)
  Blurs a circular area by reducing contrasting pixels.
- [class func morphologyRectangleMaximum() -> any CIFilter & CIMorphologyRectangleMaximum](cifilter-swift.class/morphologyrectanglemaximum.md)
  Blurs a rectangular area by enlarging contrasting pixels.
- [class func morphologyRectangleMinimum() -> any CIFilter & CIMorphologyRectangleMinimum](cifilter-swift.class/morphologyrectangleminimum.md)
  Blurs a rectangular area by reducing contrasting pixels.
- [class func motionBlur() -> any CIFilter & CIMotionBlur](cifilter-swift.class/motionblur.md)
  Creates motion blur on an image.
- [class func noiseReduction() -> any CIFilter & CINoiseReduction](cifilter-swift.class/noisereduction.md)
  Reduces noise by sharpening the edges of objects.
- [class func zoomBlur() -> any CIFilter & CIZoomBlur](cifilter-swift.class/zoomblur.md)
  Creates a zoom blur centered around a single point on the image.
### Protocols
- [protocol CIBokehBlur](cibokehblur.md)
  The properties you use to configure a bokeh blur filter.
- [protocol CIBoxBlur](ciboxblur.md)
  The properties you use to configure a box blur filter.
- [protocol CIDiscBlur](cidiscblur.md)
  The properties you use to configure a disc blur filter.
- [protocol CIGaussianBlur](cigaussianblur.md)
  The properties you use to configure a Gaussian blur filter.
- [protocol CIMaskedVariableBlur](cimaskedvariableblur.md)
  The properties you use to configure a masked variable blur filter.
- [protocol CIMedian](cimedian.md)
  The properties you use to configure a median filter.
- [protocol CIMorphologyGradient](cimorphologygradient.md)
  The properties you use to configure a morphology gradient filter.
- [protocol CIMorphologyMaximum](cimorphologymaximum.md)
  The properties you use to configure a morphology maximum filter.
- [protocol CIMorphologyMinimum](cimorphologyminimum.md)
  The properties you use to configure a morphology minimum filter.
- [protocol CIMorphologyRectangleMaximum](cimorphologyrectanglemaximum.md)
  The properties you use to configure a morphology rectangle maximum filter.
- [protocol CIMorphologyRectangleMinimum](cimorphologyrectangleminimum.md)
  The properties you use to configure a morphology rectangle minimum filter.
- [protocol CIMotionBlur](cimotionblur.md)
  The properties you use to configure a motion blur filter.
- [protocol CINoiseReduction](cinoisereduction.md)
  The properties you use to configure a noise reduction filter.
- [protocol CIZoomBlur](cizoomblur.md)
  The properties you use to configure a zoom blur filter.

## See Also

- [Color Adjustment Filters](color-adjustment-filters.md)
  Apply color transformations, including exposure, hue, and tint adjustments.
- [Color Effect Filters](color-effect-filters.md)
  Apply color effects, including photo effects, dithering, and color maps.
- [Composite Operations](composite-operations.md)
  Composite images by using a range of blend modes and compositing operators.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/blur-filters)*