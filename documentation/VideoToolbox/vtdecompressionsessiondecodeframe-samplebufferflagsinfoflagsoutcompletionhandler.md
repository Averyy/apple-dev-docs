# VTDecompressionSessionDecodeFrame(_:sampleBuffer:flags:infoFlagsOut:completionHandler:)

**Framework**: Video Toolbox  
**Kind**: func

Decompresses a video frame and calls the provided output closure when decompression completes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func VTDecompressionSessionDecodeFrame(_ session: VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags decodeFlags: VTDecodeFrameFlags, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, completionHandler: @escaping (OSStatus, VTDecodeInfoFlags, CVImageBuffer?, [CMTaggedBuffer]?, CMTime, CMTime) -> Void) -> OSStatus
```

#### Return Value

An `OSStatus` value that indicates the result of the operation.

#### Discussion

This function cannot be called with a session created with a [`VTDecompressionOutputCallbackRecord`](vtdecompressionoutputcallbackrecord.md).

## Parameters

- `session`: The decompression session.
- `sampleBuffer`: A   object containing one or more video frames.
- `decodeFlags`: If both flags are clear, the decompression shall complete and your output callback function will be called before   returns. If either flag is set,   may return before the output callback function is called.
- `infoFlagsOut`: Pass   if you do not want to receive this information.
- `completionHandler`: The closure to be called when decoding the frame is completed. If the VTDecompressionSessionDecodeFrame call returns an error, the closure will not be called.

## See Also

- [func VTDecompressionSessionCanAcceptFormatDescription(VTDecompressionSession, formatDescription: CMFormatDescription) -> Bool](vtdecompressionsessioncanacceptformatdescription(_:formatdescription:).md)
  Indicates whether the session can decode frames with the given format description.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, frameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?) -> OSStatus](vtdecompressionsessiondecodeframe(_:samplebuffer:flags:framerefcon:infoflagsout:).md)
  Decompresses a video frame.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, outputHandler: VTDecompressionOutputHandler) -> OSStatus](vtdecompressionsessiondecodeframe(_:samplebuffer:flags:infoflagsout:outputhandler:).md)
  Decompresses a video frame and invokes the output callback when the decompression completes.
- [func VTDecompressionSessionFinishDelayedFrames(VTDecompressionSession) -> OSStatus](vtdecompressionsessionfinishdelayedframes(_:).md)
  Directs the decompression session to emit all delayed frames.
- [func VTDecompressionSessionWaitForAsynchronousFrames(VTDecompressionSession) -> OSStatus](vtdecompressionsessionwaitforasynchronousframes(_:).md)
  Waits for any and all outstanding asynchronous and delayed frames to complete, then returns.
- [func VTDecompressionSessionCopyBlackPixelBuffer(VTDecompressionSession, pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> OSStatus](vtdecompressionsessioncopyblackpixelbuffer(_:pixelbufferout:).md)
  Copies a black pixel buffer from the decompression session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsessiondecodeframe(_:samplebuffer:flags:infoflagsout:completionhandler:))*