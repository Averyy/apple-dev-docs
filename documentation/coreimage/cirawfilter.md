# CIRAWFilter

**Framework**: Core Image  
**Kind**: class

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
class CIRAWFilter
```

#### Overview

Use this class to generate a [`CIImage`](ciimage.md) object based on the configuration parameters you provide.

You can use this object in conjunction with other Core Image classes—such as [`CIFilter`](cifilter-swift.class.md) and [`CIContext`](cicontext.md)—to take advantage of the built-in Core Image filters when processing images or writing custom filters.

You can also query this object to find out about the supported camera models, decoders, and filters.

## Topics

### Creating a filter
- [convenience init?(cvPixelBuffer: CVPixelBuffer, properties: [AnyHashable : Any])](cirawfilter/init(cvpixelbuffer:properties:).md)
  Creates a RAW filter from the pixel buffer and its properties that you specify.
- [convenience init?(imageData: Data, identifierHint: String?)](cirawfilter/init(imagedata:identifierhint:).md)
  Creates a RAW filter from the image data and type hint that you specify.
- [convenience init?(imageURL: URL)](cirawfilter/init(imageurl:).md)
  Creates a RAW filter from the image at the URL location that you specify.
### Inspecting supported camera models, decoders, and filters
- [class var supportedCameraModels: [String]](cirawfilter/supportedcameramodels.md)
  An array containing the names of all supported camera models.
- [var supportedDecoderVersions: [CIRAWDecoderVersion]](cirawfilter/supporteddecoderversions.md)
  An array of all supported decoder versions for the given image type.
- [struct CIRAWDecoderVersion](cirawdecoderversion.md)
- [var isColorNoiseReductionSupported: Bool](cirawfilter/iscolornoisereductionsupported.md)
  A Boolean that indicates if the current image supports color noise reduction adjustments.
- [var isContrastSupported: Bool](cirawfilter/iscontrastsupported.md)
  A Boolean that indicates if the current image supports contrast adjustments.
- [var isDetailSupported: Bool](cirawfilter/isdetailsupported.md)
  A Boolean that indicates if the current image supports detail enhancement adjustments.
- [var isLensCorrectionSupported: Bool](cirawfilter/islenscorrectionsupported.md)
  A Boolean that indicates if you can enable lens correction for the current image.
- [var isLocalToneMapSupported: Bool](cirawfilter/islocaltonemapsupported.md)
  A Boolean that indicates if the current image supports local tone curve adjustments.
- [var isLuminanceNoiseReductionSupported: Bool](cirawfilter/isluminancenoisereductionsupported.md)
  A Boolean that indicates if the current image supports luminance noise reduction adjustments.
- [var isMoireReductionSupported: Bool](cirawfilter/ismoirereductionsupported.md)
  A Boolean that indicates if the current image supports moire artifact reduction adjustments.
- [var isSharpnessSupported: Bool](cirawfilter/issharpnesssupported.md)
  A Boolean that indicates if the current image supports sharpness adjustments.
- [var nativeSize: CGSize](cirawfilter/nativesize.md)
  The full native size of the unscaled image.
### Configuring a filter
- [var baselineExposure: Float](cirawfilter/baselineexposure.md)
  A value that indicates the baseline exposure to apply to the image.
- [var boostAmount: Float](cirawfilter/boostamount.md)
  A value that indicates the amount of global tone curve to apply to the image.
- [var boostShadowAmount: Float](cirawfilter/boostshadowamount.md)
  A value that indicates the amount to boost the shadow areas of the image.
- [var colorNoiseReductionAmount: Float](cirawfilter/colornoisereductionamount.md)
  A value that indicates the amount of chroma noise reduction to apply to the image.
- [var contrastAmount: Float](cirawfilter/contrastamount.md)
  A value that indicates the amount of local contrast to apply to the edges of the image.
- [var decoderVersion: CIRAWDecoderVersion](cirawfilter/decoderversion.md)
  A value that indicates the decoder version to use.
- [var detailAmount: Float](cirawfilter/detailamount.md)
  A value that indicates the amount of detail enhancement to apply to the edges of the image.
- [var exposure: Float](cirawfilter/exposure.md)
  A value that indicates the amount of exposure to apply to the image.
- [var extendedDynamicRangeAmount: Float](cirawfilter/extendeddynamicrangeamount.md)
  A value that indicates the amount of extended dynamic range (EDR) to apply to the image.
- [var isDraftModeEnabled: Bool](cirawfilter/isdraftmodeenabled.md)
  A Boolean that indicates whether to enable draft mode.
- [var isGamutMappingEnabled: Bool](cirawfilter/isgamutmappingenabled.md)
  A Boolean that indicates whether to enable gamut mapping.
- [var isLensCorrectionEnabled: Bool](cirawfilter/islenscorrectionenabled.md)
  A Boolean that indicates whether to enable lens correction.
- [var linearSpaceFilter: CIFilter?](cirawfilter/linearspacefilter.md)
  An optional filter you can apply to the RAW image while it’s in linear space.
- [var localToneMapAmount: Float](cirawfilter/localtonemapamount.md)
  A value that indicates the amount of local tone curve to apply to the image.
- [var luminanceNoiseReductionAmount: Float](cirawfilter/luminancenoisereductionamount.md)
  A value that indicates the amount of luminance noise reduction to apply to the image.
- [var moireReductionAmount: Float](cirawfilter/moirereductionamount.md)
  A value that indicates the amount of moire artifact reduction to apply to high frequency areas of the image.
- [var neutralChromaticity: CGPoint](cirawfilter/neutralchromaticity.md)
  A value that indicates the amount of white balance based on chromaticity values to apply to the image.
- [var neutralLocation: CGPoint](cirawfilter/neutrallocation.md)
  A value that indicates the amount of white balance based on pixel coordinates to apply to the image.
- [var neutralTemperature: Float](cirawfilter/neutraltemperature.md)
  A value that indicates the amount of white balance based on temperature values to apply to the image.
- [var neutralTint: Float](cirawfilter/neutraltint.md)
  A value that indicates the amount of white balance based on tint values to apply to the image.
- [var orientation: CGImagePropertyOrientation](cirawfilter/orientation.md)
  A value that indicates the orientation of the image.
- [var portraitEffectsMatte: CIImage?](cirawfilter/portraiteffectsmatte.md)
  An optional auxiliary image that represents the portrait effects matte of the image.
- [var previewImage: CIImage?](cirawfilter/previewimage.md)
  An optional auxiliary image that represents a preview of the original image.
- [var properties: [AnyHashable : Any]](cirawfilter/properties.md)
  A dictionary that contains properties of the image source.
- [var scaleFactor: Float](cirawfilter/scalefactor.md)
  A value that indicates the desired scale factor to draw the output image.
- [var semanticSegmentationGlassesMatte: CIImage?](cirawfilter/semanticsegmentationglassesmatte.md)
  An optional auxiliary image that represents the semantic segmentation glasses matte of the image.
- [var semanticSegmentationHairMatte: CIImage?](cirawfilter/semanticsegmentationhairmatte.md)
  An optional auxiliary image that represents the semantic segmentation hair matte of the image.
- [var semanticSegmentationSkinMatte: CIImage?](cirawfilter/semanticsegmentationskinmatte.md)
  An optional auxiliary image that represents the semantic segmentation skin matte of the image.
- [var semanticSegmentationSkyMatte: CIImage?](cirawfilter/semanticsegmentationskymatte.md)
  An optional auxiliary image that represents the semantic segmentation sky matte of the image.
- [var semanticSegmentationTeethMatte: CIImage?](cirawfilter/semanticsegmentationteethmatte.md)
  An optional auxiliary image that represents the semantic segmentation teeth matte of the image.
- [var shadowBias: Float](cirawfilter/shadowbias.md)
  A value that indicates the amount to subtract from the shadows in the image.
- [var sharpnessAmount: Float](cirawfilter/sharpnessamount.md)
  A value that indicates the amount of sharpness to apply to the edges of the image.
### Instance Properties
- [var isHighlightRecoveryEnabled: Bool](cirawfilter/ishighlightrecoveryenabled.md)
- [var isHighlightRecoverySupported: Bool](cirawfilter/ishighlightrecoverysupported.md)

## Relationships

### Inherits From
- [CIFilter](cifilter-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CIFilter](cifilter-swift.class.md)
  An image processor that produces an image by manipulating one or more input images or by generating new image data.
- [class CIColor](cicolor.md)
  The Core Image class that defines a color object.
- [class CIVector](civector.md)
  The Core Image class that defines a vector object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilter)*