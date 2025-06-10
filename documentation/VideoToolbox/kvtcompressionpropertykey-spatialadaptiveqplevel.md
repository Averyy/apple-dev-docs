# kVTCompressionPropertyKey_SpatialAdaptiveQPLevel

**Framework**: Video Toolbox  
**Kind**: var

A value that controls spatial adaptation of the quantization parameter (QP) based on per-frame statistics.

**Availability**:
- macOS 15.0+

## Declaration

```swift
let kVTCompressionPropertyKey_SpatialAdaptiveQPLevel: CFString
```

#### Discussion

If set to [`kVTQPModulationLevel_Disable`](kvtqpmodulationlevel_disable.md), spatial QP adaptation is not applied based on per-frame statistics. If set to [`kVTQPModulationLevel_Default`](kvtqpmodulationlevel_default.md), video encoder is allowed to apply spatial QP adaptation for each macro block (or coding unit) within a video frame. QP adaptation is based on spatial characteristics of a frame and the level of spatial QP adaptation is decided internally by the rate controller.

## Topics

### Levels
- [var kVTQPModulationLevel_Default: Int](kvtqpmodulationlevel_default.md)
- [var kVTQPModulationLevel_Disable: Int](kvtqpmodulationlevel_disable.md)

## See Also

- [let kVTVideoEncoderSpecification_EncoderID: CFString](kvtvideoencoderspecification_encoderid.md)
  A key that indicates a particular video encoder to use.
- [let kVTCompressionPropertyKey_RecommendedParallelizationLimit: CFString](kvtcompressionpropertykey_recommendedparallelizationlimit.md)
  The recommended number of compression sessions to instantiate in a parallel encoding configuration.
- [let kVTCompressionPropertyKey_RecommendedParallelizedSubdivisionMinimumDuration: CFString](kvtcompressionpropertykey_recommendedparallelizedsubdivisionminimumduration.md)
  The recommended minimum duration for a given subdivision in a parallel encoding configuration.
- [let kVTCompressionPropertyKey_RecommendedParallelizedSubdivisionMinimumFrameCount: CFString](kvtcompressionpropertykey_recommendedparallelizedsubdivisionminimumframecount.md)
  The recommended minimum number of video frames for a given subdivision in a parallel encoding configuration.
- [let kVTCompressionPropertyKey_EnableLTR: CFString](kvtcompressionpropertykey_enableltr.md)
  Enables Long Term Reference (LTR) frames during encoding.
- [let kVTCompressionPropertyKey_EncoderID: CFString](kvtcompressionpropertykey_encoderid.md)
  Specifies a particular video encoder by its ID string.
- [let kVTCompressionPropertyKey_MinAllowedFrameQP: CFString](kvtcompressionpropertykey_minallowedframeqp.md)
  The minimum allowed encoded frame QP (Quantization Parameter).
- [let kVTCompressionPropertyKey_MaxAllowedFrameQP: CFString](kvtcompressionpropertykey_maxallowedframeqp.md)
  The maximum allowed encoded frame QP (Quantization Parameter).
- [let kVTCompressionPropertyKey_PreserveDynamicHDRMetadata: CFString](kvtcompressionpropertykey_preservedynamichdrmetadata.md)
  Specifies whether to preserve dynamic HDR metadata on the input pixel buffer.
- [let kVTEncodeFrameOptionKey_AcknowledgedLTRTokens: CFString](kvtencodeframeoptionkey_acknowledgedltrtokens.md)
  Enable Long Term Reference (LTR) frames during encoding.
- [let kVTEncodeFrameOptionKey_ForceLTRRefresh: CFString](kvtencodeframeoptionkey_forceltrrefresh.md)
  A Boolean value that indicates whether to force Long Term Reference (LTR).
- [let kVTSampleAttachmentKey_RequireLTRAcknowledgementToken: CFString](kvtsampleattachmentkey_requireltracknowledgementtoken.md)
  A number value that contains a unique token for this Long Term Reference (LTR).
- [let kVTVideoEncoderSpecification_EnableLowLatencyRateControl: CFString](kvtvideoencoderspecification_enablelowlatencyratecontrol.md)
  Specifies to select an encoder that supports low-latency operation and enables low-latency mode.
- [let kVTCompressionPropertyKey_SuggestedLookAheadFrameCount: CFString](kvtcompressionpropertykey_suggestedlookaheadframecount.md)
  A value that requests that the encoder retain the specified number of frames during encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_spatialadaptiveqplevel)*