# VTDecompressionSession

**Framework**: Video Toolbox  
**Role**: API Collection

An object that decompresses video data.

## Overview

A decompression session supports the decompression of a sequence of video frames. Here’s the basic workflow:

1. Create a decompression session by calling [`VTDecompressionSessionCreate(allocator:formatDescription:decoderSpecification:imageBufferAttributes:outputCallback:decompressionSessionOut:)`](./vtdecompressionsessioncreate%28allocator,formatdescription,decoderspecification,imagebufferattributes,outputcallback,decompressionsessionout%29.md).
2. Optionally, configure the session with your desired [Decompression Properties](./decompression-properties.md) by calling [`VTSessionSetProperty(_:key:value:)`](./vtsessionsetproperty%28_,key,value%29.md) or [`VTSessionSetProperties(_:propertyDictionary:)`](./vtsessionsetproperties%28_,propertydictionary%29.md).
3. Decode video frames using [`VTDecompressionSessionDecodeFrame(_:sampleBuffer:flags:frameRefcon:infoFlagsOut:)`](./vtdecompressionsessiondecodeframe%28_,samplebuffer,flags,framerefcon,infoflagsout%29.md).
4. When you finish with the decompression session, call [`VTDecompressionSessionInvalidate(_:)`](./vtdecompressionsessioninvalidate%28_%29.md) to tear it down, and call [`CFRelease`](../CoreFoundation/cfrelease.md) to free its memory.

## Topics

### Creating a Session
- [func VTDecompressionSessionCreate(allocator: CFAllocator?, formatDescription: CMVideoFormatDescription, decoderSpecification: CFDictionary?, imageBufferAttributes: CFDictionary?, decompressionSessionOut: UnsafeMutablePointer<VTDecompressionSession?>) -> OSStatus](./vtdecompressionsessioncreate%28allocator,formatdescription,decoderspecification,imagebufferattributes,decompressionsessionout%29.md)
- [func VTDecompressionSessionCreate(allocator: CFAllocator?, formatDescription: CMVideoFormatDescription, decoderSpecification: CFDictionary?, imageBufferAttributes: CFDictionary?, outputCallback: UnsafePointer<VTDecompressionOutputCallbackRecord>?, decompressionSessionOut: UnsafeMutablePointer<VTDecompressionSession?>) -> OSStatus](./vtdecompressionsessioncreate%28allocator,formatdescription,decoderspecification,imagebufferattributes,outputcallback,decompressionsessionout%29.md)
  Creates a session for decompressing video frames.
### Configuring a Session
- [Decompression Properties](./decompression-properties.md)
  Properties used to configure a VideoToolbox decompression session.
- [func VTVideoDecoderExtensionProperties(CMFormatDescription) throws -> [VTExtensionPropertiesKey : Any]](./vtvideodecoderextensionproperties%28_%29.md)
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
- [func VTDecompressionSessionWaitForAsynchronousFrames(VTDecompressionSession) -> OSStatus](./vtdecompressionsessionwaitforasynchronousframes%28_%29.md)
  Waits for any and all outstanding asynchronous and delayed frames to complete, then returns.
- [func VTDecompressionSessionCopyBlackPixelBuffer(VTDecompressionSession, pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> OSStatus](./vtdecompressionsessioncopyblackpixelbuffer%28_,pixelbufferout%29.md)
  Copies a black pixel buffer from the decompression session.
### Decoding Multi-Image Frames
- [func VTIsStereoMVHEVCDecodeSupported() -> Bool](./vtisstereomvhevcdecodesupported%28%29.md)
  Returns a Boolean value that indicates whether the system supports MV-HEVC decoding.
- [typealias VTDecompressionMultiImageCapableOutputHandler](./vtdecompressionmultiimagecapableoutputhandler.md)
  A type alias for callback that the system invokes when it finishes decompressing a frame.
- [VTDecompressionSessionSetMultiImageCallback](./vtdecompressionsessionsetmultiimagecallback.md)
  Provides a callback capable of receiving multiple images for individual frame decoding requests.
- [VTDecompressionSessionDecodeFrameWithMultiImageCapableOutputHandler](./vtdecompressionsessiondecodeframewithmultiimagecapableoutputhandler.md)
  Decompresses a multi-image frame and calls the specified output handler upon completion.
### Invalidating a Session
- [func VTDecompressionSessionInvalidate(VTDecompressionSession)](./vtdecompressionsessioninvalidate%28_%29.md)
  Tears down a decompression session.
### Accessing the Type Identifier
- [func VTDecompressionSessionGetTypeID() -> CFTypeID](./vtdecompressionsessiongettypeid%28%29.md)
  Returns the Core Foundation type identifier for the decompression session.
### Data Types
- [class VTDecompressionSession](./vtdecompressionsession.md)
  A reference to a decompression session.
- [struct VTDecodeFrameFlags](./vtdecodeframeflags.md)
  Flags to pass to a decompression session and the video decoder.
- [struct VTDecodeInfoFlags](./vtdecodeinfoflags.md)
  Flags that provide information about the status of a decode operation.
- [typealias VTDecompressionOutputCallback](./vtdecompressionoutputcallback.md)
  The prototype for the callback invoked when frame decompression is complete.
- [struct VTDecompressionOutputCallbackRecord](./vtdecompressionoutputcallbackrecord.md)
- [typealias VTDecompressionOutputHandler](./vtdecompressionoutputhandler.md)
  The prototype for the block invoked when frame decompression is complete.

## See Also

### Compression
- [Encoding video for low-latency conferencing](./encoding-video-for-low-latency-conferencing.md)
  Configure a compression session to optimize encoding for video-conferencing apps.
- [Encoding video for live streaming](./encoding-video-for-live-streaming.md)
  Configure a compression session to encode video for live streaming.
- [Encoding video for offline transcoding](./encoding-video-for-offline-transcoding.md)
  Configure a compression session to transcode video in offline workflows.
- [VTCompressionSession](./vtcompressionsession-api-collection.md)
  An object that compresses video data.
- [VTFrameSilo](./vtframesilo-api-collection.md)
  An object that stores sample buffers from a multipass encoding session.
- [VTMultiPassStorage](./vtmultipassstorage-api-collection.md)
  An object that stores video encoding metadata from a multipass encoding session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsession-api-collection)*