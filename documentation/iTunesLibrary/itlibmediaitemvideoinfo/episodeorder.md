# episodeOrder

**Framework**: iTunes Library  
**Kind**: property

The numerical order of the episode, if the media item is an episode of a TV series.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var episodeOrder: Int { get }
```

#### Discussion

This property is `0` if the media item isn’t an episode of a TV series.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibmediaitemvideoinfo/episodeorder)*