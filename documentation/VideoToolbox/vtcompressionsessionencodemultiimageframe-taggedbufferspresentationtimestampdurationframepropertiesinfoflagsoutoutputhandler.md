# VTCompressionSessionEncodeMultiImageFrame(_:taggedBuffers:presentationTimeStamp:duration:frameProperties:infoFlagsOut:outputHandler:)

**Framework**: Video Toolbox  
**Kind**: func

Passes a multi-image frame to a compression session for encoding and provides a callback to handle the output.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func VTCompressionSessionEncodeMultiImageFrame(_ session: VTCompressionSession, taggedBuffers: [CMTaggedBuffer], presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, outputHandler: @escaping VTCompressionOutputHandler) -> OSStatus
```

#### Return Value

An `OSStatus` value that indicates the result of the operation.

#### Discussion

The system doesn’t guarantee that encoded frames be output before the function returns. The session and encoder retain the image buffer as long as necessary.

You can’t call this function on a session created with a [`VTCompressionOutputCallback`](vtcompressionoutputcallback.md).

> ❗ **Important**:  Don’t modify the pixel data after making this call.

## Parameters

- `session`: The compression session.
- `taggedBuffers`: An array of [`CMTaggedBuffer`](https://developer.apple.com/documentation/CoreMedia/CMTaggedBuffer) structures that contains the multiple images for a video frame to compress.
- `presentationTimeStamp`: The presentation timestamp for this frame to attach to the sample buffer. Each presentation timestamp that you pass to a session must be greater than the previous one.
- `duration`: The presentation duration for this frame to attach to the sample buffer. Pass a value of [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTime/invalid) if you don’t have duration information.
- `frameProperties`: A dictionary that specifies additional properties for encoding this frame. Some session properties may also change between frames, which affect subsequently encoded frames.
- `infoFlagsOut`: Points to a [`VTEncodeInfoFlags`](vtencodeinfoflags.md) value to receive information about the encode operation. The system sets the [`asynchronous`](vtencodeinfoflags/asynchronous.md) flag if the encode runs asynchronously. The system sets the [`frameDropped`](vtencodeinfoflags/framedropped.md) flag if the encoding process dropped a frame (synchronously). Pass `NULL` if you don’t want to receive this information.
- `outputHandler`: A callback the system invokes when it completes encoding a frame. The system may invoke this callback asynchronously, on a different thread from the one that calls [`VTCompressionSessionEncodeMultiImageFrame(_:taggedBuffers:presentationTimeStamp:duration:frameProperties:infoFlagsOut:outputHandler:)`](vtcompressionsessionencodemultiimageframe(_:taggedbuffers:presentationtimestamp:duration:frameproperties:infoflagsout:outputhandler:).md).

## See Also

- [func VTIsStereoMVHEVCEncodeSupported() -> Bool](vtisstereomvhevcencodesupported().md)
  Returns a Boolean value that indicates whether the system supports MV-HEVC encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessionencodemultiimageframe(_:taggedbuffers:presentationtimestamp:duration:frameproperties:infoflagsout:outputhandler:))*