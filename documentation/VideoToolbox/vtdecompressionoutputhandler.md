# VTDecompressionOutputHandler

**Framework**: Video Toolbox  
**Kind**: typealias

The prototype for the block invoked when frame decompression is complete.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
typealias VTDecompressionOutputHandler = (OSStatus, VTDecodeInfoFlags, CVImageBuffer?, CMTime, CMTime) -> Void
```

#### Discussion

When you decode a frame, you pass in a callback block to be called for that decompressed frame.  This block is not necessarily called in display order.

## Parameters

- `status`:   if decompression was successful; an error code if decompression was not successful.
- `infoFlags`: If the   bit is set, it is safe for the client to modify the imageBuffer.
- `imageBuffer`: The decompressed frame, if decompression was successful; otherwise,  .
- `presentationTimeStamp`: The frame’s presentation timestamp; otherwise,   if the timestamp is not available.
- `presentationDuration`: The frame’s presentation duration; kCMTimeInvalid if the timestamp is not available.

## See Also

- [class VTDecompressionSession](vtdecompressionsession.md)
  A reference to a decompression session.
- [struct VTDecodeFrameFlags](vtdecodeframeflags.md)
  Flags to pass to a decompression session and the video decoder.
- [struct VTDecodeInfoFlags](vtdecodeinfoflags.md)
  Flags that provide information about the status of a decode operation.
- [typealias VTDecompressionOutputCallback](vtdecompressionoutputcallback.md)
  The prototype for the callback invoked when frame decompression is complete.
- [struct VTDecompressionOutputCallbackRecord](vtdecompressionoutputcallbackrecord.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputhandler)*