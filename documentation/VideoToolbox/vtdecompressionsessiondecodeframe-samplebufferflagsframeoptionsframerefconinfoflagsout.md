# VTDecompressionSessionDecodeFrame(_:sampleBuffer:flags:frameOptions:frameRefcon:infoFlagsOut:)

**Framework**: Video Toolbox  
**Kind**: func

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func VTDecompressionSessionDecodeFrame(_ session: VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags decodeFlags: VTDecodeFrameFlags, frameOptions: CFDictionary?, frameRefcon sourceFrameRefCon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?) -> OSStatus
```

#### Discussion

Decompresses a video frame.

If an error is returned from this function, there will be no callback.  Otherwise the callback provided during VTDecompressionSessionCreate will be called.

## Parameters

- `session`: The decompression session.
- `sampleBuffer`: A CMSampleBuffer containing one or more video frames.
- `decodeFlags`: A bitfield of directives to the decompression session and decoder. The kVTDecodeFrame_EnableAsynchronousDecompression bit indicates whether the video decoder may decompress the frame asynchronously. The kVTDecodeFrame_EnableTemporalProcessing bit indicates whether the decoder may delay calls to the output callback so as to enable processing in temporal (display) order. If both flags are clear, the decompression shall complete and your output callback function will be called before VTDecompressionSessionDecodeFrameWithOptions returns. If either flag is set, VTDecompressionSessionDecodeFrameWithOptions may return before the output callback function is called.
- `frameOptions`: Contains key/value pairs specifying additional options for decoding this frame. Only keys with `kVTDecodeFrameOptionKey_` prefix should be used in this dictionary.
- `sourceFrameRefCon`: Your reference value for the frame. Note that if sampleBuffer contains multiple frames, the output callback function will be called multiple times with this sourceFrameRefCon.
- `infoFlagsOut`: Points to a VTDecodeInfoFlags to receive information about the decode operation. The kVTDecodeInfo_Asynchronous bit may be set if the decode is (or was) running asynchronously. The kVTDecodeInfo_FrameDropped bit may be set if the frame was dropped (synchronously). Pass NULL if you do not want to receive this information.

## See Also

- [func VTDecompressionSessionCanAcceptFormatDescription(VTDecompressionSession, formatDescription: CMFormatDescription) -> Bool](vtdecompressionsessioncanacceptformatdescription(_:formatdescription:).md)
  Indicates whether the session can decode frames with the given format description.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, frameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?) -> OSStatus](vtdecompressionsessiondecodeframe(_:samplebuffer:flags:framerefcon:infoflagsout:).md)
  Decompresses a video frame.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, outputHandler: VTDecompressionOutputHandler) -> OSStatus](vtdecompressionsessiondecodeframe(_:samplebuffer:flags:infoflagsout:outputhandler:).md)
  Decompresses a video frame and invokes the output callback when the decompression completes.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, frameOptions: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, outputHandler: VTDecompressionOutputHandler) -> OSStatus](vtdecompressionsessiondecodeframe(_:samplebuffer:flags:frameoptions:infoflagsout:outputhandler:).md)
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, completionHandler: (OSStatus, VTDecodeInfoFlags, CVImageBuffer?, [CMTaggedBuffer]?, CMTime, CMTime) -> Void) -> OSStatus](vtdecompressionsessiondecodeframe(_:samplebuffer:flags:infoflagsout:completionhandler:).md)
  Decompresses a video frame and calls the provided output closure when decompression completes.
- [func VTDecompressionSessionFinishDelayedFrames(VTDecompressionSession) -> OSStatus](vtdecompressionsessionfinishdelayedframes(_:).md)
  Directs the decompression session to emit all delayed frames.
- [func VTDecompressionSessionWaitForAsynchronousFrames(VTDecompressionSession) -> OSStatus](vtdecompressionsessionwaitforasynchronousframes(_:).md)
  Waits for any and all outstanding asynchronous and delayed frames to complete, then returns.
- [func VTDecompressionSessionCopyBlackPixelBuffer(VTDecompressionSession, pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> OSStatus](vtdecompressionsessioncopyblackpixelbuffer(_:pixelbufferout:).md)
  Copies a black pixel buffer from the decompression session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsessiondecodeframe(_:samplebuffer:flags:frameoptions:framerefcon:infoflagsout:))*