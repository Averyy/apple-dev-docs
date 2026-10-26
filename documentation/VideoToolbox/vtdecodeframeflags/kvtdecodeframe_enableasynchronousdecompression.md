# kVTDecodeFrame_EnableAsynchronousDecompression

**Framework**: Video Toolbox  
**Kind**: case  
**Role**: Enumeration Case

A flag that indicates to enable asynchronous decompression.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```c
kVTDecodeFrame_EnableAsynchronousDecompression
```

#### Discussion

With this bit cleared, the video decoder emits every frame before it returns. With the bit set, the decoder may process frames asynchronously, but it’s not compelled to do so.

## See Also

### Flags
- [kVTDecodeFrame_1xRealTimePlayback](./kvtdecodeframe_1xrealtimeplayback.md)
  A flag that provides a hint to the video decoder that it’s ok to use a low-power mode that can’t decode faster than realtime.
- [kVTDecodeFrame_DoNotOutputFrame](./kvtdecodeframe_donotoutputframe.md)
  A flag that provides a hint to the decompression session and video decoder not to return a frame.
- [kVTDecodeFrame_EnableTemporalProcessing](./kvtdecodeframe_enabletemporalprocessing.md)
  A flag that indicates to enable temporal processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecodeframeflags/kvtdecodeframe_enableasynchronousdecompression)*