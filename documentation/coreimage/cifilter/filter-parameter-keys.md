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
  A key for z scalar value ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)) that specifies a time.
- [let kCIInputDepthImageKey: String](kciinputdepthimagekey.md)
  A key for an image with depth values.
- [let kCIInputDisparityImageKey: String](kciinputdisparityimagekey.md)
  A key for an image with disparity values.
- [let kCIInputTransformKey: String](kciinputtransformkey.md)
  A key for an [`NSAffineTransform`](https://developer.apple.com/documentation/foundation/nsaffinetransform) object that specifies a transformation to apply.
- [let kCIInputScaleKey: String](kciinputscalekey.md)
  A key for a scalar value ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)) that specifies  the amount of the effect.
- [let kCIInputAspectRatioKey: String](kciinputaspectratiokey.md)
  A key for a scalar value ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)) that specifies a ratio.
- [let kCIInputCenterKey: String](kciinputcenterkey.md)
  A key for a [`CIVector`](civector.md) object that specifies the center of the area, as   and  - coordinates, to be filtered.
- [let kCIInputRadiusKey: String](kciinputradiuskey.md)
  A key for a scalar value ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)) that specifies the distance from the center of an effect.
- [let kCIInputAngleKey: String](kciinputanglekey.md)
  A key for a scalar value ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)) that specifies an angle.
- [let kCIInputRefractionKey: String](kciinputrefractionkey.md)
  A key for a scalar value ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)) that specifies the index of refraction of the material (such as glass) used in the effect.
- [let kCIInputWidthKey: String](kciinputwidthkey.md)
  A key for a scalar value ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)) that specifies the width of the effect.
- [let kCIInputSharpnessKey: String](kciinputsharpnesskey.md)
  A key for a scalar value ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)) that specifies the amount of sharpening to apply.
- [let kCIInputIntensityKey: String](kciinputintensitykey.md)
  A key for a scalar value ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)) that specifies an intensity value.
- [let kCIInputEVKey: String](kciinputevkey.md)
  A key for a scalar value ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)) that specifies how many F-stops brighter or darker the image should be.
- [let kCIInputSaturationKey: String](kciinputsaturationkey.md)
  A key for a scalar value ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)) that specifies the amount to adjust the saturation.
- [let kCIInputColorKey: String](kciinputcolorkey.md)
  A key for a [`CIColor`](cicolor.md) object that specifies a color value.
- [let kCIInputBrightnessKey: String](kciinputbrightnesskey.md)
  A key for a scalar value ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)) that specifies a brightness level. 
- [let kCIInputContrastKey: String](kciinputcontrastkey.md)
  A key for a scalar value ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)) that specifies a contrast level.
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
  A key for an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object that specifies a version number.
- [static let baselineExposure: CIRAWFilterOption](cirawfilteroption/2202263-baselineexposure.md)
  A key for an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object containing a float that expresses the amount of baseline exposure applied to an image.
- [static let disableGamutMap: CIRAWFilterOption](cirawfilteroption/2202264-disablegamutmap.md)
  A key for an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object containing a Boolean value that determines whether or not to disable gamut mapping.
- [static let moireAmount: CIRAWFilterOption](cirawfilteroption/2880265-moireamount.md)
  A key for an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object containing a double that expresses the amount of moiré reduction applied to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/filter_parameter_keys)*