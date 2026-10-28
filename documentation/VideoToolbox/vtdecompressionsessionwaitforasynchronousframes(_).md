# VTDecompressionSessionWaitForAsynchronousFrames(_:)

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Waits for any and all outstanding asynchronous and delayed frames to complete, then returns.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTDecompressionSessionWaitForAsynchronousFrames(_ session: VTDecompressionSession) -> OSStatus
```

```c
extern OSStatus VTDecompressionSessionWaitForAsynchronousFrames(VTDecompressionSessionRef session);
```

## Return Value

An `OSStatus` value that indicates the result of the operation.

## Discussion

This function automatically calls [`VTDecompressionSessionFinishDelayedFrames(_:)`](./vtdecompressionsessionfinishdelayedframes%28_%29.md),  so clients don’t have to call both.

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
- [func VTDecompressionSessionFinishDelayedFrames(VTDecompressionSession) -> OSStatus](./vtdecompressionsessionfinishdelayedframes%28_%29.md)
  Directs the decompression session to emit all delayed frames.
- [func VTDecompressionSessionCopyBlackPixelBuffer(VTDecompressionSession, pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> OSStatus](./vtdecompressionsessioncopyblackpixelbuffer%28_,pixelbufferout%29.md)
  Copies a black pixel buffer from the decompression session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsessionwaitforasynchronousframes(_:))*