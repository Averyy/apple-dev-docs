# kVTVideoEncoderSpecification_EncoderID

**Framework**: Videotoolbox  
**Kind**: var

A key that indicates a particular video encoder to use.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTVideoEncoderSpecification_EncoderID: CFString
```

#### Discussion

To specify a particular video encoder when creating a compression session, pass an encoder specification doc://com.apple.documentation/documentation/corefoundation/cfdictionary-rum containing this key and the encoder ID as its value. You can get the encoder ID string from the `kVTVideoEncoderList_EncoderID` entry in the array returned by [`VTCopyVideoEncoderList(_:_:)`](vtcopyvideoencoderlist(_:_:).md).

## See Also

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
- [let kVTCompressionPropertyKey_SpatialAdaptiveQPLevel: CFString](kvtcompressionpropertykey_spatialadaptiveqplevel.md)
  A value that controls spatial adaptation of the quantization parameter (QP) based on per-frame statistics.
- [let kVTCompressionPropertyKey_SuggestedLookAheadFrameCount: CFString](kvtcompressionpropertykey_suggestedlookaheadframecount.md)
  A value that requests that the encoder retain the specified number of frames during encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderspecification_encoderid)*