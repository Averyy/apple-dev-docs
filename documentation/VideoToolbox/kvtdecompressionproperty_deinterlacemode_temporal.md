# kVTDecompressionProperty_DeinterlaceMode_Temporal

**Framework**: Video Toolbox  
**Kind**: var

A temporal deinterlace mode.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTDecompressionProperty_DeinterlaceMode_Temporal: CFString
```

#### Discussion

Applies a filter that uses a window of multiple frames to generate deinterlaced results, and provides a better result at the expense of a pipeline delay.

This mode is only used if [`kVTDecodeFrame_EnableTemporalProcessing`](vtdecodeframeflags/kvtdecodeframe_enabletemporalprocessing.md) is set, otherwise a non-temporal mode will be used instead.

## See Also

- [let kVTDecompressionProperty_DeinterlaceMode_VerticalFilter: CFString](kvtdecompressionproperty_deinterlacemode_verticalfilter.md)
  A vertical filter deinterlace mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionproperty_deinterlacemode_temporal)*