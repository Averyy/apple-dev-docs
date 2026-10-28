# VTCompressionSessionEncodeMultiImageFrame

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Passes a multi-image frame to a compression session for encoding.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```c
extern OSStatus VTCompressionSessionEncodeMultiImageFrame(VTCompressionSessionRef session, CMTaggedBufferGroupRef taggedBufferGroup, CMTime presentationTimeStamp, CMTime duration, CFDictionaryRef frameProperties, void *sourceFrameRefcon, VTEncodeInfoFlags *infoFlagsOut);
```

## Return Value

An `OSStatus` value that indicates the result of the operation.

## Discussion

The system doesn’t guarantee that encoded frames be output before the function returns. The session and encoder retain the image buffer as long as necessary.

> ❗ **Important**:  Don’t modify the pixel data after making this call.

## Parameters

- `session`: The compression session.
- `taggedBufferGroup`: A [`CMTaggedBufferGroupRef`](../CoreMedia/cmtaggedbuffergroupref.md) that contains the multiple images for a video frame to compress.
- `presentationTimeStamp`: The presentation timestamp for this frame to attach to the sample buffer. Each presentation timestamp that you pass to a session must be greater than the previous one.
- `duration`: The presentation duration for this frame to attach to the sample buffer. If you don’t have duration information, pass [`invalid`](../CoreMedia/cmtime/invalid.md).
- `frameProperties`: A dictionary that specifies additional properties for encoding this frame. Some session properties may also change between frames, which affect subsequently encoded frames.
- `sourceFrameRefcon`: Your reference value for the frame, which the system passes to the output callback function.
- `infoFlagsOut`: Points to a [`VTEncodeInfoFlags`](./vtencodeinfoflags.md) value to receive information about the encode operation.

  The system sets the [`asynchronous`](./vtencodeinfoflags/asynchronous.md) flag if the encode runs asynchronously.

  The system sets the [`frameDropped`](./vtencodeinfoflags/framedropped.md) flag if the encoding process dropped a frame (synchronously).

  Pass `NULL` if you don’t want to receive this information.

## See Also

### Encoding Multi-Image Frames
- [func VTIsStereoMVHEVCEncodeSupported() -> Bool](./vtisstereomvhevcencodesupported%28%29.md)
  Returns a Boolean value that indicates whether the system supports MV-HEVC encoding.
- [VTCompressionSessionEncodeMultiImageFrameWithOutputHandler](./vtcompressionsessionencodemultiimageframewithoutputhandler.md)
  Passes a multi-image frame to a compression session for encoding and provides a callback to handle the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessionencodemultiimageframe)*