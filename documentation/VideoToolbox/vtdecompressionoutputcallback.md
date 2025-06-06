# VTDecompressionOutputCallback

**Framework**: Videotoolbox  
**Kind**: typealias

The prototype for the callback invoked when frame decompression is complete.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
typealias VTDecompressionOutputCallback = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, OSStatus, VTDecodeInfoFlags, CVImageBuffer?, CMTime, CMTime) -> Void
```

#### Discussion

When you create a decompression session, you pass in a callback function to be called for decompressed frames.  This function is not necessarily called in display order.

## Parameters

- `decompressionOutputRefCon`: The callback’s reference value, copied from the   field of the   structure.
- `sourceFrameRefCon`: The frame’s reference value, copied from the   argument to  .
- `status`:   if decompression was successful; an error code if decompression was not successful.
- `infoFlags`: If the   bit is set, it is safe for the client to modify the imageBuffer.
- `imageBuffer`: The decompressed frame, if decompression was successful; otherwise,  .
- `presentationTimeStamp`: The frame’s presentation timestamp, which is determined by calling  ; otherwise,   if the timestamp is not available.
- `presentationDuration`: The frame’s presentation duration, which is determined by calling  ; otherwise,   if the timestamp is not available.

## See Also

- [class VTDecompressionSession](vtdecompressionsession.md)
  A reference to a decompression session.
- [struct VTDecodeFrameFlags](vtdecodeframeflags.md)
  Flags to pass to a decompression session and the video decoder.
- [struct VTDecodeInfoFlags](vtdecodeinfoflags.md)
  Flags that provide information about the status of a decode operation.
- [struct VTDecompressionOutputCallbackRecord](vtdecompressionoutputcallbackrecord.md)
- [typealias VTDecompressionOutputHandler](vtdecompressionoutputhandler.md)
  The prototype for the block invoked when frame decompression is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputcallback)*