# VTDecompressionSessionDecodeFrameWithMultiImageCapableOutputHandler

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Decompresses a multi-image frame and calls the specified output handler upon completion.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```c
extern OSStatus VTDecompressionSessionDecodeFrameWithMultiImageCapableOutputHandler(VTDecompressionSessionRef session, CMSampleBufferRef sampleBuffer, VTDecodeFrameFlags decodeFlags, VTDecodeInfoFlags *infoFlagsOut, VTDecompressionMultiImageCapableOutputHandler multiImageCapableOutputHandler);
```

## Parameters

- `session`: The decompression session.
- `sampleBuffer`: A CMSampleBuffer containing one or more video frames.
- `decodeFlags`: A bitfield of directives to the decompression session and decoder. The kVTDecodeFrame_EnableAsynchronousDecompression bit indicates whether the video decoder may decompress the frame asynchronously. The kVTDecodeFrame_EnableTemporalProcessing bit indicates whether the decoder may delay calls to the output callback so as to enable processing in temporal (display) order. If both flags are clear, the decompression shall complete and your output callback function will be called before VTDecompressionSessionDecodeFrame returns. If either flag is set, VTDecompressionSessionDecodeFrame may return before the output callback function is called.
- `infoFlagsOut`: Points to a VTDecodeInfoFlags to receive information about the decode operation. The kVTDecodeInfo_Asynchronous bit may be set if the decode is (or was) running asynchronously. The kVTDecodeInfo_FrameDropped bit may be set if the frame was dropped (synchronously). Pass NULL if you do not want to receive this information.
- `multiImageCapableOutputHandler`: A block for the system to call when it finished decoding the frame. If the [`VTDecompressionSessionDecodeFrameWithMultiImageCapableOutputHandler`](./vtdecompressionsessiondecodeframewithmultiimagecapableoutputhandler.md) call returns an error, the block isn’t called.

## Topics

### Output Handler
- [typealias VTDecompressionMultiImageCapableOutputHandler](./vtdecompressionmultiimagecapableoutputhandler.md)
  A type alias for callback that the system invokes when it finishes decompressing a frame.

## See Also

### Decoding Multi-Image Frames
- [func VTIsStereoMVHEVCDecodeSupported() -> Bool](./vtisstereomvhevcdecodesupported%28%29.md)
  Returns a Boolean value that indicates whether the system supports MV-HEVC decoding.
- [VTDecompressionSessionSetMultiImageCallback](./vtdecompressionsessionsetmultiimagecallback.md)
  Provides a callback capable of receiving multiple images for individual frame decoding requests.
- [typealias VTDecompressionMultiImageCapableOutputHandler](./vtdecompressionmultiimagecapableoutputhandler.md)
  A type alias for callback that the system invokes when it finishes decompressing a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsessiondecodeframewithmultiimagecapableoutputhandler)*