# kCIInputBiasKey

**Framework**: Core Image  
**Kind**: var

Simple bias value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let kCIInputBiasKey: String
```

#### Discussion

A key for the simple bias value to use along with the exposure adjustment ([`kCIInputEVKey`](kciinputevkey.md)). The associated value must be an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object that specifies floating-point value. The value has no effect if the image used for initialization is not RAW.

## See Also

- [static let decoderVersion: CIRAWFilterOption](cirawfilteroption/decoderversion.md)
  A key for the version number of the method to be used for decoding. A newly initialized object defaults to the newest available decoder version for the given image type. You can request an alternative, older version to maintain compatibility with older releases. Must be one of the values listed for the [`supportedDecoderVersions`](cirawfilteroption/supporteddecoderversions.md) key, otherwise a `nil` output image is generated. The associated value must be an `NSNumber` object that specifies an integer value in range of `0` to the current decoder version. When you request a specific version of the decoder, Core Image produces an image that is  the same across different versions of the operating system. Core Image, however, does not guarantee that  the same bits are produced across different versions of the operating system. That’s because the rounding behavior of floating-point arithmetic can vary due to differences in compilers or hardware. Note that this option has no effect if the image used for initialization is not RAW.
- [static let supportedDecoderVersions: CIRAWFilterOption](cirawfilteroption/supporteddecoderversions.md)
  A key for the supported decoder versions.
- [static let boostAmount: CIRAWFilterOption](cirawfilteroption/boostamount.md)
  A key for the amount of boost to apply to an image.
- [static let neutralChromaticityX: CIRAWFilterOption](cirawfilteroption/neutralchromaticityx.md)
  The x value of the chromaticity.
- [static let neutralChromaticityY: CIRAWFilterOption](cirawfilteroption/neutralchromaticityy.md)
  The y value of the chromaticity.
- [static let neutralTemperature: CIRAWFilterOption](cirawfilteroption/neutraltemperature.md)
  A key for neutral temperature.
- [static let neutralTint: CIRAWFilterOption](cirawfilteroption/neutraltint.md)
  A key for the neutral tint.
- [static let neutralLocation: CIRAWFilterOption](cirawfilteroption/neutrallocation.md)
  A key for the neutral position. Use this key to set the location in geometric coordinates of the unrotated output image that should be used as neutral. You cannot query this value; it is undefined for reading. The associated value is a two-element [`CIVector`](civector.md) object that specifies the location (`x`, `y`).
- [static let scaleFactor: CIRAWFilterOption](cirawfilteroption/scalefactor.md)
  A key for the scale factor.
- [static let allowDraftMode: CIRAWFilterOption](cirawfilteroption/allowdraftmode.md)
  A key for allowing draft mode.
- [static let ignoreImageOrientation: CIRAWFilterOption](cirawfilteroption/ignoreimageorientation.md)
  A key for specifying whether to ignore the image orientation
- [static let imageOrientation: CIRAWFilterOption](cirawfilteroption/imageorientation.md)
  A key for the image orientation.
- [static let enableSharpening: CIRAWFilterOption](cirawfilteroption/enablesharpening.md)
  A key for the sharpening state.
- [static let enableChromaticNoiseTracking: CIRAWFilterOption](cirawfilteroption/enablechromaticnoisetracking.md)
  A key for progressive chromatic noise tracking (based on ISO and exposure time).
- [static let noiseReductionAmount: CIRAWFilterOption](cirawfilteroption/noisereductionamount.md)
  A key for the amount to reduce noise in the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/kciinputbiaskey)*