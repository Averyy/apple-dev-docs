# Filter Parameter Keys

**Framework**: Core Image

Keys for input parameters to filters.

#### Overview

These keys represent some of the most commonly used input parameters. A filter can use other kinds of input parameters.

## Topics

### Constants
- [let kCIOutputImageKey: String](kcioutputimagekey.md)
  A key for the [`CIImage`](ciimage.md) object produced by a filter.
- [let kCIInputAmountKey: String](kciinputamountkey.md)
- [let kCIInputBackgroundImageKey: String](kciinputbackgroundimagekey.md)
  A key for the [`CIImage`](ciimage.md) object to use as a background image.
- [let kCIInputImageKey: String](kciinputimagekey.md)
  A key for the [`CIImage`](ciimage.md) object to use as an input image. For filters that also use a background image, this key refers to the foreground image.
- [let kCIInputTimeKey: String](kciinputtimekey.md)
  Specify a time.
- [let kCIInputDepthImageKey: String](kciinputdepthimagekey.md)
  A key for an image with depth values.
- [let kCIInputDisparityImageKey: String](kciinputdisparityimagekey.md)
  A key for an image with disparity values.
- [let kCIInputTransformKey: String](kciinputtransformkey.md)
  Transformation to apply.
- [let kCIInputScaleKey: String](kciinputscalekey.md)
  The amount of scale to apply.
- [let kCIInputAspectRatioKey: String](kciinputaspectratiokey.md)
  Aspect Ratio.
- [let kCIInputCenterKey: String](kciinputcenterkey.md)
  A key for a [`CIVector`](civector.md) object that specifies the center of the area, as   and  - coordinates, to be filtered.
- [let kCIInputRadiusKey: String](kciinputradiuskey.md)
  The distance from the center of an effect.
- [let kCIInputAngleKey: String](kciinputanglekey.md)
  The angle.
- [let kCIInputRefractionKey: String](kciinputrefractionkey.md)
  The index of refraction to use.
- [let kCIInputWidthKey: String](kciinputwidthkey.md)
  A key for a scalar value that specifies the width of the effect.
- [let kCIInputSharpnessKey: String](kciinputsharpnesskey.md)
  Amount of sharpening to apply.
- [let kCIInputIntensityKey: String](kciinputintensitykey.md)
  An intensity value.
- [let kCIInputEVKey: String](kciinputevkey.md)
  How many F-stops brighter or darker the image should be.
- [let kCIInputSaturationKey: String](kciinputsaturationkey.md)
  The amount to adjust the saturation.
- [let kCIInputColorKey: String](kciinputcolorkey.md)
  A key for a [`CIColor`](cicolor.md) object that specifies a color value.
- [let kCIInputBrightnessKey: String](kciinputbrightnesskey.md)
  Brightness level.
- [let kCIInputContrastKey: String](kciinputcontrastkey.md)
  A contrast level.
- [let kCIInputWeightsKey: String](kciinputweightskey.md)
  A key for a [`CIVector`](civector.md) object that describes a weight matrix for use with a convolution filter.
- [let kCIInputGradientImageKey: String](kciinputgradientimagekey.md)
  A key for a [`CIImage`](ciimage.md) object that specifies an environment map with alpha. Typically, this image contains highlight and shadow.
- [let kCIInputMaskImageKey: String](kciinputmaskimagekey.md)
  A key for a [`CIImage`](ciimage.md) object to use as a mask.
- [let kCIInputMatteImageKey: String](kciinputmatteimagekey.md)
- [let kCIInputShadingImageKey: String](kciinputshadingimagekey.md)
  A key for a [`CIImage`](ciimage.md) object  that specifies an environment map with alpha values. Typically this image contains highlight and shadow.
- [let kCIInputTargetImageKey: String](kciinputtargetimagekey.md)
  A key for a [`CIImage`](ciimage.md) object that is the target image for a transition.
- [let kCIInputExtentKey: String](kciinputextentkey.md)
  A key for a [`CIVector`](civector.md) object that specifies a rectangle that defines the extent of the effect.
- [let kCIInputVersionKey: String](kciinputversionkey.md)
  Version Key
- [static let standard: CIDynamicRangeOption](cidynamicrangeoption/standard.md)
  Standard dynamic range. Images with `contentHeadroom` metadata will be tone mapped to a maximum pixel value of 1.0.
- [static let constrainedHigh: CIDynamicRangeOption](cidynamicrangeoption/constrainedhigh.md)
  Use extended dynamic range, but brightness is modulated to optimize for co-existence with other composited content. For best results, images should contain `contentAverageLightLevel` metadata.
- [static let high: CIDynamicRangeOption](cidynamicrangeoption/high.md)
  Use High dynamic range. Provides the best HDR quality. This needs to be reserved for situations where the user is focused on the media, such as larger views in an image editing/viewing app, or annotating/drawing with HDR colors
- [static let baselineExposure: CIRAWFilterOption](cirawfilteroption/baselineexposure.md)
  The amount of baseline exposure applied.
- [static let disableGamutMap: CIRAWFilterOption](cirawfilteroption/disablegamutmap.md)
  Whether or not to disable gamut mapping.
- [static let moireAmount: CIRAWFilterOption](cirawfilteroption/moireamount.md)
  The amount of moiré reduction to apply.

## See Also

- [Filter Attribute Keys](filter-attribute-keys.md)
  Attributes for a filter and its parameters.
- [Data Type Attributes](data-type-attributes.md)
  Numeric data types.
- [Vector Quantity Attributes](vector-quantity-attributes.md)
  Vector data types.
- [Color Attribute Keys](color-attribute-keys.md)
  Color types.
- [Image Attribute Keys](image-attribute-keys.md)
  Image Types
- [Filter Category Keys](filter-category-keys.md)
  Categories of filters.
- [Options for Applying a Filter](options-for-applying-a-filter.md)
  Options that control the application of a custom Core Image filter.
- [User Interface Control Options](user-interface-control-options.md)
  Sets of controls for various user scenarios.
- [User Interface Options](user-interface-options.md)
  Keys or values for the size of the input parameter controls for a filter view.
- [RAW Image Options](raw-image-options.md)
  Options for creating a [`CIFilter`](cifilter-swift.class.md) object from RAW image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/filter-parameter-keys)*