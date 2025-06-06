# VTCompressionSessionGetPixelBufferPool(_:)

**Framework**: Videotoolbox  
**Kind**: func

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

#### Return Value

A configured pixel buffer pool.

#### Discussion

The compression session creates this pixel buffer pool based on the compressor’s pixel buffer attributes and any pixel buffer attributes passed in to [`VTCompressionSessionCreate(allocator:width:height:codecType:encoderSpecification:imageBufferAttributes:compressedDataAllocator:outputCallback:refcon:compressionSessionOut:)`](vtcompressionsessioncreate(allocator:width:height:codectype:encoderspecification:imagebufferattributes:compresseddataallocator:outputcallback:refcon:compressionsessionout:).md).  If the source pixel buffer attributes and the compressor pixel buffer attributes cannot be reconciled, the pool is based on the source pixel buffer attributes, and VideoToolbox converts each [`CVImageBuffer`](https://developer.apple.com/documentation/CoreVideo/CVImageBuffer) internally.

> **Note**:  Clients can call this function once and retain the resulting pool, but the call is cheap enough that it’s ok to call it once per frame.  If a change of session properties causes the compressor’s pixel buffer attributes to change, it’s possible that this function might return a different pool.

## Parameters

- `session`: The compression session.

## See Also

- [func VTCompressionSessionPrepareToEncodeFrames(VTCompressionSession) -> OSStatus](vtcompressionsessionpreparetoencodeframes(_:).md)
  Enables the encoder to perform any necessary resource allocation before the encoder begins encoding frames (optional).
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, sourceFrameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?) -> OSStatus](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:sourceframerefcon:infoflagsout:).md)
  Presents frames to the compression session.
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, outputHandler: VTCompressionOutputHandler) -> OSStatus](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:infoflagsout:outputhandler:).md)
  Presents frames to the compression session and invokes the output callback when compression is complete.
- [func VTCompressionSessionCompleteFrames(VTCompressionSession, untilPresentationTimeStamp: CMTime) -> OSStatus](vtcompressionsessioncompleteframes(_:untilpresentationtimestamp:).md)
  Forces the compression session to complete the encoding of frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessiongetpixelbufferpool(_:))*