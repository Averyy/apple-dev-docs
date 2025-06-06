# exposure

**Framework**: Core Image  
**Kind**: instp

A value that indicates the amount of exposure to apply to the image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var exposure: Float { get set }
```

#### Discussion

The default value is `0`.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilter/3801626-exposure)*