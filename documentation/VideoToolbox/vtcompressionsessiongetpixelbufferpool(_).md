# VTCompressionSessionGetPixelBufferPool(_:)

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Returns a pool that provides ideal source pixel buffers for a compression session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTCompressionSessionGetPixelBufferPool(_ session: VTCompressionSession) -> CVPixelBufferPool?
```

```c
extern CVPixelBufferPoolRefVTCompressionSessionGetPixelBufferPool(VTCompressionSessionRef session);
```

#### Return Value

A configured pixel buffer pool.

#### Discussion

The compression session creates this pixel buffer pool based on the compressor’s pixel buffer attributes and any pixel buffer attributes passed in to [`VTCompressionSessionCreate(allocator:width:height:codecType:encoderSpecification:imageBufferAttributes:compressedDataAllocator:outputCallback:refcon:compressionSessionOut:)`](./vtcompressionsessioncreate%28allocator,width,height,codectype,encoderspecification,imagebufferattributes,compresseddataallocator,outputcallback,refcon,compressionsessionout%29.md).  If the source pixel buffer attributes and the compressor pixel buffer attributes cannot be reconciled, the pool is based on the source pixel buffer attributes, and VideoToolbox converts each [`CVImageBuffer`](../CoreVideo/cvimagebuffer.md) internally.

> **Note**:  Clients can call this function once and retain the resulting pool, but the call is cheap enough that it’s ok to call it once per frame.  If a change of session properties causes the compressor’s pixel buffer attributes to change, it’s possible that this function might return a different pool.

## Parameters

- `session`: The compression session.

## See Also

### Encoding Frames
- [func VTCompressionSessionPrepareToEncodeFrames(VTCompressionSession) -> OSStatus](./vtcompressionsessionpreparetoencodeframes%28_%29.md)
  Enables the encoder to perform any necessary resource allocation before the encoder begins encoding frames (optional).
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, sourceFrameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?) -> OSStatus](./vtcompressionsessionencodeframe%28_,imagebuffer,presentationtimestamp,duration,frameproperties,sourceframerefcon,infoflagsout%29.md)
  Presents frames to the compression session.
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, outputHandler: VTCompressionOutputHandler) -> OSStatus](./vtcompressionsessionencodeframe%28_,imagebuffer,presentationtimestamp,duration,frameproperties,infoflagsout,outputhandler%29.md)
  Presents frames to the compression session and invokes the output callback when compression is complete.
- [func VTCompressionSessionCompleteFrames(VTCompressionSession, untilPresentationTimeStamp: CMTime) -> OSStatus](./vtcompressionsessioncompleteframes%28_,untilpresentationtimestamp%29.md)
  Forces the compression session to complete the encoding of frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessiongetpixelbufferpool(_:))*