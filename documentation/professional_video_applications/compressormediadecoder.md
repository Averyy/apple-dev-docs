# CompressorMediaDecoder

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

An interface with methods you use to retrieve decoded video, audio, and image data from a source media file.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
protocol CompressorMediaDecoder
```

```objc
@protocol CompressorMediaDecoder
```

## Overview

The Compressor app configures a decoder object to produce decoded video frames and audio samples based on the encoder attributes and source media properties.

During the encoding process, the Compressor app provides this decoder object to the extension. Call the methods in the decoder object to get:

- Source video frames at the width, height, and frame rate specified in the decoding attributes.
- Audio samples at the sample rate and channel layout specified in the encoder settings.
- Uncompressed images from the decoder object with an image format that the extension, the source media, and the Compressor app filters support.
- Closed-caption data and details of the source media timecode.

## Topics

### Getting Decoded Frames and Samples
- [func copyAudio(atStart: Int64, count: UnsafeMutablePointer<Int64>!) -> Data!](./compressormediadecoder/copyaudio%28atstart,count%29.md)
  Returns decoded audio samples starting from the specified temporal position.
- [func copyCloseCaptionData(Int64, frameCount: Int64) -> [AnyHashable : Any]!](./compressormediadecoder/copyclosecaptiondata%28_,framecount%29.md)
  Returns a list of closed-caption tracks associated with the specified video frames.
- [func copyFrame(Int64) -> IOSurface!](./compressormediadecoder/copyframe%28_%29.md)
  Returns the decoded video frame indicated by the frame number.
- [func releaseFrame(IOSurface!)](./compressormediadecoder/releaseframe%28_%29.md)
  Release a decoded frame when the encoder extension no longer needs the frame.
- [typealias CompressorMediaDecoderPtr](./compressormediadecoderptr.md)
  The type alias for referencing the decoder object.
### Getting Decoding Attributes
- [func decodingAttributes() -> [AnyHashable : Any]!](./compressormediadecoder/decodingattributes%28%29.md)
  Returns a set of video attributes of the decoded source media file.
- [func startTimeCodeForMedia() -> [AnyHashable : Any]!](./compressormediadecoder/starttimecodeformedia%28%29.md)
  Returns the source media timecode details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressormediadecoder)*