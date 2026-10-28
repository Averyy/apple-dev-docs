# VTDecompressionSessionSetMultiImageCallback

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Provides a callback capable of receiving multiple images for individual frame decoding requests.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```c
extern OSStatus VTDecompressionSessionSetMultiImageCallback(VTDecompressionSessionRef decompressionSession, VTDecompressionOutputMultiImageCallback outputMultiImageCallback, void *outputMultiImageRefcon);
```

## Return Value

An `OSStatus` value that indicates the result of the operation.

## Discussion

In multi-image decompression, a single video sample contains a single frame (with one PTS) that the system decodes to produce multiple images.

The system uses the multi-image callback when the video decoder outputs [`CMTaggedBufferGroupRef`](../CoreMedia/cmtaggedbuffergroupref.md) objects, or when frame decoding fails and returns a nonzero status. The original single-image callback is only used in the case where the video decoder outputs a [`CVImageBuffer`](../CoreVideo/cvimagebuffer.md) instead of a [`CMTaggedBufferGroupRef`](../CoreMedia/cmtaggedbuffergroupref.md).

## Parameters

- `decompressionSession`: The decompression session.
- `outputMultiImageCallback`: A callback to handle multi-image output.
- `outputMultiImageRefcon`: Your reference value for the session.

## Topics

### Output Callback
- [typealias VTDecompressionOutputMultiImageCallback](./vtdecompressionoutputmultiimagecallback.md)
  A callback that the system invokes when multi-image frame decompression completes.

## See Also

### Decoding Multi-Image Frames
- [func VTIsStereoMVHEVCDecodeSupported() -> Bool](./vtisstereomvhevcdecodesupported%28%29.md)
  Returns a Boolean value that indicates whether the system supports MV-HEVC decoding.
- [VTDecompressionSessionDecodeFrameWithMultiImageCapableOutputHandler](./vtdecompressionsessiondecodeframewithmultiimagecapableoutputhandler.md)
  Decompresses a multi-image frame and calls the specified output handler upon completion.
- [typealias VTDecompressionMultiImageCapableOutputHandler](./vtdecompressionmultiimagecapableoutputhandler.md)
  A type alias for callback that the system invokes when it finishes decompressing a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsessionsetmultiimagecallback)*