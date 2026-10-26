# CompressorExtensionEncoderPtr

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

The type alias to use for referencing the `CompressorExtensionEncoder` object.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
typealias CompressorExtensionEncoderPtr = any NSObjectProtocol & CompressorExtensionEncoder
```

```c
typedef NSObject<CompressorExtensionEncoder> * CompressorExtensionEncoderPtr;
```

## See Also

### Encoding and Merging Segments
- [func runTranscode(for: CompressorMediaDecoderPtr!, start: Int64, duration: Int64, toFile: URL!, startTimeCode: [AnyHashable : Any]!)](./compressorextensionencoder/runtranscode%28for,start,duration,tofile,starttimecode%29.md)
  Encodes the source media files to an output format based on the encoder settings.
- [func mergeSegments([Any]!, andAudio: URL!, toFile: URL!)](./compressorextensionencoder/mergesegments%28_,andaudio,tofile%29.md)
  Merges multiple encoded video segments with an encoded audio segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionencoderptr)*