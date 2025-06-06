# audio

**Framework**: Uniform Type Identifiers  
**Kind**: property

A type that represents audio that doesn’t contain video.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var audio: UTType { get }
```

#### Discussion

The identifier for this type is `public.audio`.

This type conforms to [`UTTypeAudiovisualContent`](uttypeaudiovisualcontent.md).

## See Also

- [static var image: UTType](uttype-swift.struct/image.md)
  A base type that represents image data.
- [static var audiovisualContent: UTType](uttype-swift.struct/audiovisualcontent.md)
  A base type that represents data that contains video content that may or may not also include audio.
- [static var movie: UTType](uttype-swift.struct/movie.md)
  A base type representing media formats that may contain both video and audio.
- [static var video: UTType](uttype-swift.struct/video.md)
  A type that represents video that doesn’t contain audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/audio)*