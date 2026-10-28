# VTCompressionSession

**Framework**: Video Toolbox  
**Role**: API Collection

An object that compresses video data.

## Overview

A compression session supports the compression of a sequence of video frames. Here’s the workflow:

1. Create a compression session using [`VTCompressionSessionCreate(allocator:width:height:codecType:encoderSpecification:imageBufferAttributes:compressedDataAllocator:outputCallback:refcon:compressionSessionOut:)`](./vtcompressionsessioncreate%28allocator,width,height,codectype,encoderspecification,imagebufferattributes,compresseddataallocator,outputcallback,refcon,compressionsessionout%29.md).
2. Optionally, configure the session with your desired [Compression Properties](./compression-properties.md) by calling [`VTSessionSetProperty(_:key:value:)`](./vtsessionsetproperty%28_,key,value%29.md) or [`VTSessionSetProperties(_:propertyDictionary:)`](./vtsessionsetproperties%28_,propertydictionary%29.md).
3. Encode video frames using [`VTCompressionSessionEncodeFrame(_:imageBuffer:presentationTimeStamp:duration:frameProperties:sourceFrameRefcon:infoFlagsOut:)`](./vtcompressionsessionencodeframe%28_,imagebuffer,presentationtimestamp,duration,frameproperties,sourceframerefcon,infoflagsout%29.md) and receive the compressed video frames in the session’s [`VTCompressionOutputCallback`](./vtcompressionoutputcallback.md).
4. To force the completion of some or all pending frames, call [`VTCompressionSessionCompleteFrames(_:untilPresentationTimeStamp:)`](./vtcompressionsessioncompleteframes%28_,untilpresentationtimestamp%29.md).
5. When you finish with the compression session, call [`VTCompressionSessionInvalidate(_:)`](./vtcompressionsessioninvalidate%28_%29.md) to invalidate it and [`CFRelease`](../CoreFoundation/cfrelease.md) to free its memory.

## Topics

### Creating a Session
- [func VTCompressionSessionCreate(allocator: CFAllocator?, width: Int32, height: Int32, codecType: CMVideoCodecType, encoderSpecification: CFDictionary?, imageBufferAttributes: CFDictionary?, compressedDataAllocator: CFAllocator?, outputCallback: VTCompressionOutputCallback?, refcon: UnsafeMutableRawPointer?, compressionSessionOut: UnsafeMutablePointer<VTCompressionSession?>) -> OSStatus](./vtcompressionsessioncreate%28allocator,width,height,codectype,encoderspecification,imagebufferattributes,compresseddataallocator,outputcallback,refcon,compressionsessionout%29.md)
  Creates an object that compresses video frames.
### Configuring a Session
- [Compression Properties](./compression-properties.md)
  Properties that you use to configure a compression session.
### Encoding Frames
- [func VTCompressionSessionGetPixelBufferPool(VTCompressionSession) -> CVPixelBufferPool?](./vtcompressionsessiongetpixelbufferpool%28_%29.md)
  Returns a pool that provides ideal source pixel buffers for a compression session.
- [func VTCompressionSessionPrepareToEncodeFrames(VTCompressionSession) -> OSStatus](./vtcompressionsessionpreparetoencodeframes%28_%29.md)
  Enables the encoder to perform any necessary resource allocation before the encoder begins encoding frames (optional).
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, sourceFrameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?) -> OSStatus](./vtcompressionsessionencodeframe%28_,imagebuffer,presentationtimestamp,duration,frameproperties,sourceframerefcon,infoflagsout%29.md)
  Presents frames to the compression session.
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, outputHandler: VTCompressionOutputHandler) -> OSStatus](./vtcompressionsessionencodeframe%28_,imagebuffer,presentationtimestamp,duration,frameproperties,infoflagsout,outputhandler%29.md)
  Presents frames to the compression session and invokes the output callback when compression is complete.
