# kVTCompressionPropertyKey_VBVBufferDuration

**Framework**: Video Toolbox  
**Kind**: var

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let kVTCompressionPropertyKey_VBVBufferDuration: CFString
```

#### Discussion

Capacity of the video buffering verifier (VBV) model in seconds.

VBV model allows for larger variations in bitrates while avoiding decoder-side overflows or underflows. A larger VBV model size may improve compression quality, but it requires more memory and may introduce delay. The value of this property must be greater than 0.0. The default value is set as 2.5 seconds. This property key is compatible with constant bitrate (CBR) or variable bitrate (VBR) rate control. This property key is incompatible with:

1. kVTCompressionPropertyKey_AverageBitRate,
2. kVTCompressionPropertyKey_DataRateLimits,
3. VTVideoEncoderSpecification_EnableLowLatencyRateControl=True.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_vbvbufferduration)*