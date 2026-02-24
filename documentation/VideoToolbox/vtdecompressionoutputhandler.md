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
typealias VTDecompressionOutputHandler = @Sendable (OSStatus, VTDecodeInfoFlags, CVImageBuffer?, CMTime, CMTime) -> Void
```

#### Discussion

When you decode a frame, you pass in a callback block to be called for that decompressed frame.  This block is not necessarily called in display order.

## Parameters

- `status`: `noErr` if decompression was successful; an error code if decompression was not successful.
- `infoFlags`: Information about the decode operation. The [`asynchronous`](vtdecodeinfoflags/asynchronous.md) bit may be set if the decode ran asynchronously. The [`frameDropped`](vtdecodeinfoflags/framedropped.md) bit may be set if the frame was dropped. If the [`imageBufferModifiable`](vtdecodeinfoflags/imagebuffermodifiable.md) bit is set, it is safe for the client to modify the imageBuffer.
- `imageBuffer`: The decompressed frame, if decompression was successful; otherwise, `NULL`. > ❗ **Important**:  The video decompressor may still be referencing the `imageBuffer` returned in this callback if the [`imageBufferModifiable`](vtdecodeinfoflags/imagebuffermodifiable.md) flag is not set.  Unless this flag is set, it is not safe to modify the returned `imageBuffer`.
- `presentationTimeStamp`: The frame’s presentation timestamp; otherwise, `kCMTimeInvalid` if the timestamp is not available.
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