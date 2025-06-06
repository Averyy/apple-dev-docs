# CIRAWDecoderVersion

**Framework**: Core Image  
**Kind**: struct

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct CIRAWDecoderVersion
```

## Topics

### Initializers
- [init(rawValue: String)](cirawdecoderversion/3802023-init.md)
### Type Properties
- [static let none: CIRAWDecoderVersion](cirawdecoderversion/3801613-none.md)
- [static let version6: CIRAWDecoderVersion](cirawdecoderversion/3801607-version6.md)
- [static let version6DNG: CIRAWDecoderVersion](cirawdecoderversion/3801608-version6dng.md)
- [static let version7: CIRAWDecoderVersion](cirawdecoderversion/3801609-version7.md)
- [static let version7DNG: CIRAWDecoderVersion](cirawdecoderversion/3801610-version7dng.md)
- [static let version8: CIRAWDecoderVersion](cirawdecoderversion/3801611-version8.md)
- [static let version8DNG: CIRAWDecoderVersion](cirawdecoderversion/3801612-version8dng.md)

## Relationships

### Conforms To
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)

## See Also

- [class var supportedCameraModels: [String]](cirawfilter/3801659-supportedcameramodels.md)
  An array containing the names of all supported camera models.
- [var supportedDecoderVersions: [CIRAWDecoderVersion]](cirawfilter/3801660-supporteddecoderversions.md)
  An array of all supported decoder versions for the given image type.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawdecoderversion)*