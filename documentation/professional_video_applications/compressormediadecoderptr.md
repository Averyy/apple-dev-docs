# CompressorMediaDecoderPtr

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

The type alias for referencing the decoder object.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
typealias CompressorMediaDecoderPtr = any NSObjectProtocol & CompressorMediaDecoder
```

```c
typedef NSObject<CompressorMediaDecoder> * CompressorMediaDecoderPtr;
```

## See Also

### Getting Decoded Frames and Samples
- [func copyAudio(atStart: Int64, count: UnsafeMutablePointer<Int64>!) -> Data!](./compressormediadecoder/copyaudio%28atstart,count%29.md)
  Returns decoded audio samples starting from the specified temporal position.
- [func copyCloseCaptionData(Int64, frameCount: Int64) -> [AnyHashable : Any]!](./compressormediadecoder/copyclosecaptiondata%28_,framecount%29.md)
  Returns a list of closed-caption tracks associated with the specified video frames.
- [func copyFrame(Int64) -> IOSurface!](./compressormediadecoder/copyframe%28_%29.md)
  Returns the decoded video frame indicated by the frame number.
- [func releaseFrame(IOSurface!)](./compressormediadecoder/releaseframe%28_%29.md)
  Release a decoded frame when the encoder extension no longer needs the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressormediadecoderptr)*