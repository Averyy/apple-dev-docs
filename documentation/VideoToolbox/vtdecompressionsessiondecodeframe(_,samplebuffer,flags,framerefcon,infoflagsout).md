# VTDecompressionSessionDecodeFrame(_:sampleBuffer:flags:frameRefcon:infoFlagsOut:)

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus VTDecompressionSessionDecodeFrame(VTDecompressionSessionRef session, CMSampleBufferRef sampleBuffer, VTDecodeFrameFlags decodeFlags, void *sourceFrameRefCon, VTDecodeInfoFlags *infoFlagsOut);
```

#### Return Value

An `OSStatus` value that indicates the result of the operation.

## Parameters

- `session`: The decompression session.
- `sampleBuffer`: A [`CMSampleBuffer`](../CoreMedia/cmsamplebuffer.md) object containing one or more video frames.
- `decodeFlags`: A bitfield of directives to the decompression session and decoder.

  The [`kVTDecodeFrame_EnableAsynchronousDecompression`](./vtdecodeframeflags/kvtdecodeframe_enableasynchronousdecompression.md) bit indicates whether the video decoder may decompress the frame asynchronously.

  The [`kVTDecodeFrame_EnableTemporalProcessing`](./vtdecodeframeflags/kvtdecodeframe_enabletemporalprocessing.md) bit indicates whether the decoder may delay calls to the output callback so as to enable processing in temporal (display) order.

  If both flags are clear, the decompression completes and your output callback function will be called before `VTDecompressionSessionDecodeFrame` returns. If either flag is set, `VTDecompressionSessionDecodeFrame` may return before the output callback function is called.
- `sourceFrameRefCon`: Your reference value for the frame.  Note that if `sampleBuffer` contains multiple frames, the output callback function is called multiple times with this `sourceFrameRefCon` value.
- `infoFlagsOut`: A [`VTEncodeInfoFlags`](./vtencodeinfoflags.md) pointer to receive information about the decode operation.

  The [`asynchronous`](./vtdecodeinfoflags/asynchronous.md) bit may be set if the decode is (or was) running asynchronously.

  The [`frameDropped`](./vtdecodeinfoflags/framedropped.md) bit may be set if the frame was dropped (synchronously).

  Pass `NULL` if you do not want to receive this information.

## See Also

### Decoding Frames
- [func VTDecompressionSessionCanAcceptFormatDescription(VTDecompressionSession, formatDescription: CMFormatDescription) -> Bool](./vtdecompressionsessioncanacceptformatdescription%28_,formatdescription%29.md)
  Indicates whether the session can decode frames with the given format description.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, frameOptions: CFDictionary?, frameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?) -> OSStatus](./vtdecompressionsessiondecodeframe%28_,samplebuffer,flags,frameoptions,framerefcon,infoflagsout%29.md)
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, outputHandler: VTDecompressionOutputHandler) -> OSStatus](./vtdecompressionsessiondecodeframe%28_,samplebuffer,flags,infoflagsout,outputhandler%29.md)
  Decompresses a video frame and invokes the output callback when the decompression completes.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, frameOptions: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, outputHandler: VTDecompressionOutputHandler) -> OSStatus](./vtdecompressionsessiondecodeframe%28_,samplebuffer,flags,frameoptions,infoflagsout,outputhandler%29.md)
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, completionHandler: (OSStatus, VTDecodeInfoFlags, CVImageBuffer?, [CMTaggedBuffer]?, CMTime, CMTime) -> Void) -> OSStatus](./vtdecompressionsessiondecodeframe%28_,samplebuffer,flags,infoflagsout,completionhandler%29.md)
  Decompresses a video frame and calls the provided output closure when decompression completes.
- [func VTDecompressionSessionFinishDelayedFrames(VTDecompressionSession) -> OSStatus](./vtdecompressionsessionfinishdelayedframes%28_%29.md)
  Directs the decompression session to emit all delayed frames.
- [func VTDecompressionSessionWaitForAsynchronousFrames(VTDecompressionSession) -> OSStatus](./vtdecompressionsessionwaitforasynchronousframes%28_%29.md)
  Waits for any and all outstanding asynchronous and delayed frames to complete, then returns.
- [func VTDecompressionSessionCopyBlackPixelBuffer(VTDecompressionSession, pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> OSStatus](./vtdecompressionsessioncopyblackpixelbuffer%28_,pixelbufferout%29.md)
  Copies a black pixel buffer from the decompression session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsessiondecodeframe(_:samplebuffer:flags:framerefcon:infoflagsout:))*