# kVTCompressionPropertyKey_VariableBitRate

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
let kVTCompressionPropertyKey_VariableBitRate: CFString
```

#### Discussion

Requires that the encoder use a variable bitrate (VBR) rate control algorithm and specifies the desired variable bitrate in bits per second.

The actual peak bitrate present in the bitstream may be above or below this value based on other parameters such as kVTCompressionPropertyKey_VBVMaxBitRate. This property key needs to be set to achieve Variable Bitrate (VBR) rate control. This property key is not compatible with:

1. kVTCompressionPropertyKey_AverageBitRate,
2. kVTCompressionPropertyKey_ConstantBitRate,
3. kVTCompressionPropertyKey_DataRateLimits,
4. VTVideoEncoderSpecification_EnableLowLatencyRateControl = True.

## See Also

- [let kVTCompressionPropertyKey_AverageBitRate: CFString](kvtcompressionpropertykey_averagebitrate.md)
  The long-term desired average bit rate in bits per second.
- [let kVTCompressionPropertyKey_ConstantBitRate: CFString](kvtcompressionpropertykey_constantbitrate.md)
  Requires that the encoder use a Constant Bit Rate algorithm.
- [let kVTCompressionPropertyKey_DataRateLimits: CFString](kvtcompressionpropertykey_dataratelimits.md)
  Zero, one, or two hard limits on data rate.
- [let kVTCompressionPropertyKey_EstimatedAverageBytesPerFrame: CFString](kvtcompressionpropertykey_estimatedaveragebytesperframe.md)
  An estimate of the expected size in bytes of a single encoded frame based on the current configuration.
- [let kVTCompressionPropertyKey_MoreFramesAfterEnd: CFString](kvtcompressionpropertykey_moreframesafterend.md)
  A Boolean value indicating whether and how a compression session concatenates frames with other compressed frames to form a longer series.
- [let kVTCompressionPropertyKey_MoreFramesBeforeStart: CFString](kvtcompressionpropertykey_moreframesbeforestart.md)
  A Boolean value that indicates whether and how a compression session concatenates frames with other compressed frames to form a longer series.
- [let kVTCompressionPropertyKey_Quality: CFString](kvtcompressionpropertykey_quality.md)
  The desired compression quality.
- [let kVTCompressionPropertyKey_TargetQualityForAlpha: CFString](kvtcompressionpropertykey_targetqualityforalpha.md)
  The target quality to use for encoding the alpha channel.
- [let kVTCompressionPropertyKey_VBVBufferDuration: CFString](kvtcompressionpropertykey_vbvbufferduration.md)
- [let kVTCompressionPropertyKey_VBVInitialDelayPercentage: CFString](kvtcompressionpropertykey_vbvinitialdelaypercentage.md)
- [let kVTCompressionPropertyKey_VBVMaxBitRate: CFString](kvtcompressionpropertykey_vbvmaxbitrate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_variablebitrate)*