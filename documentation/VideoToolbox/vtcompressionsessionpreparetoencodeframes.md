# VTCompressionSessionPrepareToEncodeFrames(_:)

**Framework**: Videotoolbox  
**Kind**: func

Enables the encoder to perform any necessary resource allocation before the encoder begins encoding frames (optional).

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTCompressionSessionPrepareToEncodeFrames(_ session: VTCompressionSession) -> OSStatus
```

#### Discussion

If this function isn’t called, any necessary resources are allocated on the first [`VTCompressionSessionEncodeFrame(_:imageBuffer:presentationTimeStamp:duration:frameProperties:sourceFrameRefcon:infoFlagsOut:)`](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:sourceframerefcon:infoflagsout:).md) call.

Subsequent calls to this function have no effect.

## Parameters

- `session`: The compression session.

## See Also

- [func VTCompressionSessionGetPixelBufferPool(VTCompressionSession) -> CVPixelBufferPool?](vtcompressionsessiongetpixelbufferpool(_:).md)
  Returns a pool that provides ideal source pixel buffers for a compression session.
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, sourceFrameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?) -> OSStatus](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:sourceframerefcon:infoflagsout:).md)
  Presents frames to the compression session.
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, outputHandler: VTCompressionOutputHandler) -> OSStatus](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:infoflagsout:outputhandler:).md)
  Presents frames to the compression session and invokes the output callback when compression is complete.
- [func VTCompressionSessionCompleteFrames(VTCompressionSession, untilPresentationTimeStamp: CMTime) -> OSStatus](vtcompressionsessioncompleteframes(_:untilpresentationtimestamp:).md)
  Forces the compression session to complete the encoding of frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessionpreparetoencodeframes(_:))*