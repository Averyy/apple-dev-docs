# CIRAWFilter

**Framework**: Core Image  
**Kind**: cl

A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class CIRAWFilter : CIFilter
```

#### Overview

Use this class to generate a [`CIImage`](ciimage.md) object based on the configuration parameters you provide.

You can use this object in conjunction with other Core Image classes—such as [`CIFilter`](cifilter.md) and [`CIContext`](cicontext.md)—to take advantage of the built-in Core Image filters when processing images or writing custom filters.

You can also query this object to find out about the supported camera models, decoders, and filters.

## Topics

### Creating a filter
- [init?(cvPixelBuffer: CVPixelBuffer, properties: [AnyHashable : Any])](cirawfilter/3801628-init.md)
  Creates a RAW filter from the pixel buffer and its properties that you specify.
- [init?(imageData: Data, identifierHint: String?)](cirawfilter/3801629-init.md)
  Creates a RAW filter from the image data and type hint that you specify.
- [init?(imageURL: URL)](cirawfilter/3801630-init.md)
  Creates a RAW filter from the image at the URL location that you specify.
### Inspecting supported camera models, decoders, and filters
- [class var supportedCameraModels: [String]](cirawfilter/3801659-supportedcameramodels.md)
  An array containing the names of all supported camera models.
- [var supportedDecoderVersions: [CIRAWDecoderVersion]](cirawfilter/3801660-supporteddecoderversions.md)
  An array of all supported decoder versions for the given image type.
- [struct CIRAWDecoderVersion](cirawdecoderversion.md)
- [var isColorNoiseReductionSupported: Bool](cirawfilter/3801619-iscolornoisereductionsupported.md)
  A Boolean that indicates if the current image supports color noise reduction adjustments.
- [var isContrastSupported: Bool](cirawfilter/3801621-iscontrastsupported.md)
  A Boolean that indicates if the current image supports contrast adjustments.
- [var isDetailSupported: Bool](cirawfilter/3801624-isdetailsupported.md)
  A Boolean that indicates if the current image supports detail enhancement adjustments.
- [var isLensCorrectionSupported: Bool](cirawfilter/3801633-islenscorrectionsupported.md)
  A Boolean that indicates if you can enable lens correction for the current image.
- [var isLocalToneMapSupported: Bool](cirawfilter/3801636-islocaltonemapsupported.md)
  A Boolean that indicates if the current image supports local tone curve adjustments.
- [var isLuminanceNoiseReductionSupported: Bool](cirawfilter/3801638-isluminancenoisereductionsupport.md)
  A Boolean that indicates if the current image supports luminance noise reduction adjustments.
- [var isMoireReductionSupported: Bool](cirawfilter/3801640-ismoirereductionsupported.md)
  A Boolean that indicates if the current image supports moire artifact reduction adjustments.
- [var isSharpnessSupported: Bool](cirawfilter/3801658-issharpnesssupported.md)
  A Boolean that indicates if the current image supports sharpness adjustments.
- [var nativeSize: CGSize](cirawfilter/3801641-nativesize.md)
  The full native size of the unscaled image.
### Configuring a filter
- [var baselineExposure: Float](cirawfilter/3801615-baselineexposure.md)
  A value that indicates the baseline exposure to apply to the image.
- [var boostAmount: Float](cirawfilter/3801616-boostamount.md)
  A value that indicates the amount of global tone curve to apply to the image.
- [var boostShadowAmount: Float](cirawfilter/3801617-boostshadowamount.md)
  A value that indicates the amount to boost the shadow areas of the image.
- [var colorNoiseReductionAmount: Float](cirawfilter/3801618-colornoisereductionamount.md)
  A value that indicates the amount of chroma noise reduction to apply to the image.
- [var contrastAmount: Float](cirawfilter/3801620-contrastamount.md)
  A value that indicates the amount of local contrast to apply to the edges of the image.
- [var decoderVersion: CIRAWDecoderVersion](cirawfilter/3801622-decoderversion.md)
  A value that indicates the decoder version to use.
- [var detailAmount: Float](cirawfilter/3801623-detailamount.md)
  A value that indicates the amount of detail enhancement to apply to the edges of the image.
- [var exposure: Float](cirawfilter/3801626-exposure.md)
  A value that indicates the amount of exposure to apply to the image.
- [var extendedDynamicRangeAmount: Float](cirawfilter/3820998-extendeddynamicrangeamount.md)
  A value that indicates the amount of extended dynamic range (EDR) to apply to the image.
- [var isDraftModeEnabled: Bool](cirawfilter/3801625-isdraftmodeenabled.md)
  A Boolean that indicates whether to enable draft mode.
- [var isGamutMappingEnabled: Bool](cirawfilter/3801631-isgamutmappingenabled.md)
  A Boolean that indicates whether to enable gamut mapping.
- [var isLensCorrectionEnabled: Bool](cirawfilter/3801632-islenscorrectionenabled.md)
  A Boolean that indicates whether to enable lens correction.
- [var linearSpaceFilter: CIFilter?](cirawfilter/3801634-linearspacefilter.md)
  An optional filter you can apply to the RAW image while it’s in linear space.
- [var localToneMapAmount: Float](cirawfilter/3801635-localtonemapamount.md)
  A value that indicates the amount of local tone curve to apply to the image.
- [var luminanceNoiseReductionAmount: Float](cirawfilter/3801637-luminancenoisereductionamount.md)
  A value that indicates the amount of luminance noise reduction to apply to the image.
- [var moireReductionAmount: Float](cirawfilter/3801639-moirereductionamount.md)
  A value that indicates the amount of moire artifact reduction to apply to high frequency areas of the image.
- [var neutralChromaticity: CGPoint](cirawfilter/3801642-neutralchromaticity.md)
  A value that indicates the amount of white balance based on chromaticity values to apply to the image.
- [var neutralLocation: CGPoint](cirawfilter/3801643-neutrallocation.md)
  A value that indicates the amount of white balance based on pixel coordinates to apply to the image.
- [var neutralTemperature: Float](cirawfilter/3801644-neutraltemperature.md)
  A value that indicates the amount of white balance based on temperature values to apply to the image.
- [var neutralTint: Float](cirawfilter/3801645-neutraltint.md)
  A value that indicates the amount of white balance based on tint values to apply to the image.
- [var orientation: CGImagePropertyOrientation](cirawfilter/3801646-orientation.md)
  A value that indicates the orientation of the image.
- [var portraitEffectsMatte: CIImage?](cirawfilter/3801647-portraiteffectsmatte.md)
  An optional auxiliary image that represents the portrait effects matte of the image.
- [var previewImage: CIImage?](cirawfilter/3801648-previewimage.md)
  An optional auxiliary image that represents a preview of the original image.
- [var properties: [AnyHashable : Any]](cirawfilter/3801649-properties.md)
  A dictionary that contains properties of the image source.
- [var scaleFactor: Float](cirawfilter/3801650-scalefactor.md)
  A value that indicates the desired scale factor to draw the output image.
- [var semanticSegmentationGlassesMatte: CIImage?](cirawfilter/3801651-semanticsegmentationglassesmatte.md)
  An optional auxiliary image that represents the semantic segmentation glasses matte of the image.
- [var semanticSegmentationHairMatte: CIImage?](cirawfilter/3801652-semanticsegmentationhairmatte.md)
  An optional auxiliary image that represents the semantic segmentation hair matte of the image.
- [var semanticSegmentationSkinMatte: CIImage?](cirawfilter/3801653-semanticsegmentationskinmatte.md)
  An optional auxiliary image that represents the semantic segmentation skin matte of the image.
- [var semanticSegmentationSkyMatte: CIImage?](cirawfilter/3801654-semanticsegmentationskymatte.md)
  An optional auxiliary image that represents the semantic segmentation sky matte of the image.
- [var semanticSegmentationTeethMatte: CIImage?](cirawfilter/3801655-semanticsegmentationteethmatte.md)
  An optional auxiliary image that represents the semantic segmentation teeth matte of the image.
- [var shadowBias: Float](cirawfilter/3801656-shadowbias.md)
  A value that indicates the amount to subtract from the shadows in the image.
- [var sharpnessAmount: Float](cirawfilter/3801657-sharpnessamount.md)
  A value that indicates the amount of sharpness to apply to the edges of the image.

## Relationships

### Inherits From
- [CIFilter](cifilter.md)

## See Also

- [class CIFilter](cifilter.md)
  An image processor that produces an image by manipulating one or more input images or by generating new image data.
- [class CIColor](cicolor.md)
  The component values defining a color in a specific color space.
- [class CIVector](civector.md)
  A container for coordinate values, direction vectors, matrices, and other non-scalar values, typically used in Core Image for filter parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilter)*