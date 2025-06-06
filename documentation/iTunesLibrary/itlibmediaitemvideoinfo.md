# ITLibMediaItemVideoInfo

**Framework**: iTunes Library  
**Kind**: class

This class encapsulates the video information of a video media item.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
class ITLibMediaItemVideoInfo
```

#### Overview

Video media items include TV shows, movies, and video podcasts.

## Topics

### Getting Video Information
- [var videoWidth: Int](itlibmediaitemvideoinfo/videowidth.md)
  The width of the video in pixels.
- [var videoHeight: Int](itlibmediaitemvideoinfo/videoheight.md)
  The height of the video in pixels.
- [var series: String?](itlibmediaitemvideoinfo/series.md)
  The name of the corresponding TV series, if the media item is an episode in a TV series.
- [var sortSeries: String?](itlibmediaitemvideoinfo/sortseries.md)
  The sorting name of the corresponding TV series, if the media item is an episode in a TV series.
- [var season: Int](itlibmediaitemvideoinfo/season.md)
  The corresponding TV season, if the media item is an episode of a TV series.
- [var isHD: Bool](itlibmediaitemvideoinfo/ishd.md)
  A Boolean value that indicates whether the video is high-definition.
- [var episode: String?](itlibmediaitemvideoinfo/episode.md)
  The name of the episode, if the media item is an episode of a TV series.
- [var episodeOrder: Int](itlibmediaitemvideoinfo/episodeorder.md)
  The numerical order of the episode, if the media item is an episode of a TV series.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ITLibMediaItem](itlibmediaitem.md)
  This class describes a media item (a track) in the iTunes library, such as a song, a video, or a podcast.
- [class ITLibMediaEntity](itlibmediaentity.md)
  This class describes a media entity, which can be a media item, such as an audio track.
- [class ITLibArtist](itlibartist.md)
  This class represents an artist, such as the performer of a song.
- [class ITLibArtwork](itlibartwork.md)
  This class represents the artwork for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibmediaitemvideoinfo)*