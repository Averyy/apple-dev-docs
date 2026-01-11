# kVTCompressionPropertyKey_SuggestedLookAheadFrameCount

**Framework**: Video Toolbox  
**Kind**: var

A value that requests that the encoder retain the specified number of frames during encoding.

**Availability**:
- macOS 15.0+

## Declaration

```swift
let kVTCompressionPropertyKey_SuggestedLookAheadFrameCount: CFString
```

#### Discussion

These frames will be used for additional analysis and statistics gathering before the frame is finally encoded at the end of the window. When this property is not set, video encoder will automatically determine the number of lookahead frames.

Encoder will choose number of lookahead frames closer to the suggested value based on internal configuration. This property directly affects latency of the video encoder. The following properties also affect look ahead frames:

1. Value of this property must be less than or equal to `kVTCompressionPropertyKey_MaxFrameDelayCount`.
2. This property is ignored when `VTVideoEncoderSpecification_EnableLowLatencyRateControl` is set to true
3. This property is ignored when `kVTCompressionPropertyKey_Quality` is set to 1.0
4. This property can not be used in conjunction with multi-pass feature (`kVTCompressionPropertyKey_MultiPassStorage`)

## See Also

- [let kVTCompressionPropertyKey_ExpectedDuration: CFString](kvtcompressionpropertykey_expectedduration.md)
  The expected total duration of the compression session, if known.
- [let kVTCompressionPropertyKey_ExpectedFrameRate: CFString](kvtcompressionpropertykey_expectedframerate.md)
  The expected frame rate, if known.
- [let kVTCompressionPropertyKey_MaximumRealTimeFrameRate: CFString](kvtcompressionpropertykey_maximumrealtimeframerate.md)
  A value that specifies the maximum real time rate at which frames can be submitted to a compression session.
- [let kVTCompressionPropertyKey_PrioritizeEncodingSpeedOverQuality: CFString](kvtcompressionpropertykey_prioritizeencodingspeedoverquality.md)
  A hint for the video encoder to maximize its speed during encoding, sacrificing quality if needed.
- [let kVTCompressionPropertyKey_ReferenceBufferCount: CFString](kvtcompressionpropertykey_referencebuffercount.md)
- [let kVTCompressionPropertyKey_SourceFrameCount: CFString](kvtcompressionpropertykey_sourceframecount.md)
  The number of source frames, if known.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_suggestedlookaheadframecount)*