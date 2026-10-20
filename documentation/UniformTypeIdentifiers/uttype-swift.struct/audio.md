# audio

**Framework**: Uniform Type Identifiers  
**Kind**: property  
**Role**: Type Property

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

This type conforms to [`UTTypeAudiovisualContent`](../uttypeaudiovisualcontent.md).

## See Also

### Image, audio, and video base types
- [static var image: UTType](./image.md)
  A base type that represents image data.
- [static var audiovisualContent: UTType](./audiovisualcontent.md)
  A base type that represents data that contains video content that may or may not also include audio.
- [static var movie: UTType](./movie.md)
  A base type representing media formats that may contain both video and audio.
- [static var video: UTType](./video.md)
  A type that represents video that doesn’t contain audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/audio)*