# noiseReductionContrastAmount

**Framework**: Core Image  
**Kind**: property

A key for the amount of contrast enhancement to apply during noise reduction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static let noiseReductionContrastAmount: CIRAWFilterOption
```

#### Discussion

The value for this key is a [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a value between `0.0` and `1.0`.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilteroption/noisereductioncontrastamount)*