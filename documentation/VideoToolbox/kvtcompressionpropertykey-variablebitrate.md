# kVTCompressionPropertyKey_VariableBitRate

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
let kVTCompressionPropertyKey_VariableBitRate: CFString
```

#### Discussion

```None
Requires that the encoder use a variable bitrate (VBR) rate control algorithm and specifies the desired variable bitrate in bits per second.
```

The actual peak bitrate present in the bitstream may be above or below this value based on other parameters such as kVTCompressionPropertyKey_VBVMaxBitRate. This property key needs to be set to achieve Variable Bitrate (VBR) rate control. This property key is not compatible with:

1. kVTCompressionPropertyKey_AverageBitRate,
2. kVTCompressionPropertyKey_ConstantBitRate,
3. kVTCompressionPropertyKey_DataRateLimits,
4. VTVideoEncoderSpecification_EnableLowLatencyRateControl = True.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_variablebitrate)*