# kVTCompressionPropertyKey_EstimatedAverageBytesPerFrame

**Framework**: Video Toolbox  
**Kind**: var

An estimate of the expected size in bytes of a single encoded frame based on the current configuration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_EstimatedAverageBytesPerFrame: CFString
```

## See Also

- [let kVTCompressionPropertyKey_AverageBitRate: CFString](kvtcompressionpropertykey_averagebitrate.md)
  The long-term desired average bit rate in bits per second.
- [let kVTCompressionPropertyKey_ConstantBitRate: CFString](kvtcompressionpropertykey_constantbitrate.md)
  Requires that the encoder use a Constant Bit Rate algorithm.
- [let kVTCompressionPropertyKey_DataRateLimits: CFString](kvtcompressionpropertykey_dataratelimits.md)
  Zero, one, or two hard limits on data rate.
- [let kVTCompressionPropertyKey_MoreFramesAfterEnd: CFString](kvtcompressionpropertykey_moreframesafterend.md)
  A Boolean value indicating whether and how a compression session concatenates frames with other compressed frames to form a longer series.
- [let kVTCompressionPropertyKey_MoreFramesBeforeStart: CFString](kvtcompressionpropertykey_moreframesbeforestart.md)
  A Boolean value that indicates whether and how a compression session concatenates frames with other compressed frames to form a longer series.
- [let kVTCompressionPropertyKey_Quality: CFString](kvtcompressionpropertykey_quality.md)
  The desired compression quality.
- [let kVTCompressionPropertyKey_TargetQualityForAlpha: CFString](kvtcompressionpropertykey_targetqualityforalpha.md)
  The target quality to use for encoding the alpha channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_estimatedaveragebytesperframe)*