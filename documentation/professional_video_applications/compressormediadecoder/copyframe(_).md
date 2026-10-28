# copyFrame(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the decoded video frame indicated by the frame number.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func copyFrame(_ frameNumber: Int64) -> IOSurface!
```

```objc
- (IOSurface *) copyFrame:(int64_t) frameNumber;
```

## Return Value

IOSurface-based video frame buffers.

## Discussion

Use the values in the [`decodingAttributes()`](./decodingattributes%28%29.md) dictionary to find the video attributes, such as height and pixel ratio, of the decoded frame.

## Parameters

- `frameNumber`: The video frame to retrieve.

## See Also

### Getting Decoded Frames and Samples
- [func copyAudio(atStart: Int64, count: UnsafeMutablePointer<Int64>!) -> Data!](./copyaudio%28atstart,count%29.md)
  Returns decoded audio samples starting from the specified temporal position.
- [func copyCloseCaptionData(Int64, frameCount: Int64) -> [AnyHashable : Any]!](./copyclosecaptiondata%28_,framecount%29.md)
  Returns a list of closed-caption tracks associated with the specified video frames.
- [func releaseFrame(IOSurface!)](./releaseframe%28_%29.md)
  Release a decoded frame when the encoder extension no longer needs the frame.
- [typealias CompressorMediaDecoderPtr](../compressormediadecoderptr.md)
  The type alias for referencing the decoder object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressormediadecoder/copyframe(_:))*