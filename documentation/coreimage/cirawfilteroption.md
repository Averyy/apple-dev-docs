# CIRAWFilterOption

**Framework**: Core Image  
**Kind**: struct

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.5+ - Deprecated in 12.0
- tvOS 10.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
struct CIRAWFilterOption
```

## Topics

### Initializers
- [init(rawValue: String)](cirawfilteroption/2998475-init.md)
### Type Properties
- [static let activeKeys: CIRAWFilterOption](cirawfilteroption/1438129-activekeys.md)
  A key for the set of input keys available for use. The associated value is an [`NSSet`](https://developer.apple.com/documentation/foundation/nsset) object containing the set of input keys which may be used to affect the output image. (Depending on the input image type and the decoder version, some input keys may be unavailable.) This key is read-only.
- [static let allowDraftMode: CIRAWFilterOption](cirawfilteroption/1438010-allowdraftmode.md)
  A key for allowing draft mode. The associated value is a Boolean value packaged as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object.  It’s best not to use draft mode if the image needs to be drawn without draft mode at a later time, because changing the value from [`true`](https://developer.apple.com/documentation/swift/true) to [`false`](https://developer.apple.com/documentation/swift/false) is an expensive operation. If the optional scale factor is smaller than a certain value, additionally setting draft mode can improve image decoding speed without any perceivable loss of quality. However, turning on draft mode does not have any effect if the scale factor is not below this threshold.
- [static let baselineExposure: CIRAWFilterOption](cirawfilteroption/2202263-baselineexposure.md)
  A key for an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object containing a float that expresses the amount of baseline exposure applied to an image.
- [static let boostAmount: CIRAWFilterOption](cirawfilteroption/1438098-boostamount.md)
  A key for the amount of boost to apply to an image. The associated value is a floating-point value packaged as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object. The value must be in the range of `0...1`. A value of `0` indicates no boost, that is, a linear response. The default value is `1`, which indicates full boost.
- [static let boostShadowAmount: CIRAWFilterOption](cirawfilteroption/1438066-boostshadowamount.md)
  A key for the amount to boost the shadow areas of the image. The associated value must be an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object that specifies floating-point value. The value has no effect if the image used for initialization is not RAW.
- [static let ciInputEnableEDRModeKey: CIRAWFilterOption](cirawfilteroption/3334940-ciinputenableedrmodekey.md)
- [static let ciInputLocalToneMapAmountKey: CIRAWFilterOption](cirawfilteroption/3697067-ciinputlocaltonemapamountkey.md)
- [static let colorNoiseReductionAmount: CIRAWFilterOption](cirawfilteroption/1437640-colornoisereductionamount.md)
  A key for the amount of noise reduction to apply to color data in the image.
- [static let decoderVersion: CIRAWFilterOption](cirawfilteroption/1438193-decoderversion.md)
  A key for the version number of the method to be used for decoding. A newly initialized object defaults to the newest available decoder version for the given image type. You can request an alternative, older version to maintain compatibility with older releases. Must be one of the values listed for the [`supportedDecoderVersions`](cirawfilteroption/1437927-supporteddecoderversions.md) key, otherwise a `nil` output image is generated. The associated value must be an `NSNumber` object that specifies an integer value in range of `0` to the current decoder version. When you request a specific version of the decoder, Core Image produces an image that is  the same across different versions of the operating system. Core Image, however, does not guarantee that  the same bits are produced across different versions of the operating system. That’s because the rounding behavior of floating-point arithmetic can vary due to differences in compilers or hardware. Note that this option has no effect if the image used for initialization is not RAW.
- [static let disableGamutMap: CIRAWFilterOption](cirawfilteroption/2202264-disablegamutmap.md)
  A key for an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object containing a Boolean value that determines whether or not to disable gamut mapping.
- [static let enableChromaticNoiseTracking: CIRAWFilterOption](cirawfilteroption/1438231-enablechromaticnoisetracking.md)
  A key for progressive chromatic noise tracking (based on ISO and exposure time). The associated value must be an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object that specifies a `BOOL` value ([`true`](https://developer.apple.com/documentation/swift/true) or [`false`](https://developer.apple.com/documentation/swift/false)). The default is [`true`](https://developer.apple.com/documentation/swift/true). This option has no effect if the image used for initialization is not RAW.
- [static let enableSharpening: CIRAWFilterOption](cirawfilteroption/1438016-enablesharpening.md)
  A key for the sharpening state. The associated value must be an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object that specifies a `BOOL` value ([`true`](https://developer.apple.com/documentation/swift/true) or [`false`](https://developer.apple.com/documentation/swift/false)). The default is [`true`](https://developer.apple.com/documentation/swift/true). This option has no effect if the image used for initialization is not RAW.
- [static let enableVendorLensCorrection: CIRAWFilterOption](cirawfilteroption/1437715-enablevendorlenscorrection.md)
  A key for whether to automatically correct for image distortion from known lenses.
- [static let ignoreImageOrientation: CIRAWFilterOption](cirawfilteroption/1437949-ignoreimageorientation.md)
  A key for specifying whether to ignore the image orientation. The associated value is a Boolean value packaged as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object.  The default value is [`false`](https://developer.apple.com/documentation/swift/false). An image is usually loaded in its proper orientation, as long as the associated metadata records its orientation. For special purposes you might want to load the image in its physical orientation. The exact meaning of "physical orientation” is dependent on the specific image.
- [static let imageOrientation: CIRAWFilterOption](cirawfilteroption/1437637-imageorientation.md)
  A key for the image orientation. The associated value is an integer value packaged as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object. Valid values are in range `1...8` and follow the EXIF specification. The value is disregarded when the `kCIIgnoreImageOrientationKey` flag is set. You can change the orientation of the image by overriding this value. By changing this value you can rotate an image in 90-degree increments.
- [static let linearSpaceFilter: CIRAWFilterOption](cirawfilteroption/1438078-linearspacefilter.md)
  A key for the filter to apply to the image while it is temporarily in a linear color space as part of  RAW image processing. The associated value must be a [`CIFilter`](cifilter.md) object.
- [static let luminanceNoiseReductionAmount: CIRAWFilterOption](cirawfilteroption/1437945-luminancenoisereductionamount.md)
  A key for the amount of noise reduction to apply to luminance data in the image.
- [static let moireAmount: CIRAWFilterOption](cirawfilteroption/2880265-moireamount.md)
  A key for an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object containing a double that expresses the amount of moiré reduction applied to an image.
- [static let neutralChromaticityX: CIRAWFilterOption](cirawfilteroption/1437605-neutralchromaticityx.md)
  The x value of the chromaticity.  The associated value is a floating-point value packaged as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object.  You can query this value to get the current x value for neutral x, y.
- [static let neutralChromaticityY: CIRAWFilterOption](cirawfilteroption/1438039-neutralchromaticityy.md)
  The y value of the chromaticity.  The associated value is a floating-point value packaged as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object.  You can query this value to get the current y value for neutral x, y.
- [static let neutralLocation: CIRAWFilterOption](cirawfilteroption/1437915-neutrallocation.md)
  A key for the neutral position. Use this key to set the location in geometric coordinates of the unrotated output image that should be used as neutral. You cannot query this value; it is undefined for reading. The associated value is a two-element [`CIVector`](civector.md) object that specifies the location (`x`, `y`). 
- [static let neutralTemperature: CIRAWFilterOption](cirawfilteroption/1438177-neutraltemperature.md)
  A key for neutral temperature. The associated value is a floating-point value packaged as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object. You can query this value to get the current temperature value.
- [static let neutralTint: CIRAWFilterOption](cirawfilteroption/1438113-neutraltint.md)
  A key for the neutral tint. The associated value is a floating-point value packaged as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object. Use this key to set or fetch the temperature and tint values.  You can query this value to get the current tint value.
- [static let noiseReductionAmount: CIRAWFilterOption](cirawfilteroption/1437990-noisereductionamount.md)
  A key for the amount to reduce noise in the image. The associated value must be an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object that specifies a floating-point value between `0.0` and `1.0`. The value has no effect if the image used for initialization is not RAW.
- [static let noiseReductionContrastAmount: CIRAWFilterOption](cirawfilteroption/1437681-noisereductioncontrastamount.md)
  A key for the amount of contrast enhancement to apply during noise reduction.
- [static let noiseReductionDetailAmount: CIRAWFilterOption](cirawfilteroption/1437943-noisereductiondetailamount.md)
  A key for the amount of detail enhancement to apply during noise reduction.
- [static let noiseReductionSharpnessAmount: CIRAWFilterOption](cirawfilteroption/1438009-noisereductionsharpnessamount.md)
  A key for the amount of sharpness enhancement to apply during noise reduction.
- [static let outputNativeSize: CIRAWFilterOption](cirawfilteroption/1438050-outputnativesize.md)
  A key for the full native size of the original, non-transformed RAW image. The associated value is a [`CIVector`](civector.md) object whose X and Y values are the image’s width and height. This key is read-only.
- [static let propertiesKey: CIRAWFilterOption](cirawfilteroption/3750393-propertieskey.md)
- [static let scaleFactor: CIRAWFilterOption](cirawfilteroption/1437936-scalefactor.md)
  A key for the scale factor. The associated value is a floating-point value packaged as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object that specifies the desired scale factor at which the image will be drawn. Setting this value can greatly improve the drawing performance. A value of `1` is the identity. In some cases, if you change the scale factor and enable draft mode, performance can decrease. See [`allowDraftMode`](cirawfilteroption/1438010-allowdraftmode.md).
- [static let supportedDecoderVersions: CIRAWFilterOption](cirawfilteroption/1437927-supporteddecoderversions.md)
  A key for the supported decoder versions. The associated value is  an [`NSArray`](https://developer.apple.com/documentation/foundation/nsarray) object that contains all supported decoder versions for the given image type, sorted in increasingly newer order. Each entry is an [`NSDictionary`](https://developer.apple.com/documentation/foundation/nsdictionary) object that contains key-value pairs. All entries represent a valid version identifier that can be passed as the `kCIDecoderVersion` value for the key `kCIDecoderMethodKey`. Version values are read-only; attempting to set this value raises an exception. Currently, the only defined key is `@"version"` which has as its value an [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) that uniquely describing a given decoder version. This string might not be suitable for user interface display.. 

## Relationships

### Conforms To
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)

## See Also

- [init!(cvPixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]!)](cifilter/2138288-init.md)
  Creates a filter from a Core Video pixel buffer.
- [init!(imageData: Data!, options: [CIRAWFilterOption : Any]!)](cifilter/1437879-init.md)
  Creates a filter that allows the processing of RAW images.
- [init!(imageURL: URL!, options: [CIRAWFilterOption : Any]!)](cifilter/1438096-init.md)
  Creates a filter that allows the processing of RAW images.
- [class func serializedXMP(from: [CIFilter], inputImageExtent: CGRect) -> Data?](cifilter/1438006-serializedxmp.md)
  Serializes filter parameters into XMP form that is suitable for embedding in an image.
- [class func filterArray(fromSerializedXMP: Data, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter]](cifilter/1438237-filterarray.md)
  Returns an array of filter objects de-serialized from XMP data.
- [class func supportedRawCameraModels() -> [String]!](cifilter/3242782-supportedrawcameramodels.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilteroption)*