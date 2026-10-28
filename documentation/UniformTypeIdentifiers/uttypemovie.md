# UTTypeMovie

**Framework**: Uniform Type Identifiers  
**Kind**: var  
**Role**: Global Variable

A base type representing media formats that may contain both video and audio.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```c
extern UTType * const UTTypeMovie;
```

## Discussion

This type corresponds to what users would label a “movie”.

The identifier for this type is `public.movie`.

This type conforms to [`UTTypeAudiovisualContent`](./uttypeaudiovisualcontent.md).

## See Also

### Image, audio, and video base types
- [UTTypeImage](./uttypeimage.md)
  A base type that represents image data.
- [UTTypeAudio](./uttypeaudio.md)
  A type that represents audio that doesn’t contain video.
- [UTTypeAudiovisualContent](./uttypeaudiovisualcontent.md)
  A base type that represents data that contains video content that may or may not also include audio.
- [UTTypeVideo](./uttypevideo.md)
  A type that represents video that doesn’t contain audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypemovie)*