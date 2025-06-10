# kVTCompressionPropertyKey_VBVInitialDelayPercentage

**Framework**: Video Toolbox  
**Kind**: var

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
let kVTCompressionPropertyKey_VBVInitialDelayPercentage: CFString
```

#### Discussion

```None
Initial delay of the VBV model between storing the picture in the VBV buffer model and decoding of that picture, as a percentage of VBV buffer duration.
```

This value should be specified as a number in the range of 0 to 100. Larger value increases the delay but results in smoother playback. Default value is 90, meaning 90% of the VBV buffer duration. This property key is incompatible with:

1. kVTCompressionPropertyKey_AverageBitRate,
2. kVTCompressionPropertyKey_DataRateLimits,
3. VTVideoEncoderSpecification_EnableLowLatencyRateControl=True.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_vbvinitialdelaypercentage)*