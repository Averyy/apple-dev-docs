# VTCompressionSession

**Framework**: Video Toolbox

An object that compresses video data.

#### Overview

A compression session supports the compression of a sequence of video frames. Here’s the workflow:

1. Create a compression session using [`VTCompressionSessionCreate(allocator:width:height:codecType:encoderSpecification:imageBufferAttributes:compressedDataAllocator:outputCallback:refcon:compressionSessionOut:)`](vtcompressionsessioncreate(allocator:width:height:codectype:encoderspecification:imagebufferattributes:compresseddataallocator:outputcallback:refcon:compressionsessionout:).md).
2. Optionally, configure the session with your desired [`Compression Properties`](compression-properties.md) by calling [`VTSessionSetProperty(_:key:value:)`](vtsessionsetproperty(_:key:value:).md) or [`VTSessionSetProperties(_:propertyDictionary:)`](vtsessionsetproperties(_:propertydictionary:).md).
3. Encode video frames using [`VTCompressionSessionEncodeFrame(_:imageBuffer:presentationTimeStamp:duration:frameProperties:sourceFrameRefcon:infoFlagsOut:)`](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:sourceframerefcon:infoflagsout:).md) and receive the compressed video frames in the session’s [`VTCompressionOutputCallback`](vtcompressionoutputcallback.md).
4. To force the completion of some or all pending frames, call [`VTCompressionSessionCompleteFrames(_:untilPresentationTimeStamp:)`](vtcompressionsessioncompleteframes(_:untilpresentationtimestamp:).md).
5. When you finish with the compression session, call [`VTCompressionSessionInvalidate(_:)`](vtcompressionsessioninvalidate(_:).md) to invalidate it and [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) to free its memory.

## Topics

### Creating a Session
- [func VTCompressionSessionCreate(allocator: CFAllocator?, width: Int32, height: Int32, codecType: CMVideoCodecType, encoderSpecification: CFDictionary?, imageBufferAttributes: CFDictionary?, compressedDataAllocator: CFAllocator?, outputCallback: VTCompressionOutputCallback?, refcon: UnsafeMutableRawPointer?, compressionSessionOut: UnsafeMutablePointer<VTCompressionSession?>) -> OSStatus](vtcompressionsessioncreate(allocator:width:height:codectype:encoderspecification:imagebufferattributes:compresseddataallocator:outputcallback:refcon:compressionsessionout:).md)
  Creates an object that compresses video frames.
### Configuring a Session
- [Compression Properties](compression-properties.md)
  Properties that you use to configure a compression session.
### Encoding Frames
- [func VTCompressionSessionGetPixelBufferPool(VTCompressionSession) -> CVPixelBufferPool?](vtcompressionsessiongetpixelbufferpool(_:).md)
  Returns a pool that provides ideal source pixel buffers for a compression session.
- [func VTCompressionSessionPrepareToEncodeFrames(VTCompressionSession) -> OSStatus](vtcompressionsessionpreparetoencodeframes(_:).md)
  Enables the encoder to perform any necessary resource allocation before the encoder begins encoding frames (optional).
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, sourceFrameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?) -> OSStatus](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:sourceframerefcon:infoflagsout:).md)
  Presents frames to the compression session.
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, outputHandler: VTCompressionOutputHandler) -> OSStatus](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:infoflagsout:outputhandler:).md)
  Presents frames to the compression session and invokes the output callback when compression is complete.
- [func VTCompressionSessionCompleteFrames(VTCompressionSession, untilPresentationTimeStamp: CMTime) -> OSStatus](vtcompressionsessioncompleteframes(_:untilpresentationtimestamp:).md)
  Forces the compression session to complete the encoding of frames.
### Encoding Multi-Image Frames
- [func VTIsStereoMVHEVCEncodeSupported() -> Bool](vtisstereomvhevcencodesupported().md)
  Returns a Boolean value that indicates whether the system supports MV-HEVC encoding.
- [func VTCompressionSessionEncodeMultiImageFrame(VTCompressionSession, taggedBuffers: [CMTaggedBuffer], presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, outputHandler: VTCompressionOutputHandler) -> OSStatus](vtcompressionsessionencodemultiimageframe(_:taggedbuffers:presentationtimestamp:duration:frameproperties:infoflagsout:outputhandler:).md)
  Passes a multi-image frame to a compression session for encoding and provides a callback to handle the output.
### Performing Multiple Passes
- [func VTCompressionSessionBeginPass(VTCompressionSession, flags: VTCompressionSessionOptionFlags, UnsafeMutablePointer<UInt32>?) -> OSStatus](vtcompressionsessionbeginpass(_:flags:_:).md)
  Marks the start of a specific compression pass.
- [func VTCompressionSessionEndPass(VTCompressionSession, furtherPassesRequestedOut: UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](vtcompressionsessionendpass(_:furtherpassesrequestedout:_:).md)
  Marks the end of a compression pass.
- [func VTCompressionSessionGetTimeRangesForNextPass(VTCompressionSession, timeRangeCountOut: UnsafeMutablePointer<CMItemCount>, timeRangeArrayOut: UnsafeMutablePointer<UnsafePointer<CMTimeRange>?>) -> OSStatus](vtcompressionsessiongettimerangesfornextpass(_:timerangecountout:timerangearrayout:).md)
  Retrieves the time ranges for the next pass.
### Invalidating a Session
- [func VTCompressionSessionInvalidate(VTCompressionSession)](vtcompressionsessioninvalidate(_:).md)
  Tears down a compression session.
### Accessing the Type Identifier
- [func VTCompressionSessionGetTypeID() -> CFTypeID](vtcompressionsessiongettypeid().md)
  Retrieves the Core Foundation type identifier for the compression session.
### Data Types
- [class VTCompressionSession](vtcompressionsession.md)
  A reference to a VideoToolbox compression session.
- [struct VTEncodeInfoFlags](vtencodeinfoflags.md)
  Flags that indicate encoder state.

## See Also

- [Encoding video for low-latency conferencing](encoding-video-for-low-latency-conferencing.md)
  Configure a compression session to optimize encoding for video-conferencing apps.
- [Encoding video for live streaming](encoding-video-for-live-streaming.md)
  Configure a compression session to encode video for live streaming.
- [Encoding video for offline transcoding](encoding-video-for-offline-transcoding.md)
  Configure a compression session to transcode video in offline workflows.
- [VTDecompressionSession](vtdecompressionsession-api-collection.md)
  An object that decompresses video data.
- [VTFrameSilo](vtframesilo-api-collection.md)
  An object that stores sample buffers from a multipass encoding session.
- [VTMultiPassStorage](vtmultipassstorage-api-collection.md)
  An object that stores video encoding metadata from a multipass encoding session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsession-api-collection)*