- [func VTCompressionSessionCompleteFrames(VTCompressionSession, untilPresentationTimeStamp: CMTime) -> OSStatus](./vtcompressionsessioncompleteframes%28_,untilpresentationtimestamp%29.md)
  Forces the compression session to complete the encoding of frames.
### Encoding Multi-Image Frames
- [func VTIsStereoMVHEVCEncodeSupported() -> Bool](./vtisstereomvhevcencodesupported%28%29.md)
  Returns a Boolean value that indicates whether the system supports MV-HEVC encoding.
- [func VTCompressionSessionEncodeMultiImageFrame(VTCompressionSession, taggedBuffers: [CMTaggedBuffer], presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, outputHandler: VTCompressionOutputHandler) -> OSStatus](./vtcompressionsessionencodemultiimageframe%28_,taggedbuffers,presentationtimestamp,duration,frameproperties,infoflagsout,outputhandler%29.md)
  Passes a multi-image frame to a compression session for encoding and provides a callback to handle the output.
- [VTCompressionSessionEncodeMultiImageFrame](./vtcompressionsessionencodemultiimageframe.md)
  Passes a multi-image frame to a compression session for encoding.
- [VTCompressionSessionEncodeMultiImageFrameWithOutputHandler](./vtcompressionsessionencodemultiimageframewithoutputhandler.md)
  Passes a multi-image frame to a compression session for encoding and provides a callback to handle the output.
### Performing Multiple Passes
- [func VTCompressionSessionBeginPass(VTCompressionSession, flags: VTCompressionSessionOptionFlags, UnsafeMutablePointer<UInt32>?) -> OSStatus](./vtcompressionsessionbeginpass%28_,flags,_%29.md)
  Marks the start of a specific compression pass.
- [func VTCompressionSessionEndPass(VTCompressionSession, furtherPassesRequestedOut: UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](./vtcompressionsessionendpass%28_,furtherpassesrequestedout,_%29.md)
  Marks the end of a compression pass.
- [func VTCompressionSessionGetTimeRangesForNextPass(VTCompressionSession, timeRangeCountOut: UnsafeMutablePointer<CMItemCount>, timeRangeArrayOut: UnsafeMutablePointer<UnsafePointer<CMTimeRange>?>) -> OSStatus](./vtcompressionsessiongettimerangesfornextpass%28_,timerangecountout,timerangearrayout%29.md)
  Retrieves the time ranges for the next pass.
### Invalidating a Session
- [func VTCompressionSessionInvalidate(VTCompressionSession)](./vtcompressionsessioninvalidate%28_%29.md)
  Tears down a compression session.
### Accessing the Type Identifier
- [func VTCompressionSessionGetTypeID() -> CFTypeID](./vtcompressionsessiongettypeid%28%29.md)
  Retrieves the Core Foundation type identifier for the compression session.
### Data Types
- [class VTCompressionSession](./vtcompressionsession.md)
  A reference to a VideoToolbox compression session.
- [struct VTEncodeInfoFlags](./vtencodeinfoflags.md)
  Flags that indicate encoder state.

## See Also

### Compression
- [Encoding video for low-latency conferencing](./encoding-video-for-low-latency-conferencing.md)
  Configure a compression session to optimize encoding for video-conferencing apps.
- [Encoding video for live streaming](./encoding-video-for-live-streaming.md)
  Configure a compression session to encode video for live streaming.
- [Encoding video for offline transcoding](./encoding-video-for-offline-transcoding.md)
  Configure a compression session to transcode video in offline workflows.
- [VTDecompressionSession](./vtdecompressionsession-api-collection.md)
  An object that decompresses video data.
- [VTFrameSilo](./vtframesilo-api-collection.md)
  An object that stores sample buffers from a multipass encoding session.
- [VTMultiPassStorage](./vtmultipassstorage-api-collection.md)
  An object that stores video encoding metadata from a multipass encoding session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsession-api-collection)*