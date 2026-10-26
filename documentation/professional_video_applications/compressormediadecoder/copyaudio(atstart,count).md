# copyAudio(atStart:count:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns decoded audio samples starting from the specified temporal position.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func copyAudio(atStart start: Int64, count: UnsafeMutablePointer<Int64>!) -> Data!
```

```objc
- (NSData *) copyAudioAtStart:(int64_t) start count:(int64_t *) count;
```

#### Return Value

A data buffer with decoded audio samples at the sample rate and channel layout specified in the encoder settings.

#### Discussion

If the decoder does not have enough samples to return as specified in the `count` parameter, it updates the `count` parameter with the actual number of samples in the returned audio data buffer.

> **Note**:  It’s recommended that you call the decoder for audio samples of 1 second per call, in temporal order.

## Parameters

- `start`: The temporal position of the audio sample.
- `count`: On input, the number of audio samples to return; on output, the actual number of samples returned.

## See Also

### Getting Decoded Frames and Samples
- [func copyCloseCaptionData(Int64, frameCount: Int64) -> [AnyHashable : Any]!](./copyclosecaptiondata%28_,framecount%29.md)
  Returns a list of closed-caption tracks associated with the specified video frames.
- [func copyFrame(Int64) -> IOSurface!](./copyframe%28_%29.md)
  Returns the decoded video frame indicated by the frame number.
- [func releaseFrame(IOSurface!)](./releaseframe%28_%29.md)
  Release a decoded frame when the encoder extension no longer needs the frame.
- [typealias CompressorMediaDecoderPtr](../compressormediadecoderptr.md)
  The type alias for referencing the decoder object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressormediadecoder/copyaudio(atstart:count:))*