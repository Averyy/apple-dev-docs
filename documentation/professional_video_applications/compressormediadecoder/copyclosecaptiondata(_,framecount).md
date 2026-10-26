# copyCloseCaptionData(_:frameCount:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a list of closed-caption tracks associated with the specified video frames.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func copyCloseCaptionData(_ startFrame: Int64, frameCount: Int64) -> [AnyHashable : Any]!
```

```objc
- (NSDictionary *) copyCloseCaptionData:(int64_t) startFrame frameCount:(int64_t) frameCount;
```

#### Return Value

`nil` if closed-caption data is not available. Otherwise, it returns a dictionary with a frame number as the key, and a value that’s an array of 16-bit integers representing the closed-caption data.

#### Discussion

> **Note**:  The decoder object supports only CEA-608 closed-caption format.

## Parameters

- `startFrame`: The frame number at which to start collecting the closed-caption data.
- `frameCount`: The number of frames to retrieve the closed-caption data from.

## See Also

### Getting Decoded Frames and Samples
- [func copyAudio(atStart: Int64, count: UnsafeMutablePointer<Int64>!) -> Data!](./copyaudio%28atstart,count%29.md)
  Returns decoded audio samples starting from the specified temporal position.
- [func copyFrame(Int64) -> IOSurface!](./copyframe%28_%29.md)
  Returns the decoded video frame indicated by the frame number.
- [func releaseFrame(IOSurface!)](./releaseframe%28_%29.md)
  Release a decoded frame when the encoder extension no longer needs the frame.
- [typealias CompressorMediaDecoderPtr](../compressormediadecoderptr.md)
  The type alias for referencing the decoder object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressormediadecoder/copyclosecaptiondata(_:framecount:))*