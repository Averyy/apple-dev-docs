# VTDecompressionSessionDecodeFrame(_:sampleBuffer:flags:frameRefcon:infoFlagsOut:)

**Framework**: Video Toolbox  
**Kind**: func

Decompresses a video frame.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTDecompressionSessionDecodeFrame(_ session: VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags decodeFlags: VTDecodeFrameFlags, frameRefcon sourceFrameRefCon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?) -> OSStatus
```

#### Return Value

An `OSStatus` value that indicates the result of the operation.

## Parameters

- `session`: The decompression session.
- `sampleBuffer`: A   object containing one or more video frames.
- `decodeFlags`: If both flags are clear, the decompression completes and your output callback function will be called before   returns. If either flag is set,   may return before the output callback function is called.
- `sourceFrameRefCon`: Your reference value for the frame.  Note that if   contains multiple frames, the output callback function is called multiple times with this   value.
- `infoFlagsOut`: Pass   if you do not want to receive this information.

## See Also

- [func VTDecompressionSessionCanAcceptFormatDescription(VTDecompressionSession, formatDescription: CMFormatDescription) -> Bool](vtdecompressionsessioncanacceptformatdescription(_:formatdescription:).md)
  Indicates whether the session can decode frames with the given format description.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, outputHandler: VTDecompressionOutputHandler) -> OSStatus](vtdecompressionsessiondecodeframe(_:samplebuffer:flags:infoflagsout:outputhandler:).md)
  Decompresses a video frame and invokes the output callback when the decompression completes.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, completionHandler: (OSStatus, VTDecodeInfoFlags, CVImageBuffer?, [CMTaggedBuffer]?, CMTime, CMTime) -> Void) -> OSStatus](vtdecompressionsessiondecodeframe(_:samplebuffer:flags:infoflagsout:completionhandler:).md)
  Decompresses a video frame and calls the provided output closure when decompression completes.
- [func VTDecompressionSessionFinishDelayedFrames(VTDecompressionSession) -> OSStatus](vtdecompressionsessionfinishdelayedframes(_:).md)
  Directs the decompression session to emit all delayed frames.
- [func VTDecompressionSessionWaitForAsynchronousFrames(VTDecompressionSession) -> OSStatus](vtdecompressionsessionwaitforasynchronousframes(_:).md)
  Waits for any and all outstanding asynchronous and delayed frames to complete, then returns.
- [func VTDecompressionSessionCopyBlackPixelBuffer(VTDecompressionSession, pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> OSStatus](vtdecompressionsessioncopyblackpixelbuffer(_:pixelbufferout:).md)
  Copies a black pixel buffer from the decompression session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsessiondecodeframe(_:samplebuffer:flags:framerefcon:infoflagsout:))*