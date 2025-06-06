# VTCompressionSessionCompleteFrames(_:untilPresentationTimeStamp:)

**Framework**: Videotoolbox  
**Kind**: func

Forces the compression session to complete the encoding of frames.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTCompressionSessionCompleteFrames(_ session: VTCompressionSession, untilPresentationTimeStamp completeUntilPresentationTimeStamp: CMTime) -> OSStatus
```

#### Discussion

If `completeUntilPresentationTimeStamp` is numeric, frames with presentation timestamps up to and including this timestamp are emitted before the function returns.

If `completeUntilPresentationTimeStamp` is non-numeric, all pending frames are emitted before the function returns.

## Parameters

- `session`: The compression session.
- `completeUntilPresentationTimeStamp`: The timestamp at which to complete frame encoding.

## See Also

- [func VTCompressionSessionGetPixelBufferPool(VTCompressionSession) -> CVPixelBufferPool?](vtcompressionsessiongetpixelbufferpool(_:).md)
  Returns a pool that provides ideal source pixel buffers for a compression session.
- [func VTCompressionSessionPrepareToEncodeFrames(VTCompressionSession) -> OSStatus](vtcompressionsessionpreparetoencodeframes(_:).md)
  Enables the encoder to perform any necessary resource allocation before the encoder begins encoding frames (optional).
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, sourceFrameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?) -> OSStatus](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:sourceframerefcon:infoflagsout:).md)
  Presents frames to the compression session.
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, outputHandler: VTCompressionOutputHandler) -> OSStatus](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:infoflagsout:outputhandler:).md)
  Presents frames to the compression session and invokes the output callback when compression is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessioncompleteframes(_:untilpresentationtimestamp:))*