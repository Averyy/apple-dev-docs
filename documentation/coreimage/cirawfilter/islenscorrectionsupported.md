# isLensCorrectionSupported

**Framework**: Core Image  
**Kind**: property

A Boolean that indicates if you can enable lens correction for the current image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var isLensCorrectionSupported: Bool { get }
```

#### Discussion

If this value is [`true`](https://developer.apple.com/documentation/swift/true), you can enable lens correction on the image by setting [`isLensCorrectionEnabled`](cirawfilter/islenscorrectionenabled.md) to [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilter/islenscorrectionsupported)*