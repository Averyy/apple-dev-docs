# VTDecompressionSessionFinishDelayedFrames(_:)

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Directs the decompression session to emit all delayed frames.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTDecompressionSessionFinishDelayedFrames(_ session: VTDecompressionSession) -> OSStatus
```

```c
extern OSStatus VTDecompressionSessionFinishDelayedFrames(VTDecompressionSessionRef session);
```

## Return Value

An `OSStatus` value that indicates the result of the operation.

## Discussion

By default, the decompression session may not delay frames indefinitely;  frames may only be indefinitely delayed if the client opts in via [`kVTDecodeFrame_EnableTemporalProcessing`](./vtdecodeframeflags/kvtdecodeframe_enabletemporalprocessing.md).

> ❗ **Important**:  This function may return before all delayed frames are emitted.  To wait for them, call [`VTDecompressionSessionWaitForAsynchronousFrames(_:)`](./vtdecompressionsessionwaitforasynchronousframes%28_%29.md) instead.

## Parameters

- `session`: The decompression session.

## See Also

### Decoding Frames
- [func VTDecompressionSessionCanAcceptFormatDescription(VTDecompressionSession, formatDescription: CMFormatDescription) -> Bool](./vtdecompressionsessioncanacceptformatdescription%28_,formatdescription%29.md)
  Indicates whether the session can decode frames with the given format description.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, frameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?) -> OSStatus](./vtdecompressionsessiondecodeframe%28_,samplebuffer,flags,framerefcon,infoflagsout%29.md)
  Decompresses a video frame.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, frameOptions: CFDictionary?, frameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?) -> OSStatus](./vtdecompressionsessiondecodeframe%28_,samplebuffer,flags,frameoptions,framerefcon,infoflagsout%29.md)
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, outputHandler: VTDecompressionOutputHandler) -> OSStatus](./vtdecompressionsessiondecodeframe%28_,samplebuffer,flags,infoflagsout,outputhandler%29.md)
  Decompresses a video frame and invokes the output callback when the decompression completes.
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, frameOptions: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, outputHandler: VTDecompressionOutputHandler) -> OSStatus](./vtdecompressionsessiondecodeframe%28_,samplebuffer,flags,frameoptions,infoflagsout,outputhandler%29.md)
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, completionHandler: (OSStatus, VTDecodeInfoFlags, CVImageBuffer?, [CMTaggedBuffer]?, CMTime, CMTime) -> Void) -> OSStatus](./vtdecompressionsessiondecodeframe%28_,samplebuffer,flags,infoflagsout,completionhandler%29.md)
  Decompresses a video frame and calls the provided output closure when decompression completes.
- [func VTDecompressionSessionWaitForAsynchronousFrames(VTDecompressionSession) -> OSStatus](./vtdecompressionsessionwaitforasynchronousframes%28_%29.md)
  Waits for any and all outstanding asynchronous and delayed frames to complete, then returns.
- [func VTDecompressionSessionCopyBlackPixelBuffer(VTDecompressionSession, pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> OSStatus](./vtdecompressionsessioncopyblackpixelbuffer%28_,pixelbufferout%29.md)
  Copies a black pixel buffer from the decompression session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsessionfinishdelayedframes(_:))*