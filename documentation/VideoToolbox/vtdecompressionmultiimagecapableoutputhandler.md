# VTDecompressionMultiImageCapableOutputHandler

**Framework**: Video Toolbox  
**Kind**: typealias

A type alias for callback that the system invokes when it finishes decompressing a frame.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias VTDecompressionMultiImageCapableOutputHandler = @Sendable (OSStatus, VTDecodeInfoFlags, CVImageBuffer?, __CMTaggedBufferGroup?, CMTime, CMTime) -> Void
```

#### Discussion

Pass a callback of this type to [`VTDecompressionSessionDecodeFrameWithMultiImageCapableOutputHandler`](vtdecompressionsessiondecodeframewithmultiimagecapableoutputhandler.md) to handle the decompressed frame output. The system doesn’t necessarily invoke the callback in display order. If the multi-image decompression call returns an error, the system doesn’t call this block.

> ❗ **Important**:  The video decompressor may still reference the pixel buffers that this callback provides if the [`imageBufferModifiable`](vtdecodeinfoflags/imagebuffermodifiable.md) flag isn’t set. It’s not safe to modify the returned pixel buffers in this state.

## Parameters

- `status`: A value of `noErr` if decompression succeeds; otherwise, an error code if decompression fails.
- `infoFlags`: A [`VTEncodeInfoFlags`](vtencodeinfoflags.md) pointer to receive information about the decode operation. The [`asynchronous`](vtdecodeinfoflags/asynchronous.md) bit may be set if the decode is (or was) running asynchronously. The [`frameDropped`](vtdecodeinfoflags/framedropped.md) bit may be set if the frame was dropped (synchronously). Pass `NULL` if you don’t want to receive this information.
- `imageBuffer`: The decompressed pixel buffer.
- `taggedBufferGroup`: A [`CMTaggedBufferGroupRef`](https://developer.apple.com/documentation/coremedia/cmtaggedbuffergroupref) that contains the multiple images for the decompressed frame, if the decompression succeeds; otherwise, `NULL`.
- `presentationTimeStamp`: The frame’s presentation timestamp; otherwise, [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/invalid) if the value isn’t available.
- `presentationDuration`: The frame’s presentation duration; otherwise, [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/invalid) if the value isn’t available.

## See Also

- [func VTIsStereoMVHEVCDecodeSupported() -> Bool](vtisstereomvhevcdecodesupported().md)
  Returns a Boolean value that indicates whether the system supports MV-HEVC decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionmultiimagecapableoutputhandler)*