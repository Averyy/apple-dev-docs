# kVTCompressionPropertyKey_MaximumRealTimeFrameRate

**Framework**: Video Toolbox  
**Kind**: var

A value that specifies the maximum real time rate at which frames can be submitted to a compression session.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let kVTCompressionPropertyKey_MaximumRealTimeFrameRate: CFString
```

#### Discussion

The frame rate is measured in frames per second. This property can be used to inform the encoder of the maximum rate that frames could be submitted to the encoder during realtime encoding.  This allows the encoder to configure itself to ensure this capability.

This property can only be used when [`kVTCompressionPropertyKey_RealTime`](kvtcompressionpropertykey_realtime.md) has been set to true.

Unlike [`kVTCompressionPropertyKey_ExpectedFrameRate`](kvtcompressionpropertykey_expectedframerate.md), this property informs the maximum possible rate that the compression session could see, not the average frame rate that is expected in normal operation.

By default, the property has a value of zero indicating “unknown”.

## See Also

- [let kVTCompressionPropertyKey_ExpectedDuration: CFString](kvtcompressionpropertykey_expectedduration.md)
  The expected total duration of the compression session, if known.
- [let kVTCompressionPropertyKey_ExpectedFrameRate: CFString](kvtcompressionpropertykey_expectedframerate.md)
  The expected frame rate, if known.
- [let kVTCompressionPropertyKey_PrioritizeEncodingSpeedOverQuality: CFString](kvtcompressionpropertykey_prioritizeencodingspeedoverquality.md)
  A hint for the video encoder to maximize its speed during encoding, sacrificing quality if needed.
- [let kVTCompressionPropertyKey_ReferenceBufferCount: CFString](kvtcompressionpropertykey_referencebuffercount.md)
- [let kVTCompressionPropertyKey_SourceFrameCount: CFString](kvtcompressionpropertykey_sourceframecount.md)
  The number of source frames, if known.
- [let kVTCompressionPropertyKey_SuggestedLookAheadFrameCount: CFString](kvtcompressionpropertykey_suggestedlookaheadframecount.md)
  A value that requests that the encoder retain the specified number of frames during encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_maximumrealtimeframerate)*