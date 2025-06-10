# VTDecompressionSessionCanAcceptFormatDescription(_:formatDescription:)

**Framework**: Video Toolbox  
**Kind**: func

Indicates whether the session can decode frames with the given format description.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTDecompressionSessionCanAcceptFormatDescription(_ session: VTDecompressionSession, formatDescription newFormatDesc: CMFormatDescription) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the decompression session accepts the format description; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Some video decoders can accommodate minor changes in format without needing to be completely reset in a new session.  Use this function to test whether a format change is sufficiently minor.

## Parameters

- `session`: The decompression session.
- `newFormatDesc`: The   to test.

## See Also

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
- [func VTDecompressionSessionCopyBlackPixelBuffer(VTDecompressionSession, pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> OSStatus](vtdecompressionsessioncopyblackpixelbuffer(_:pixelbufferout:).md)
  Copies a black pixel buffer from the decompression session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsessioncanacceptformatdescription(_:formatdescription:))*