# VTIsStereoMVHEVCEncodeSupported()

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the system supports MV-HEVC encoding.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func VTIsStereoMVHEVCEncodeSupported() -> Bool
```

```c
extern Boolean VTIsStereoMVHEVCEncodeSupported();
```

## Return Value

[`true`](../Swift/true.md) if the system supports MV-HEVC encoding; otherwise, [`false`](../Swift/false.md).

## Discussion

A return value of [`true`](../Swift/true.md) doesn’t guarantee that encoding resources are available at all times.

## See Also

### Encoding Multi-Image Frames
- [func VTCompressionSessionEncodeMultiImageFrame(VTCompressionSession, taggedBuffers: [CMTaggedBuffer], presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, outputHandler: VTCompressionOutputHandler) -> OSStatus](./vtcompressionsessionencodemultiimageframe%28_,taggedbuffers,presentationtimestamp,duration,frameproperties,infoflagsout,outputhandler%29.md)
  Passes a multi-image frame to a compression session for encoding and provides a callback to handle the output.
- [VTCompressionSessionEncodeMultiImageFrame](./vtcompressionsessionencodemultiimageframe.md)
  Passes a multi-image frame to a compression session for encoding.
- [VTCompressionSessionEncodeMultiImageFrameWithOutputHandler](./vtcompressionsessionencodemultiimageframewithoutputhandler.md)
  Passes a multi-image frame to a compression session for encoding and provides a callback to handle the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtisstereomvhevcencodesupported())*