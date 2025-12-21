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
- `decodeFlags`: A bitfield of directives to the decompression session and decoder.   The kVTDecodeFrame_EnableAsynchronousDecompression bit indicates whether the video decoder   may decompress the frame asynchronously.   The kVTDecodeFrame_EnableTemporalProcessing bit indicates whether the decoder may delay calls to the output callback   so as to enable processing in temporal (display) order.   If both flags are clear, the decompression shall complete and your output callback function will be called   before VTDecompressionSessionDecodeFrameWithOptions returns.   If either flag is set, VTDecompressionSessionDecodeFrameWithOptions may return before the output callback function is called.
- `frameOptions`: Contains key/value pairs specifying additional options for decoding this frame.   Only keys with   prefix should be used in this dictionary.
- `sourceFrameRefCon`: Your reference value for the frame.   Note that if sampleBuffer contains multiple frames, the output callback function will be called   multiple times with this sourceFrameRefCon.
- `infoFlagsOut`: Points to a VTDecodeInfoFlags to receive information about the decode operation.   The kVTDecodeInfo_Asynchronous bit may be set if the decode is (or was) running   asynchronously.   The kVTDecodeInfo_FrameDropped bit may be set if the frame was dropped (synchronously).   Pass NULL if you do not want to receive this information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsessiondecodeframe(_:samplebuffer:flags:frameoptions:framerefcon:infoflagsout:))*