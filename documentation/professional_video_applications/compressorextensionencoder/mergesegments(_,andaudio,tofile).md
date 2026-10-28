# mergeSegments(_:andAudio:toFile:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Merges multiple encoded video segments with an encoded audio segment.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func mergeSegments(_ videoSegments: [Any]!, andAudio audioSegment: URL!, toFile file: URL!)
```

```objc
- (void) mergeSegments:(NSArray *) videoSegments andAudio:(NSURL *) audioSegment toFile:(NSURL *) file;
```

## Discussion

During a distributed encoding process, the encoder extension processes audio and video segments separately on the available encoder instances. Once the encoding job completes, the Compressor app invokes [`mergeSegments(_:andAudio:toFile:)`](./mergesegments%28_,andaudio,tofile%29.md): on one of the encoder instances with an audio segment URL, a list of video segment URLs, and the desired output file URL. Implement this method to merge multiple encoded video segments in order, with a complete audio segment, into a single output file.

Install an encoder extension on each node of the cluster that is participating in the encoding process.

## Parameters

- `videoSegments`: An array of encoded video segment URLs.
- `audioSegment`: An encoded audio segment URL.
- `file`: The destination file URL at which to place the merged segments.

## See Also

### Encoding and Merging Segments
- [func runTranscode(for: CompressorMediaDecoderPtr!, start: Int64, duration: Int64, toFile: URL!, startTimeCode: [AnyHashable : Any]!)](./runtranscode%28for,start,duration,tofile,starttimecode%29.md)
  Encodes the source media files to an output format based on the encoder settings.
- [typealias CompressorExtensionEncoderPtr](../compressorextensionencoderptr.md)
  The type alias to use for referencing the `CompressorExtensionEncoder` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionencoder/mergesegments(_:andaudio:tofile:))*