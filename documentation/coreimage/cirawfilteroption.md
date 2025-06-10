# CIRAWFilterOption

**Framework**: Core Image  
**Kind**: struct

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
struct CIRAWFilterOption
```

## Topics

### Initializers
- [init(rawValue: String)](cirawfilteroption/init(rawvalue:).md)
### Type Properties
- [static let activeKeys: CIRAWFilterOption](cirawfilteroption/activekeys.md)
  A key for the set of input keys available for use.
- [static let allowDraftMode: CIRAWFilterOption](cirawfilteroption/allowdraftmode.md)
  A key for allowing draft mode.
- [static let baselineExposure: CIRAWFilterOption](cirawfilteroption/baselineexposure.md)
  The amount of baseline exposure applied.
- [static let boostAmount: CIRAWFilterOption](cirawfilteroption/boostamount.md)
  A key for the amount of boost to apply to an image.
- [static let boostShadowAmount: CIRAWFilterOption](cirawfilteroption/boostshadowamount.md)
  A key for the amount to boost the shadow areas of the image.
- [static let ciInputEnableEDRModeKey: CIRAWFilterOption](cirawfilteroption/ciinputenableedrmodekey.md)
- [static let ciInputLocalToneMapAmountKey: CIRAWFilterOption](cirawfilteroption/ciinputlocaltonemapamountkey.md)
- [static let colorNoiseReductionAmount: CIRAWFilterOption](cirawfilteroption/colornoisereductionamount.md)
  A key for the amount of noise reduction to apply to color data in the image.
- [static let decoderVersion: CIRAWFilterOption](cirawfilteroption/decoderversion.md)
  A key for the version number of the method to be used for decoding. A newly initialized object defaults to the newest available decoder version for the given image type. You can request an alternative, older version to maintain compatibility with older releases. Must be one of the values listed for the [`supportedDecoderVersions`](cirawfilteroption/supporteddecoderversions.md) key, otherwise a `nil` output image is generated. The associated value must be an `NSNumber` object that specifies an integer value in range of `0` to the current decoder version. When you request a specific version of the decoder, Core Image produces an image that is  the same across different versions of the operating system. Core Image, however, does not guarantee that  the same bits are produced across different versions of the operating system. That’s because the rounding behavior of floating-point arithmetic can vary due to differences in compilers or hardware. Note that this option has no effect if the image used for initialization is not RAW.
- [static let disableGamutMap: CIRAWFilterOption](cirawfilteroption/disablegamutmap.md)
  Whether or not to disable gamut mapping.
- [static let enableChromaticNoiseTracking: CIRAWFilterOption](cirawfilteroption/enablechromaticnoisetracking.md)
  A key for progressive chromatic noise tracking (based on ISO and exposure time).
- [static let enableSharpening: CIRAWFilterOption](cirawfilteroption/enablesharpening.md)
  A key for the sharpening state.
- [static let enableVendorLensCorrection: CIRAWFilterOption](cirawfilteroption/enablevendorlenscorrection.md)
  A key for whether to automatically correct for image distortion from known lenses.
- [static let ignoreImageOrientation: CIRAWFilterOption](cirawfilteroption/ignoreimageorientation.md)
  A key for specifying whether to ignore the image orientation
- [static let imageOrientation: CIRAWFilterOption](cirawfilteroption/imageorientation.md)
  A key for the image orientation.
- [static let linearSpaceFilter: CIRAWFilterOption](cirawfilteroption/linearspacefilter.md)
  A key for the filter to apply to the image while it is temporarily in a linear color space as part of  RAW image processing. The associated value must be a [`CIFilter`](cifilter-swift.class.md) object.
- [static let luminanceNoiseReductionAmount: CIRAWFilterOption](cirawfilteroption/luminancenoisereductionamount.md)
  A key for the amount of noise reduction to apply to luminance data in the image.
- [static let moireAmount: CIRAWFilterOption](cirawfilteroption/moireamount.md)
  The amount of moiré reduction to apply.
- [static let neutralChromaticityX: CIRAWFilterOption](cirawfilteroption/neutralchromaticityx.md)
  The x value of the chromaticity.
- [static let neutralChromaticityY: CIRAWFilterOption](cirawfilteroption/neutralchromaticityy.md)
  The y value of the chromaticity.
- [static let neutralLocation: CIRAWFilterOption](cirawfilteroption/neutrallocation.md)
  A key for the neutral position. Use this key to set the location in geometric coordinates of the unrotated output image that should be used as neutral. You cannot query this value; it is undefined for reading. The associated value is a two-element [`CIVector`](civector.md) object that specifies the location (`x`, `y`).
- [static let neutralTemperature: CIRAWFilterOption](cirawfilteroption/neutraltemperature.md)
  A key for neutral temperature.
- [static let neutralTint: CIRAWFilterOption](cirawfilteroption/neutraltint.md)
  A key for the neutral tint.
- [static let noiseReductionAmount: CIRAWFilterOption](cirawfilteroption/noisereductionamount.md)
  A key for the amount to reduce noise in the image.
- [static let noiseReductionContrastAmount: CIRAWFilterOption](cirawfilteroption/noisereductioncontrastamount.md)
  A key for the amount of contrast enhancement to apply during noise reduction.
- [static let noiseReductionDetailAmount: CIRAWFilterOption](cirawfilteroption/noisereductiondetailamount.md)
  A key for the amount of detail enhancement to apply during noise reduction.
- [static let noiseReductionSharpnessAmount: CIRAWFilterOption](cirawfilteroption/noisereductionsharpnessamount.md)
  A key for the amount of sharpness enhancement to apply during noise reduction.
- [static let outputNativeSize: CIRAWFilterOption](cirawfilteroption/outputnativesize.md)
  A key for the full native size of the original, non-transformed RAW image. The associated value is a [`CIVector`](civector.md) object whose X and Y values are the image’s width and height. This key is read-only.
- [static let propertiesKey: CIRAWFilterOption](cirawfilteroption/propertieskey.md)
- [static let scaleFactor: CIRAWFilterOption](cirawfilteroption/scalefactor.md)
  A key for the scale factor.
- [static let supportedDecoderVersions: CIRAWFilterOption](cirawfilteroption/supporteddecoderversions.md)
  A key for the supported decoder versions.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init!(CVPixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(cvpixelbuffer:properties:options:).md)
  Creates a filter from a Core Video pixel buffer.
- [init!(imageData: Data!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(imagedata:options:).md)
  Creates a filter that allows the processing of RAW images.
- [init!(imageURL: URL!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(imageurl:options:).md)
  Creates a filter that allows the processing of RAW images.
- [class func serializedXMP(from: [CIFilter], inputImageExtent: CGRect) -> Data?](cifilter-swift.class/serializedxmp(from:inputimageextent:).md)
  Serializes filter parameters into XMP form that is suitable for embedding in an image.
- [class func filterArray(fromSerializedXMP: Data, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter]](cifilter-swift.class/filterarray(fromserializedxmp:inputimageextent:error:).md)
  Returns an array of filter objects de-serialized from XMP data.
- [class func supportedRawCameraModels() -> [String]!](cifilter-swift.class/supportedrawcameramodels.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilteroption)*