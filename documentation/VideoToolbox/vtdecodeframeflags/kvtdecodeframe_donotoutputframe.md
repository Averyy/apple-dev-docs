# kVTDecodeFrame_DoNotOutputFrame

**Framework**: Video Toolbox  
**Kind**: case  
**Role**: Enumeration Case

A flag that provides a hint to the decompression session and video decoder not to return a frame.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```c
kVTDecodeFrame_DoNotOutputFrame
```

## Discussion

This flag indicates to return NULL for this frame instead of a [`CVImageBuffer`](../../CoreVideo/cvimagebuffer.md).

## See Also

### Flags
- [kVTDecodeFrame_1xRealTimePlayback](./kvtdecodeframe_1xrealtimeplayback.md)
  A flag that provides a hint to the video decoder that it’s ok to use a low-power mode that can’t decode faster than realtime.
- [kVTDecodeFrame_EnableAsynchronousDecompression](./kvtdecodeframe_enableasynchronousdecompression.md)
  A flag that indicates to enable asynchronous decompression.
- [kVTDecodeFrame_EnableTemporalProcessing](./kvtdecodeframe_enabletemporalprocessing.md)
  A flag that indicates to enable temporal processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecodeframeflags/kvtdecodeframe_donotoutputframe)*