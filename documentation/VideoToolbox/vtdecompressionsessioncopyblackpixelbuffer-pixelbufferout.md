# VTDecompressionSessionCopyBlackPixelBuffer(_:pixelBufferOut:)

**Framework**: Video Toolbox  
**Kind**: func

Copies a black pixel buffer from the decompression session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTDecompressionSessionCopyBlackPixelBuffer(_ session: VTDecompressionSession, pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> OSStatus
```

#### Return Value

An `OSStatus` value that indicates the result of the operation.

#### Discussion

The pixel buffer is in the same format as the decompression session.

## Parameters

- `session`: The decompression session.
- `pixelBufferOut`: A pointer to receive the copied pixel buffer.

## See Also

- [func VTDecompressionSessionCanAcceptFormatDescription(VTDecompressionSession, formatDescription: CMFormatDescription) -> Bool](vtdecompressionsessioncanacceptformatdescription(_:formatdescription:).md)
  Indicates whether the session can decode frames with the given format description.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, frameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?) -> OSStatus](vtdecompressionsessiondecodeframe(_:samplebuffer:flags:framerefcon:infoflagsout:).md)
  Decompresses a video frame.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, outputHandler: VTDecompressionOutputHandler) -> OSStatus](vtdecompressionsessiondecodeframe(_:samplebuffer:flags:infoflagsout:outputhandler:).md)
  Decompresses a video frame and invokes the output callback when the decompression completes.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, completionHandler: (OSStatus, VTDecodeInfoFlags, CVImageBuffer?, [CMTaggedBuffer]?, CMTime, CMTime) -> Void) -> OSStatus](vtdecompressionsessiondecodeframe(_:samplebuffer:flags:infoflagsout:completionhandler:).md)
  Decompresses a video frame and calls the provided output closure when decompression completes.
- [func VTDecompressionSessionFinishDelayedFrames(VTDecompressionSession) -> OSStatus](vtdecompressionsessionfinishdelayedframes(_:).md)
  Directs the decompression session to emit all delayed frames.
- [func VTDecompressionSessionWaitForAsynchronousFrames(VTDecompressionSession) -> OSStatus](vtdecompressionsessionwaitforasynchronousframes(_:).md)
  Waits for any and all outstanding asynchronous and delayed frames to complete, then returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsessioncopyblackpixelbuffer(_:pixelbufferout:))*