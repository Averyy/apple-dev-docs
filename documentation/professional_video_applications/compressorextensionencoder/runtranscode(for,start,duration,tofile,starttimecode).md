# runTranscode(for:start:duration:toFile:startTimeCode:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes the source media files to an output format based on the encoder settings.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func runTranscode(for decoder: CompressorMediaDecoderPtr!, start startFrame: Int64, duration numFrames: Int64, toFile file: URL!, startTimeCode timeCodeDictionary: [AnyHashable : Any]!)
```

```objc
- (void) runTranscodeFor:(CompressorMediaDecoderPtr) decoder start:(int64_t) startFrame duration:(int64_t) numFrames toFile:(NSURL *) file startTimeCode:(NSDictionary *) timeCodeDictionary;
```

## Discussion

The Compressor app invokes this method to run an encoding job. Implement this method to transcode media files from the source format into an output format your extension supports. Inside the implementation, call the decoder interface methods to get individual video frames and audio samples to encode.

## Parameters

- `decoder`: A pointer to the decoder interface object.
- `startFrame`: The frame at which to start encoding.
- `numFrames`: The number of frames to encode.
- `file`: The destination file URL to put the encoded file into.
- `timeCodeDictionary`: A dictionary that contains timecode information about the source media. This dictionary has the following keys:

  - **`hours`, `minutes`, `seconds`, `frames`**: Integer
  - **`frameRate`**: Double
  - **`isDrop`**: Bool
  - **`reelName`**: NSString

## See Also

### Encoding and Merging Segments
- [func mergeSegments([Any]!, andAudio: URL!, toFile: URL!)](./mergesegments%28_,andaudio,tofile%29.md)
  Merges multiple encoded video segments with an encoded audio segment.
- [typealias CompressorExtensionEncoderPtr](../compressorextensionencoderptr.md)
  The type alias to use for referencing the `CompressorExtensionEncoder` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionencoder/runtranscode(for:start:duration:tofile:starttimecode:))*