# UTTypeImage

**Framework**: Uniform Type Identifiers  
**Kind**: var  
**Role**: Global Variable

A base type that represents image data.

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
extern UTType * const UTTypeImage;
```

## Discussion

The identifier for this type is `public.image`.

This type conforms to [`UTTypeData`](./uttypedata.md) and [`UTTypeContent`](./uttypecontent.md).

## See Also

### Image, audio, and video base types
- [UTTypeAudio](./uttypeaudio.md)
  A type that represents audio that doesn’t contain video.
- [UTTypeAudiovisualContent](./uttypeaudiovisualcontent.md)
  A base type that represents data that contains video content that may or may not also include audio.
- [UTTypeMovie](./uttypemovie.md)
  A base type representing media formats that may contain both video and audio.
- [UTTypeVideo](./uttypevideo.md)
  A type that represents video that doesn’t contain audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeimage)*