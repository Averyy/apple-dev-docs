# releaseFrame(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Release a decoded frame when the encoder extension no longer needs the frame.

**Availability**:
- ProVideo Encoder Extensions 1.0.2+

## Declaration

```swift
func releaseFrame(_ frame: IOSurface!)
```

```objc
- (void) releaseFrame:(IOSurface *) frame;
```

## Discussion

Use the `releaseFrame:` method to release a frame that the extension obtains by using the `copyFrame:` method and to notify the decoder that the encoder extension no longer needs the frame.

When you use the Objective-C manual reference-counting implementation, call the `releaseFrame:` method before the `frame release` call to insure the `releaseFrame:` method receives a valid frame.

## Parameters

- `frame`: The decoded frame to release.

## See Also

### Getting Decoded Frames and Samples
- [func copyAudio(atStart: Int64, count: UnsafeMutablePointer<Int64>!) -> Data!](./copyaudio%28atstart,count%29.md)
  Returns decoded audio samples starting from the specified temporal position.
- [func copyCloseCaptionData(Int64, frameCount: Int64) -> [AnyHashable : Any]!](./copyclosecaptiondata%28_,framecount%29.md)
  Returns a list of closed-caption tracks associated with the specified video frames.
- [func copyFrame(Int64) -> IOSurface!](./copyframe%28_%29.md)
  Returns the decoded video frame indicated by the frame number.
- [typealias CompressorMediaDecoderPtr](../compressormediadecoderptr.md)
  The type alias for referencing the decoder object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressormediadecoder/releaseframe(_:))*