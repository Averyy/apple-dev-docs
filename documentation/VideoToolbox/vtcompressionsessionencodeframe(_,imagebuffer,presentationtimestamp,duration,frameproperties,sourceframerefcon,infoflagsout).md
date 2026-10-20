# VTCompressionSessionEncodeFrame(_:imageBuffer:presentationTimeStamp:duration:frameProperties:sourceFrameRefcon:infoFlagsOut:)

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Presents frames to the compression session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTCompressionSessionEncodeFrame(_ session: VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, sourceFrameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?) -> OSStatus
```

```c
extern OSStatus VTCompressionSessionEncodeFrame(VTCompressionSessionRef session, CVImageBufferRef imageBuffer, CMTime presentationTimeStamp, CMTime duration, CFDictionaryRef frameProperties, void *sourceFrameRefcon, VTEncodeInfoFlags *infoFlagsOut);
```

#### Discussion

Encoded frames may or may not be output before the function returns. The client should not modify the pixel data after making this call. The session and/or encoder retains the image buffer as long as necessary.

## Parameters

- `session`: The compression session.
- `imageBuffer`: A Core Video image buffer ([`CVImageBuffer`](../CoreVideo/cvimagebuffer.md)) containing a video frame to be compressed. The buffer must have a nonzero reference count.
- `presentationTimeStamp`: The presentation timestamp for this frame, to be attached to the sample buffer. Each presentation timestamp passed to a session must be greater than the previous one.
- `duration`: The presentation duration for this frame, to be attached to the sample buffer. If you do not have duration information, pass [`invalid`](../CoreMedia/cmtime/invalid.md).
- `frameProperties`: Key/value pairs specifying additional properties for encoding this frame. Note that some session properties may also be changed between frames. Such changes affect subsequently encoded frames.
- `sourceFrameRefcon`: Your reference value for the frame, which will be passed to the output callback function.
- `infoFlagsOut`: A pointer to a `VTEncodeInfoFlags` to receive information about the encode operation.

  The [`asynchronous`](./vtencodeinfoflags/asynchronous.md) bit may be set if the encode is (or was) running asynchronously.

  The [`frameDropped`](./vtencodeinfoflags/framedropped.md) bit may be set if the frame was dropped (synchronously).

  Pass `NULL` if you do not want to receive this information.

## See Also

### Encoding Frames
- [func VTCompressionSessionGetPixelBufferPool(VTCompressionSession) -> CVPixelBufferPool?](./vtcompressionsessiongetpixelbufferpool%28_%29.md)
  Returns a pool that provides ideal source pixel buffers for a compression session.
- [func VTCompressionSessionPrepareToEncodeFrames(VTCompressionSession) -> OSStatus](./vtcompressionsessionpreparetoencodeframes%28_%29.md)
  Enables the encoder to perform any necessary resource allocation before the encoder begins encoding frames (optional).
- [func VTCompressionSessionEncodeFrame(VTCompressionSession, imageBuffer: CVImageBuffer, presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, outputHandler: VTCompressionOutputHandler) -> OSStatus](./vtcompressionsessionencodeframe%28_,imagebuffer,presentationtimestamp,duration,frameproperties,infoflagsout,outputhandler%29.md)
  Presents frames to the compression session and invokes the output callback when compression is complete.
- [func VTCompressionSessionCompleteFrames(VTCompressionSession, untilPresentationTimeStamp: CMTime) -> OSStatus](./vtcompressionsessioncompleteframes%28_,untilpresentationtimestamp%29.md)
  Forces the compression session to complete the encoding of frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:sourceframerefcon:infoflagsout:))*