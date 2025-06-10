# kVTCompressionPropertyKey_VBVMaxBitRate

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
let kVTCompressionPropertyKey_VBVMaxBitRate: CFString
```

#### Discussion

```None
Defines the maximum bitrate that can enter the video buffering verifier (VBV) model at any time in variable bitrate (VBR) mode.
```

The value of this property must be greater than zero. This property key is not compatible with:

1. kVTCompressionPropertyKey_AverageBitRate,
2. kVTCompressionPropertyKey_ConstantBitRate,
3. kVTCompressionPropertyKey_DataRateLimits,
4. VTVideoEncoderSpecification_EnableLowLatencyRateControl=True.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_vbvmaxbitrate)*