# VTCompressionSessionPrepareToEncodeFrames(_:)

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus VTCompressionSessionPrepareToEncodeFrames(VTCompressionSessionRef session);
```

#### Discussion

If this function isn’t called, any necessary resources are allocated on the first [`VTCompressionSessionEncodeFrame(_:imageBuffer:presentationTimeStamp:duration:frameProperties:sourceFrameRefcon:infoFlagsOut:)`](./vtcompressionsessionencodeframe%28_,imagebuffer,presentationtimestamp,duration,frameproperties,sourceframerefcon,infoflagsout%29.md) call.

Subsequent calls to this function have no effect.

## Parameters

- `session`: The compression session.

## See Also

### Encoding Frames
- [func VTCompressionSessionGetPixelBufferPool(VTCompressionSession) -> CVPixelBufferPool?](./vtcompressionsessiongetpixelbufferpool%28_%29.md)
  Returns a pool that provides ideal source pixel buffers for a compression session.
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, sourceFrameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?) -> OSStatus](./vtcompressionsessionencodeframe%28_,imagebuffer,presentationtimestamp,duration,frameproperties,sourceframerefcon,infoflagsout%29.md)
  Presents frames to the compression session.
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, outputHandler: VTCompressionOutputHandler) -> OSStatus](./vtcompressionsessionencodeframe%28_,imagebuffer,presentationtimestamp,duration,frameproperties,infoflagsout,outputhandler%29.md)
  Presents frames to the compression session and invokes the output callback when compression is complete.
- [func VTCompressionSessionCompleteFrames(VTCompressionSession, untilPresentationTimeStamp: CMTime) -> OSStatus](./vtcompressionsessioncompleteframes%28_,untilpresentationtimestamp%29.md)
  Forces the compression session to complete the encoding of frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessionpreparetoencodeframes(_:))*