# image

**Framework**: Uniform Type Identifiers  
**Kind**: property

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

```swift
static var image: UTType { get }
```

#### Discussion

The identifier for this type is `public.image`.

This type conforms to [`UTTypeData`](uttypedata.md) and [`UTTypeContent`](uttypecontent.md).

## See Also

- [static var audio: UTType](uttype-swift.struct/audio.md)
  A type that represents audio that doesn’t contain video.
- [static var audiovisualContent: UTType](uttype-swift.struct/audiovisualcontent.md)
  A base type that represents data that contains video content that may or may not also include audio.
- [static var movie: UTType](uttype-swift.struct/movie.md)
  A base type representing media formats that may contain both video and audio.
- [static var video: UTType](uttype-swift.struct/video.md)
  A type that represents video that doesn’t contain audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/image)*